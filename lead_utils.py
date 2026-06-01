from __future__ import annotations

from typing import Any
from urllib.parse import quote_plus


Lead = dict[str, Any]


def build_contact_summary(lead: Lead) -> str:
    contacts: list[str] = []
    if lead.get("kontak"):
        contacts.append(f"WhatsApp/Telp: {lead['kontak']}")
    if lead.get("email"):
        contacts.append(f"Email: {lead['email']}")
    if lead.get("instagram"):
        contacts.append(f"Instagram: {lead['instagram']}")
    return " | ".join(contacts) if contacts else ""


def build_google_maps_link(lead: Lead) -> str:
    name = str(lead.get("nama_bisnis", "")).strip()
    city = str(lead.get("kota", "")).strip()
    if not name and not city:
        return ""
    query = quote_plus(" ".join(part for part in (name, city) if part))
    return f"https://www.google.com/maps/search/?api=1&query={query}"


def ensure_contact_and_maps(lead: Lead) -> Lead:
    enriched = dict(lead)
    enriched["kontak_bisa_dihubungi"] = enriched.get("kontak_bisa_dihubungi") or build_contact_summary(enriched)
    enriched["google_maps_link"] = enriched.get("google_maps_link") or build_google_maps_link(enriched)
    return enriched
