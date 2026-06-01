from __future__ import annotations

import logging

from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS

from ai_helper import generate_proposal_draft, summarize_daily_report
from config import BASE_DIR, ConfigError, settings
from database import (
    get_all_leads,
    get_dashboard_stats,
    get_lead_by_id,
    get_today_leads,
    is_supabase_configured,
    update_status,
)
from lead_utils import ensure_contact_and_maps

logger = logging.getLogger(__name__)


def _frontend_dist() -> str:
    return str(BASE_DIR / "frontend" / "dist")


def create_app() -> Flask:
    app = Flask(__name__, static_folder=_frontend_dist(), static_url_path="")
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    @app.get("/")
    def index():
        dist_index = BASE_DIR / "frontend" / "dist" / "index.html"
        if dist_index.exists():
            return send_from_directory(_frontend_dist(), "index.html")
        return jsonify(
            {
                "app": "PetaKlien API",
                "message": "Frontend Vue belum dibuild. Jalankan: cd frontend && npm install && npm run dev",
                "api": "/api/dashboard",
            }
        )

    @app.get("/api/config")
    def api_config():
        return jsonify(
            {
                "default_city": settings.city,
                "default_categories": settings.business_categories,
                "default_radius_km": settings.default_search_radius_km,
                "google_maps_browser_api_key": settings.google_maps_browser_api_key,
                "supabase_configured": is_supabase_configured(),
            }
        )

    @app.get("/api/dashboard")
    def api_dashboard():
        if not is_supabase_configured():
            return jsonify(
                {
                    "leads": [],
                    "stats": {
                        "total": 0,
                        "draft": 0,
                        "approved": 0,
                        "no_website": 0,
                        "social_only": 0,
                        "today": 0,
                    },
                    "today_summary": "Mode publik tidak menyimpan data ke database.",
                }
            )

        status_filter = request.args.get("status", "all")
        website_filter = request.args.get("website", "all")
        search = request.args.get("q", "").strip().lower()

        leads = [ensure_contact_and_maps(lead) for lead in get_all_leads()]
        if status_filter != "all":
            leads = [lead for lead in leads if lead.get("status") == status_filter]
        if website_filter != "all":
            leads = [lead for lead in leads if lead.get("status_website") == website_filter]
        if search:
            leads = [
                lead
                for lead in leads
                if search in str(lead.get("nama_bisnis", "")).lower()
                or search in str(lead.get("kategori", "")).lower()
                or search in str(lead.get("kota", "")).lower()
            ]

        today_leads = [ensure_contact_and_maps(lead) for lead in get_today_leads()]
        return jsonify(
            {
                "leads": leads,
                "stats": get_dashboard_stats(),
                "today_summary": summarize_daily_report(today_leads),
            }
        )

    def _run_public_search():
        from main import run_find_once

        payload = request.get_json(silent=True) or {}
        target_city = str(payload.get("city", "")).strip()
        if not target_city:
            return jsonify({"error": "Isi kota/area target terlebih dahulu."}), 400

        categories = payload.get("categories") or settings.business_categories
        if isinstance(categories, str):
            categories = [item.strip() for item in categories.split(",") if item.strip()]

        try:
            radius_km = max(int(payload.get("radius_km") or settings.default_search_radius_km), 1)
            limit = max(int(payload.get("limit") or settings.daily_lead_limit), 1)
            latitude = float(payload["latitude"]) if payload.get("latitude") not in (None, "") else None
            longitude = float(payload["longitude"]) if payload.get("longitude") not in (None, "") else None
            no_website_only = bool(payload.get("no_website_only"))
        except (TypeError, ValueError):
            return jsonify({"error": "Radius atau koordinat tidak valid."}), 400

        try:
            result = run_find_once(
                city=target_city,
                categories=list(categories),
                radius_km=radius_km,
                latitude=latitude,
                longitude=longitude,
                limit=limit,
                no_website_only=no_website_only,
            )
        except ConfigError as exc:
            return jsonify({"error": str(exc)}), 400

        return jsonify({"result": result, "leads": result.get("leads", [])})

    @app.post("/api/find")
    def api_find_leads():
        return _run_public_search()

    @app.post("/api/find-public")
    def api_find_public():
        return _run_public_search()

    @app.get("/api/leads/<int:lead_id>")
    def api_lead_detail(lead_id: int):
        lead = get_lead_by_id(lead_id)
        if not lead:
            return jsonify({"error": "Lead tidak ditemukan."}), 404
        lead = ensure_contact_and_maps(lead)
        return jsonify({"lead": lead, "proposal": generate_proposal_draft(lead)})

    @app.patch("/api/leads/<int:lead_id>/status")
    def api_change_status(lead_id: int):
        payload = request.get_json(silent=True) or {}
        new_status = payload.get("status", "draft")
        try:
            changed = update_status(lead_id, new_status)
        except (ConfigError, ValueError) as exc:
            return jsonify({"error": str(exc)}), 400
        except Exception as exc:
            logger.exception("Gagal update status lead")
            return jsonify({"error": str(exc)}), 500

        if not changed:
            return jsonify({"error": "Lead tidak ditemukan."}), 404
        return jsonify({"ok": True, "status": new_status})

    @app.get("/<path:path>")
    def frontend_fallback(path: str):
        dist = BASE_DIR / "frontend" / "dist"
        target = dist / path
        if target.exists() and target.is_file():
            return send_from_directory(_frontend_dist(), path)
        if (dist / "index.html").exists():
            return send_from_directory(_frontend_dist(), "index.html")
        return jsonify({"error": "Frontend Vue belum dibuild."}), 404

    return app
