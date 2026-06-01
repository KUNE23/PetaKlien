# 📋 PetaKlien — Planning Document
**Versi:** 1.0  
**Tanggal:** 30 Mei 2026  
**Status:** Draft

---

## 📌 1. LATAR BELAKANG

Banyak programmer, web developer, dan digital freelancer di Indonesia yang memiliki keahlian teknis mumpuni, tetapi kesulitan mendapatkan klien secara konsisten. Persaingan di platform freelance seperti Sribulancer, Fastwork, atau Upwork semakin ketat, sementara pemasaran melalui media sosial membutuhkan waktu dan strategi yang tidak dimiliki semua developer.

Di sisi lain, masih sangat banyak **bisnis lokal di Indonesia yang belum memiliki website**. Berdasarkan data:

- Dari jutaan UMKM di Indonesia, baru sekitar **20-30% yang memiliki kehadiran digital** (website/resmi).
- Banyak bisnis lokal yang hanya memiliki akun Instagram, Facebook, atau Google Maps saja — tanpa website sendiri.
- Mereka adalah **calon klien potensial** yang sangat besar bagi para programmer.

Sayangnya, mencari bisnis-bisnis ini secara manual melalui Google Maps satu per satu sangat **memakan waktu, melelahkan, dan tidak efisien**.

**PetaKlien hadir untuk menjembatani kesenjangan ini.**

---

## 🔴 2. MASALAH

### 2.1. Dari Sisi Programmer / Freelancer

| Masalah | Dampak |
|---------|--------|
| **Sulit mencari klien** — tidak punya pipeline prospek yang jelas | Waktu menganggur antar proyek jadi panjang |
| **Pemasaran manual** — harus hunting satu per satu via Google Maps, catat manual | Menghabiskan 2-4 jam sehari hanya untuk mencari prospek |
| **Tidak ada sistem prioritas** — bingung klien mana yang harus dikejar duluan | Peluang bagus terlewat |
| **Tidak ada catatan terpusat** — data bisnis berserakan di notes, screenshots, chat | Sulit follow-up, data hilang |
| **Gagal follow-up** — lupa udah komunikasi sama siapa aja | Prospek dingin, closed deal hilang |

### 2.2. Dari Sisi Bisnis Lokal (Calon Klien)

| Masalah | Dampak |
|---------|--------|
| **Tidak tersentuh digital** — hanya mengandalkan medsos atau Google Maps | Kehilangan pelanggan yang mencari secara online |
| **Tidak sadar butuh website** — tidak ada yang menawarkan solusi | Potensi bisnis tidak maksimal |
| **Tidak tahu cara membuat website** — menganggap mahal/sulit | Tetak bertahan di zona nyaman tanpa website |

### 2.3. Akar Masalah

```
Programmer butuh klien ──┐
                          ├──> Tidak ada jembatan ──> Potensi hilang di kedua sisi
Bisnis butuh website  ───┘
```

**Tidak ada sistem otomatis yang:**
1. Menemukan bisnis lokal yang belum punya website
2. Mengumpulkan data kontak & info mereka
3. Menyortir berdasarkan prioritas (skor peluang)
4. Memudahkan follow-up terstruktur
5. Tersedia dalam satu dashboard / bot yang gampang dipakai

---

## 💡 3. IDE — PetaKlien

**PetaKlien** adalah platform / sistem otomatis yang mencari, mengumpulkan, dan menyortir **bisnis lokal yang belum memiliki website** — menggunakan data dari **Google Maps** — sehingga programmer dan web developer bisa langsung fokus pada follow-up, bukan manual searching.

### 3.1. Filosofi Nama

| Kata | Makna |
|------|-------|
| **Peta** | Google Maps — sumber data lokasi bisnis |
| **Klien** | Tujuan akhir: mendapatkan klien baru |

> **PetaKlien** = "Membaca peta untuk menemukan klien."

### 3.2. Konsep Utama

| Konsep | Deskripsi |
|--------|-----------|
| **Maps-Based Lead Generation** | Data bersumber dari Google Maps (nama bisnis, kategori, kontak, lokasi, status website) |
| **Scoring Otomatis** | Setiap lead diberi skor prioritas 1-10 berdasarkan potensi |
| **Approval Workflow** | Lead disimpan sebagai draft → di-review & di-approve manual → baru siap untuk follow-up |
| **Web-Based Workflow** | Dashboard Vue + Flask API + Supabase |
| **Tanpa Spam** | Sistem tidak mengirim proposal otomatis — etis, tidak spam |

### 3.3. Target Pengguna

1. **Freelance web developer / programmer** — yang butuh klien konsisten
2. **Agen digital marketing** — yang menawarkan jasa pembuatan website ke UMKM
3. **Startup kecil / studio web** — yang butuh pipeline prospek untuk tim sales
4. **Siapapun yang punya jasa digital** — dan ingin menawarkan ke bisnis lokal

---

## 🛠️ 4. SOLUSI

### 4.1. Arsitektur Sistem

```
                           ┌─────────────────┐
                           │   Google Maps    │
                           │  (Sumber Data)   │
                           └────────┬────────┘
                                    │
                                    ▼
                    ┌───────────────────────────────┐
                    │      Lead Finder Engine        │
                    │  - Cari bisnis per kategori    │
                    │  - Deteksi status website      │
                    │  - Skor peluang 1-10           │
                    └───────────────┬───────────────┘
                                    │
                    ┌───────────────┴───────────────┐
                    │        Data Storage            │
                    │  ┌──────────┐ ┌──────────────┐ │
                    │  │ Supabase │ │ Google Sheets │ │
                    │  │ (Primary)│ │ (Sync/Dashboard)│
                    │  └──────────┘ └──────────────┘ │
                    └───────────────┬───────────────┘
                                    │
           ┌────────────────────────┼────────────────────────┐
           │                        │                        │
           ▼                        ▼                        ▼
   ┌────────────────┐       ┌────────────────┐
   │   Vue Web UI    │       │ Google Sheets   │
   │ input lokasi    │       │ optional sync    │
   │ review pipeline │       │ reports/export   │
   └────────────────┘       └────────────────┘
```

### 4.2. Fitur Utama

#### ✅ Sudah Tersedia (MVP)

| Fitur | Fungsi |
|-------|--------|
| **Pencarian Lead Otomatis** | Mencari bisnis di kategori tertentu (restoran, cafe, laundry, dll) dari data sample / Maps |
| **Deteksi Status Website** | Kategorikan: Belum ada / Hanya sosial media / Punya website |
| **Scoring Peluang** | Skor 1-10 — mana yang paling potensial |
| **Supabase Database** | Simpan data, cegah duplikat, riwayat lead |
| **Google Sheets Sync** | Dashboard untuk lihat semua lead & laporan harian |
| **Vue Dashboard** | Input lokasi, radius, kategori, review lead, approve/skip/contacted/closed |
| **Laporan Prioritas** | 5 lead terbaik hari ini — kontak & Google Maps link |

#### 🚧 Rencana Pengembangan

| Fitur | Target |
|-------|--------|
| **Integrasi Google Maps API** (real data, bukan sample) | *Next phase* |
| **Google Places API** (real data berbasis radius) | *Next phase* |
| **Export CSV / PDF** (data lead siap kirim proposal) | *Next phase* |
| **Draft Proposal Generator** (generate draft otomatis per lead) | *Next phase* |
| **Mobile App** (minimal PWA) | *Future* |

### 4.3. Alur Kerja Pengguna

```
                           ALUR PENGGUNAAN PETAKLIEN
                                   ┌─────┐
                                   │Start│
                                   └──┬──┘
                                      ▼
                    ┌─────────────────────────────────┐
                    │ User input lokasi + radius       │
                    │ lalu klik Cari Bisnis            │
                    └────────────────┬────────────────┘
                                     ▼
                    ┌─────────────────────────────────┐
                    │ Lead tersimpan di Supabase       │
                    │ Status: DRAFT                    │
                    └────────────────┬────────────────┘
                                     ▼
           ┌──────────────────────────────────────────┐
           │  Dashboard menampilkan lead baru          │
           │  lengkap dengan skor dan kontak           │
           └────────────────┬─────────────────────────┘
                            ▼
           ┌──────────────────────────────────────────┐
           │  User review lead via dashboard:          │
           │  approve / skip / contacted / closed      │
           └────────────────┬─────────────────────────┘
                            ▼
           ┌──────────────────────────────────────────┐
           │  Lead APPROVED → siap follow-up          │
           │  Buka Google Maps link / kontak          │
           │  Kirim proposal penawaran (manual)       │
           └────────────────┬─────────────────────────┘
                            ▼
                    ┌─────────────────┐
                    │ Klien deal 🎉   │
                    │ Proyek baru!    │
                    └─────────────────┘
```

### 4.4. Tech Stack (Saat Ini)

| Komponen | Teknologi |
|----------|-----------|
| Backend | Python 3.12 + Flask API |
| Frontend | Vue 3 + Vite |
| Database | Supabase |
| Cloud Sync | Google Sheets API |
| Logging | Python logging + file handler |
| Konfigurasi | .env + python-dotenv |

### 4.5. Keunggulan PetaKlien

| Dibanding | Keunggulan PetaKlien |
|-----------|----------------------|
| **Manual search Maps** | ✅ Otomatis — hemat 2-4 jam/hari |
| **Freelance platform** | ✅ Tidak ada pesaing — kamu satu-satunya yang nawarin |
| **Scraper umum** | ✅ Skor prioritas, approval workflow, etis |
| **Catatan manual** | ✅ Database terpusat, terstruktur, tersinkronisasi |

---

## 📈 5. RENCANA KE DEPAN

### Short-term (1-2 bulan)
- ✅ MVP bot selesai
- ⬜ Integrasi Google Maps API (data real)
- ⬜ Web dashboard basic

### Mid-term (3-6 bulan)
- ⬜ Fitur draft proposal otomatis per lead
- ⬜ Multi-user support (tim sales)
- ⬜ Export laporan PDF (siap dikirim ke klien)

### Long-term (6-12 bulan)
- ⬜ Public landing page: **petaklien.com**
- ⬜ PWA / mobile app
- ⬜ Marketplace: programmer daftar → sistem cari lead → match

---

## ⚠️ 6. BATASAN ETIKA

PetaKlien berkomitmen:

1. ✅ **Tidak mengirim spam** — proposal tidak dikirim otomatis ke email/WA/DM
2. ✅ **Approval manual** — lead harus di-approve dulu sebelum follow-up
3. ✅ **Batasan harian** — `DAILY_LEAD_LIMIT` mencegah scraping berlebihan
4. ✅ **Data publik** — hanya menggunakan data yang sudah tersedia di Google Maps
5. ✅ **Transparansi** — jika ditanya, pengguna bisa menjelaskan sumber data

---

> **PetaKlien — Dari Peta ke Klien, Tanpa Manual Tanpa Capek.** 🗺️🎯
