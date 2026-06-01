from __future__ import annotations

import logging
import os
from dataclasses import dataclass
from pathlib import Path

try:
    from dotenv import load_dotenv
except ImportError:  # pragma: no cover - useful before requirements are installed
    load_dotenv = None  # type: ignore[assignment]


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"


def _split_csv(value: str) -> list[str]:
    return [item.strip() for item in value.split(",") if item.strip()]


def _resolve_project_path(value: str) -> str:
    if not value:
        return ""
    path = Path(value).expanduser()
    if path.is_absolute():
        return str(path)
    return str(BASE_DIR / path)


@dataclass(frozen=True)
class Settings:
    google_service_account_file: str
    google_sheet_id: str
    google_sheet_tab: str
    supabase_url: str
    supabase_key: str
    supabase_database_url: str
    ai_provider: str
    ai_api_key: str
    city: str
    business_categories: list[str]
    daily_lead_limit: int
    log_level: str
    log_file: str
    web_host: str
    web_port: int
    google_maps_browser_api_key: str
    default_search_radius_km: int


def load_settings() -> Settings:
    if load_dotenv:
        load_dotenv(BASE_DIR / ".env")

    categories = _split_csv(
        os.getenv(
            "BUSINESS_CATEGORIES",
            "restoran,cafe,laundry,barbershop,bengkel,toko,klinik kecil,UMKM,sekolah kecil",
        )
    )

    try:
        daily_limit = int(os.getenv("DAILY_LEAD_LIMIT", "20"))
    except ValueError:
        daily_limit = 20
    try:
        web_port = int(os.getenv("WEB_PORT", "8000"))
    except ValueError:
        web_port = 8000
    try:
        default_search_radius_km = int(os.getenv("DEFAULT_SEARCH_RADIUS_KM", "100"))
    except ValueError:
        default_search_radius_km = 100
    service_account_file = _resolve_project_path(os.getenv("GOOGLE_SERVICE_ACCOUNT_FILE", ""))

    return Settings(
        google_service_account_file=service_account_file,
        google_sheet_id=os.getenv("GOOGLE_SHEET_ID", ""),
        google_sheet_tab=os.getenv("GOOGLE_SHEET_TAB", "Leads"),
        supabase_url=os.getenv("SUPABASE_URL", ""),
        supabase_key=os.getenv("SUPABASE_SERVICE_ROLE_KEY", "") or os.getenv("SUPABASE_ANON_KEY", ""),
        supabase_database_url=os.getenv("SUPABASE_DATABASE_URL", ""),
        ai_provider=os.getenv("AI_PROVIDER", ""),
        ai_api_key=os.getenv("AI_API_KEY", ""),
        city=os.getenv("CITY", "Jakarta"),
        business_categories=categories,
        daily_lead_limit=max(daily_limit, 1),
        log_level=os.getenv("LOG_LEVEL", "INFO").upper(),
        log_file=os.getenv("LOG_FILE", "logs/lead-finder-bot.log"),
        web_host=os.getenv("WEB_HOST", "127.0.0.1"),
        web_port=web_port,
        google_maps_browser_api_key=os.getenv("GOOGLE_MAPS_BROWSER_API_KEY", ""),
        default_search_radius_km=max(default_search_radius_km, 1),
    )


def setup_logging() -> None:
    root_logger = logging.getLogger()
    if getattr(root_logger, "_lead_finder_logging_configured", False):
        return

    level = getattr(logging, settings.log_level, logging.INFO)
    formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")
    handlers: list[logging.Handler] = [logging.StreamHandler()]

    if settings.log_file:
        log_path = Path(settings.log_file)
        if not log_path.is_absolute():
            log_path = BASE_DIR / log_path
        log_path.parent.mkdir(parents=True, exist_ok=True)
        handlers.append(logging.FileHandler(log_path, encoding="utf-8"))

    for handler in handlers:
        handler.setFormatter(formatter)

    root_logger.setLevel(level)
    root_logger.handlers.clear()
    root_logger.addHandler(handlers[0])
    for handler in handlers[1:]:
        root_logger.addHandler(handler)
    setattr(root_logger, "_lead_finder_logging_configured", True)

    if load_dotenv is None and not getattr(root_logger, "_lead_finder_dotenv_warning_shown", False):
        logging.getLogger(__name__).warning(
            "python-dotenv belum terpasang; file .env tidak dibaca. Jalankan: pip install -r requirements.txt"
        )
        setattr(root_logger, "_lead_finder_dotenv_warning_shown", True)

    # HTTP client logs can include full Telegram API URLs; keep secrets out of log files.
    logging.getLogger("httpx").setLevel(logging.WARNING)
    logging.getLogger("httpcore").setLevel(logging.WARNING)


settings = load_settings()


class ConfigError(RuntimeError):
    """Raised when required environment configuration is missing or invalid."""
