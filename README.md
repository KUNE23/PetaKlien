# PetaKlien

PetaKlien adalah sistem pencari prospek bisnis lokal untuk programmer, freelancer, dan web developer yang ingin menemukan calon klien yang belum memiliki website. Sistem ini tetap anti-spam: aplikasi hanya mencari lead, membuat draft, dan mengelola status. Follow-up dilakukan manual.

## Stack

- Backend: Python 3.12 + Flask API
- Frontend: Vue 3 + Vite
- Database: Supabase
- Sync opsional: Google Sheets
- AI opsional: template proposal fallback jika API key kosong

Telegram bot dan scheduler sudah dihapus agar produk lebih fokus sebagai web app portfolio.

## Struktur Baru

```text
lead-finder-bot/
├── main.py
├── web_app.py
├── database.py
├── lead_finder.py
├── lead_utils.py
├── sheets.py
├── supabase_schema.sql
├── frontend/
│   ├── package.json
│   ├── vite.config.js
│   ├── index.html
│   └── src/
│       ├── App.vue
│       ├── main.js
│       └── styles.css
└── .env
```

## Environment

```env
GOOGLE_SERVICE_ACCOUNT_FILE=
GOOGLE_SHEET_ID=
GOOGLE_SHEET_TAB=Leads

SUPABASE_URL=
SUPABASE_SERVICE_ROLE_KEY=

AI_PROVIDER=
AI_API_KEY=

CITY=Jakarta
BUSINESS_CATEGORIES=restoran,cafe,laundry,barbershop,bengkel,toko,klinik kecil,UMKM,sekolah kecil
DAILY_LEAD_LIMIT=20

LOG_LEVEL=INFO
LOG_FILE=logs/lead-finder-bot.log
WEB_HOST=127.0.0.1
WEB_PORT=8000
GOOGLE_MAPS_BROWSER_API_KEY=
DEFAULT_SEARCH_RADIUS_KM=100
```

`GOOGLE_MAPS_BROWSER_API_KEY` dipakai hanya untuk map picker di browser. Pencarian real berbasis Google Places/Maps API masih fase berikutnya; saat ini engine masih memakai data sample lokal, tetapi parameter `city`, `latitude`, `longitude`, dan `radius_km` sudah diteruskan ke backend.

## Setup Supabase

1. Buat project di Supabase.
2. Buka SQL Editor.
3. Jalankan isi file `supabase_schema.sql`.
4. Isi `.env`:

```env
SUPABASE_URL=https://xxxx.supabase.co
SUPABASE_SERVICE_ROLE_KEY=service_role_key
```

Gunakan `service_role_key` hanya di backend, jangan ditaruh di frontend.

## Install Backend

```bash
cd ~/lead-finder-bot
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

Jalankan API:

```bash
python main.py web
```

API berjalan di:

```text
http://127.0.0.1:8000
```

## Install Frontend

```bash
cd ~/lead-finder-bot/frontend
npm install
npm run dev
```

Frontend berjalan di:

```text
http://127.0.0.1:5173
```

Vite sudah diproxy ke backend Flask untuk path `/api`.

## Build Frontend

```bash
cd ~/lead-finder-bot/frontend
npm run build
```

Setelah build, Flask bisa serve hasil `frontend/dist` langsung dari:

```text
http://127.0.0.1:8000
```

## Command Backend

```bash
python main.py web
python main.py find
python main.py test-sheets
```

## Alur UI

1. User membuka dashboard Vue.
2. User memilih metode input:
   - input manual kota/area
   - pilih titik dari Google Maps jika API key tersedia
3. User mengisi radius, misalnya 100 km.
4. User memilih kategori bisnis.
5. User klik `Cari Bisnis`.
6. Lead masuk ke Supabase dengan status `draft`.
7. User review lead, approve/skip/contacted/closed.

## Etika

- Tidak ada pengiriman proposal otomatis.
- Proposal hanya draft.
- Follow-up dilakukan manual.
- Lead harian tetap dibatasi oleh `DAILY_LEAD_LIMIT`.
