from __future__ import annotations

from urllib.parse import urlparse


SOCIAL_DOMAINS = (
    "instagram.com",
    "facebook.com",
    "fb.com",
    "tiktok.com",
    "x.com",
    "twitter.com",
    "linkedin.com",
    "wa.me",
    "api.whatsapp.com",
)


def normalize_url(url: str | None) -> str:
    value = (url or "").strip()
    if not value:
        return ""
    if not value.startswith(("http://", "https://")):
        return f"https://{value}"
    return value


def _hostname(url: str) -> str:
    parsed = urlparse(normalize_url(url))
    return (parsed.netloc or parsed.path).lower().removeprefix("www.")


def is_social_media_url(url: str | None) -> bool:
    if not url:
        return False
    host = _hostname(url)
    return any(host == domain or host.endswith(f".{domain}") for domain in SOCIAL_DOMAINS)


def is_real_website(url: str | None) -> bool:
    if not url:
        return False
    host = _hostname(url)
    if "." not in host:
        return False
    return not is_social_media_url(url)


def get_website_status(website: str | None) -> str:
    if not website or not website.strip():
        return "Belum ada"
    if is_social_media_url(website):
        return "Hanya sosial media"
    if is_real_website(website):
        return "Punya website"
    return "Belum ada"

