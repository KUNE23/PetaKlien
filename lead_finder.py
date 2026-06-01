from __future__ import annotations

import logging
from datetime import datetime
from typing import Any

from lead_utils import ensure_contact_and_maps
from website_checker import get_website_status

logger = logging.getLogger(__name__)

Lead = dict[str, Any]


SAMPLE_BUSINESSES: list[Lead] = [
    {
        "nama_bisnis": "Warung Makan Sari Rasa",
        "kategori": "restoran",
        "kota": "Jakarta",
        "kontak": "081234560001",
        "email": "",
        "instagram": "https://instagram.com/sarirasa.jkt",
        "website": "",
        "sumber": "sample",
        "catatan": "Aktif posting menu harian dan menerima pesanan WhatsApp.",
    },
    {
        "nama_bisnis": "Kopi Tepi Jalan",
        "kategori": "cafe",
        "kota": "Jakarta",
        "kontak": "081234560002",
        "email": "halo@kopitepijalan.test",
        "instagram": "https://instagram.com/kopitepijalan",
        "website": "https://instagram.com/kopitepijalan",
        "sumber": "sample",
        "catatan": "Aktif promosi menu baru dan sering update story.",
    },
    {
        "nama_bisnis": "Laundry Bersih Kilat",
        "kategori": "laundry",
        "kota": "Jakarta",
        "kontak": "081234560003",
        "email": "",
        "instagram": "",
        "website": "",
        "sumber": "sample",
        "catatan": "Memiliki layanan antar jemput area sekitar.",
    },
    {
        "nama_bisnis": "Barber Rapi Studio",
        "kategori": "barbershop",
        "kota": "Jakarta",
        "kontak": "081234560004",
        "email": "",
        "instagram": "https://instagram.com/barberrapi",
        "website": "",
        "sumber": "sample",
        "catatan": "Aktif menampilkan hasil potong rambut pelanggan.",
    },
    {
        "nama_bisnis": "Bengkel Maju Motor",
        "kategori": "bengkel",
        "kota": "Jakarta",
        "kontak": "081234560005",
        "email": "",
        "instagram": "",
        "website": "https://majumotor.example.com",
        "sumber": "sample",
        "catatan": "Sudah memiliki website sederhana.",
    },
    {
        "nama_bisnis": "Toko Kue Melati",
        "kategori": "toko",
        "kota": "Bandung",
        "kontak": "081234560006",
        "email": "",
        "instagram": "https://instagram.com/tokokuemelati",
        "website": "",
        "sumber": "sample",
        "catatan": "Aktif menerima pesanan kue ulang tahun.",
    },
    {
        "nama_bisnis": "Klinik Sehat Keluarga",
        "kategori": "klinik kecil",
        "kota": "Jakarta",
        "kontak": "081234560007",
        "email": "admin@kliniksehat.test",
        "instagram": "",
        "website": "",
        "sumber": "sample",
        "catatan": "Informasi jam praktik masih tersebar di sosial media.",
    },
    {
        "nama_bisnis": "Bimbel Cerdas Anak",
        "kategori": "sekolah kecil",
        "kota": "Jakarta",
        "kontak": "081234560008",
        "email": "",
        "instagram": "https://instagram.com/bimbelcerdasanak",
        "website": "https://facebook.com/bimbelcerdasanak",
        "sumber": "sample",
        "catatan": "Aktif membuka kelas baru setiap bulan.",
    },
]


LANDING_PAGE_FRIENDLY_CATEGORIES = {
    "restoran",
    "cafe",
    "laundry",
    "barbershop",
    "bengkel",
    "toko",
    "klinik kecil",
    "umkm",
    "sekolah kecil",
}

CATEGORY_ALIASES = {
    "cafe & coffee shop": "cafe",
    "coffee shop": "cafe",
    "warung kopi": "cafe",
    "restaurant": "restoran",
    "school": "sekolah kecil",
}


def normalize_category(value: str) -> str:
    normalized = value.strip().lower()
    return CATEGORY_ALIASES.get(normalized, normalized)


def calculate_score(lead: Lead) -> int:
    score = 1
    status_website = lead.get("status_website") or get_website_status(lead.get("website"))
    category = str(lead.get("kategori", "")).lower()
    note = str(lead.get("catatan", "")).lower()

    if status_website == "Belum ada":
        score += 3
    if status_website == "Hanya sosial media":
        score += 2
    if lead.get("kontak") or lead.get("email"):
        score += 2
    if category in LANDING_PAGE_FRIENDLY_CATEGORIES:
        score += 1
    if lead.get("instagram"):
        score += 1
    if any(keyword in note for keyword in ("aktif", "posting", "promosi", "update", "pesanan", "kelas baru")):
        score += 1

    return max(1, min(score, 10))


def enrich_lead(raw_lead: Lead, city: str, category: str) -> Lead:
    lead = {
        "tanggal": datetime.now().date().isoformat(),
        "nama_bisnis": raw_lead.get("nama_bisnis", ""),
        "kategori": raw_lead.get("kategori") or normalize_category(category),
        "kota": raw_lead.get("kota") or city,
        "kontak": raw_lead.get("kontak", ""),
        "email": raw_lead.get("email", ""),
        "instagram": raw_lead.get("instagram", ""),
        "website": raw_lead.get("website", ""),
        "sumber": raw_lead.get("sumber", "sample"),
        "catatan": raw_lead.get("catatan", ""),
        "status": "draft",
    }
    lead["status_website"] = get_website_status(lead["website"])
    lead["skor_peluang"] = calculate_score(lead)
    return ensure_contact_and_maps(lead)


def search_businesses(
    city: str,
    category: str,
    limit: int = 10,
    radius_km: int | None = None,
    latitude: float | None = None,
    longitude: float | None = None,
) -> list[Lead]:
    """MVP data source. Replace this function with an official API or CSV importer later."""
    city_lower = city.lower()
    category_lower = normalize_category(category)
    logger.info(
        "Search source=sample city=%s category=%s radius_km=%s lat=%s lng=%s",
        city,
        category,
        radius_km,
        latitude,
        longitude,
    )
    matches = [
        enrich_lead(item, city, category)
        for item in SAMPLE_BUSINESSES
        if item.get("kota", "").lower() == city_lower
        and normalize_category(str(item.get("kategori", ""))) == category_lower
    ]

    if not matches:
        logger.info("Tidak ada sample spesifik untuk %s di %s", category, city)

    return matches[:limit]
