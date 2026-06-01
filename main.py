from __future__ import annotations

import argparse
import logging
import sys
from datetime import datetime
from typing import Any

from ai_helper import summarize_daily_report
from config import ConfigError, settings, setup_logging
from lead_finder import search_businesses
from lead_utils import ensure_contact_and_maps
from sheets import append_daily_report, is_google_sheets_configured

logger = logging.getLogger(__name__)


def run_find_once(
    city: str | None = None,
    categories: list[str] | None = None,
    radius_km: int | None = None,
    latitude: float | None = None,
    longitude: float | None = None,
    limit: int | None = None,
    no_website_only: bool = False,
) -> dict[str, Any]:
    """Search public lead data without saving to shared storage."""
    target_city = city or settings.city
    target_categories = categories or settings.business_categories
    target_radius_km = radius_km or settings.default_search_radius_km
    logger.info(
        "Mulai pencarian publik: city=%s, radius_km=%s, lat=%s, lng=%s, categories=%s, daily_limit=%s",
        target_city,
        target_radius_km,
        latitude,
        longitude,
        ", ".join(target_categories),
        settings.daily_lead_limit,
    )

    found = 0
    valid = 0
    no_website = 0
    leads: list[dict[str, Any]] = []
    search_limit = max(limit or settings.daily_lead_limit, 1)

    for category in target_categories:
        logger.info(
            "Mencari lead kategori=%s kota=%s radius_km=%s limit=%s",
            category,
            target_city,
            target_radius_km,
            search_limit,
        )
        candidates = search_businesses(
            target_city,
            category,
            search_limit,
            radius_km=target_radius_km,
            latitude=latitude,
            longitude=longitude,
        )
        found += len(candidates)
        logger.info("Kandidat ditemukan untuk %s: %s", category, len(candidates))

        for lead in candidates:
            if not lead.get("nama_bisnis") or not lead.get("kota"):
                continue

            valid += 1
            if lead.get("status_website") in {"Belum ada", "Hanya sosial media"}:
                no_website += 1

            if no_website_only and lead.get("status_website") not in {"Belum ada", "Hanya sosial media"}:
                continue

            if len(leads) >= search_limit:
                break

            leads.append(ensure_contact_and_maps(lead))

        if len(leads) >= search_limit:
            break

    priority_leads = sorted(
        leads,
        key=lambda lead: int(lead.get("skor_peluang", 0) or 0),
        reverse=True,
    )[:5]
    report: dict[str, Any] = {
        "tanggal": datetime.now().date().isoformat(),
        "total": len(leads),
        "valid": valid,
        "belum_punya_website": sum(1 for lead in leads if lead.get("status_website") == "Belum ada"),
        "hanya_sosial_media": sum(1 for lead in leads if lead.get("status_website") == "Hanya sosial media"),
        "kontak_prioritas": "\n".join(
            f"{lead.get('nama_bisnis')}: {lead.get('kontak_bisa_dihubungi', '')}" for lead in priority_leads
        ),
        "google_maps_prioritas": "\n".join(
            f"{lead.get('nama_bisnis')}: {lead.get('google_maps_link', '')}" for lead in priority_leads
        ),
        "ringkasan": summarize_daily_report(leads),
    }

    result: dict[str, Any] = {
        "found": found,
        "valid": valid,
        "no_website": no_website,
        "saved": 0,
        "returned": len(leads),
        "total": len(leads),
        "leads": leads,
        "report": report,
    }
    logger.info("Pencarian selesai: %s", result)
    return result


def test_sheets() -> None:
    if not is_google_sheets_configured():
        raise ConfigError(
            "Google Sheets belum dikonfigurasi. Isi GOOGLE_SERVICE_ACCOUNT_FILE dan GOOGLE_SHEET_ID di .env."
        )
    append_daily_report(
        {
            "tanggal": datetime.now().date().isoformat(),
            "total": 0,
            "valid": 0,
            "belum_punya_website": 0,
            "hanya_sosial_media": 0,
            "kontak_prioritas": "Contoh: WhatsApp/Telp, Email, atau Instagram lead prioritas.",
            "google_maps_prioritas": "Contoh: https://www.google.com/maps/search/?api=1&query=Nama+Bisnis+Kota",
            "ringkasan": "Tes koneksi Google Sheets berhasil.",
        }
    )
    print("Tes Google Sheets berhasil.")


def run_web() -> None:
    from web_app import create_app

    app = create_app()
    logger.info("Menjalankan PetaKlien web UI di http://%s:%s", settings.web_host, settings.web_port)
    app.run(host=settings.web_host, port=settings.web_port, debug=False)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Lead Finder Bot")
    parser.add_argument(
        "command",
        choices=["web", "find", "test-sheets"],
        help="Perintah yang ingin dijalankan.",
    )
    return parser.parse_args()


def main() -> None:
    setup_logging()
    args = parse_args()

    if args.command == "web":
        run_web()
    elif args.command == "find":
        result = run_find_once()
        print(result)
    elif args.command == "test-sheets":
        test_sheets()


if __name__ == "__main__":
    setup_logging()
    try:
        main()
    except KeyboardInterrupt:
        logger.info("Dihentikan oleh user.")
        sys.exit(130)
    except ConfigError as exc:
        logger.error("Command gagal: %s", exc)
        if logger.isEnabledFor(logging.DEBUG):
            logger.exception("Detail error konfigurasi")
        sys.exit(1)
    except Exception as exc:
        logger.exception("Command gagal: %s", exc)
        sys.exit(1)
