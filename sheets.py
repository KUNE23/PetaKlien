from __future__ import annotations

import logging
from pathlib import Path
from typing import Any

from config import settings

logger = logging.getLogger(__name__)

Lead = dict[str, Any]

LEAD_COLUMNS = [
    "tanggal",
    "nama_bisnis",
    "kategori",
    "kota",
    "kontak",
    "kontak_bisa_dihubungi",
    "email",
    "instagram",
    "website",
    "google_maps_link",
    "status_website",
    "sumber",
    "skor_peluang",
    "status",
    "catatan",
]

REPORT_COLUMNS = [
    "tanggal",
    "total",
    "valid",
    "belum_punya_website",
    "hanya_sosial_media",
    "kontak_prioritas",
    "google_maps_prioritas",
    "ringkasan",
]


def is_google_sheets_configured() -> bool:
    return bool(settings.google_service_account_file and settings.google_sheet_id)


def _import_google_libs() -> tuple[Any, Any]:
    try:
        import gspread
        from google.oauth2.service_account import Credentials
    except ImportError as exc:
        raise RuntimeError(
            "Dependency Google Sheets belum terpasang. Jalankan: pip install -r requirements.txt"
        ) from exc
    return gspread, Credentials


def _client() -> Any:
    if not settings.google_service_account_file:
        raise ValueError("GOOGLE_SERVICE_ACCOUNT_FILE belum diisi.")
    if not Path(settings.google_service_account_file).exists():
        raise FileNotFoundError(
            f"File service account tidak ditemukan: {settings.google_service_account_file}"
        )
    gspread, Credentials = _import_google_libs()
    scopes = ["https://www.googleapis.com/auth/spreadsheets"]
    credentials = Credentials.from_service_account_file(settings.google_service_account_file, scopes=scopes)
    return gspread.authorize(credentials)


def _worksheet(tab_name: str | None = None) -> Any:
    if not settings.google_sheet_id:
        raise ValueError("GOOGLE_SHEET_ID belum diisi.")
    gspread, _ = _import_google_libs()
    spreadsheet = _client().open_by_key(settings.google_sheet_id)
    name = tab_name or settings.google_sheet_tab
    try:
        return spreadsheet.worksheet(name)
    except gspread.WorksheetNotFound:
        return spreadsheet.add_worksheet(title=name, rows=1000, cols=20)


def _ensure_header(ws: Any, columns: list[str]) -> None:
    existing = ws.row_values(1)
    if existing[: len(columns)] != columns:
        ws.update("A1", [columns])


def append_lead(lead: Lead) -> None:
    try:
        logger.info("Sinkronisasi lead ke Google Sheets: %s", lead.get("nama_bisnis"))
        ws = _worksheet()
        _ensure_header(ws, LEAD_COLUMNS)
        ws.append_row([lead.get(column, "") for column in LEAD_COLUMNS], value_input_option="USER_ENTERED")
    except Exception:
        logger.exception("Gagal append lead ke Google Sheets")
        raise


def append_daily_report(report: dict[str, Any]) -> None:
    try:
        logger.info("Sinkronisasi laporan harian ke Google Sheets")
        ws = _worksheet("Reports")
        _ensure_header(ws, REPORT_COLUMNS)
        ws.append_row([report.get(column, "") for column in REPORT_COLUMNS], value_input_option="USER_ENTERED")
    except Exception:
        logger.exception("Gagal append laporan harian ke Google Sheets")
        raise


def get_existing_leads() -> list[dict[str, Any]]:
    try:
        ws = _worksheet()
        _ensure_header(ws, LEAD_COLUMNS)
        return ws.get_all_records()
    except Exception:
        logger.exception("Gagal membaca lead dari Google Sheets")
        return []


def update_lead_status(lead_id: int, status: str) -> bool:
    try:
        ws = _worksheet()
        _ensure_header(ws, LEAD_COLUMNS)
        status_col = LEAD_COLUMNS.index("status") + 1
        # Spreadsheet columns follow the requested format without an id column.
        # This legacy helper only works when sheet rows follow database id order.
        row_number = lead_id + 1
        if row_number < 2:
            return False
        ws.update_cell(row_number, status_col, status)
        return True
    except Exception:
        logger.exception("Gagal update status lead di Google Sheets")
        return False
