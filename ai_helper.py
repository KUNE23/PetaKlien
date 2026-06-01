from __future__ import annotations

from typing import Any

from config import settings

Lead = dict[str, Any]


def generate_proposal_draft(lead: Lead) -> str:
    """Generate draft only. The bot must never send proposals automatically."""
    nama = lead.get("nama_bisnis", "bisnis Kakak")
    kategori = lead.get("kategori", "usaha")

    if settings.ai_api_key and settings.ai_provider:
        # Hook untuk integrasi AI resmi di masa depan. Tetap return template agar MVP tidak bergantung API.
        pass

    return (
        f"Halo Kak, saya melihat {nama} aktif di bidang {kategori}. "
        "Saya ingin menawarkan pembuatan website sederhana untuk membantu pelanggan melihat informasi seperti "
        "profil usaha, katalog/menu, lokasi, jam buka, dan tombol WhatsApp. Jika berkenan, saya bisa kirimkan "
        "contoh konsep websitenya."
    )


def summarize_daily_report(leads: list[Lead]) -> str:
    total = len(leads)
    no_website = sum(1 for lead in leads if lead.get("status_website") == "Belum ada")
    social_only = sum(1 for lead in leads if lead.get("status_website") == "Hanya sosial media")
    approved = sum(1 for lead in leads if lead.get("status") == "approved")

    if total == 0:
        return "Belum ada lead yang tercatat hari ini."

    top_leads = sorted(leads, key=lambda item: int(item.get("skor_peluang", 0)), reverse=True)[:3]
    top_text = ", ".join(
        f"{lead.get('nama_bisnis')} ({lead.get('skor_peluang')}/10)" for lead in top_leads
    )

    return (
        f"Laporan hari ini: {total} lead tercatat, {no_website} belum punya website, "
        f"{social_only} hanya memakai sosial media, {approved} sudah approved. "
        f"Prioritas: {top_text}."
    )

