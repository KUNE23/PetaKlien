# PetaKlien – UI/UX Planning Document



## 1. Pendahuluan

- **Nama Proyek:** PetaKlien  

- **Visi:** Membantu freelancer, web studio, dan agency menemukan UMKM yang belum memiliki website secara otomatis, sehingga fokus bisa dialokasikan pada penawaran layanan pembuatan website.  

- **Tujuan Utama:**  

  1. Mengumpulkan lead bisnis lokal tanpa website menggunakan data Google Maps.  

  2. Menyediakan dashboard untuk filter, skor, dan pengelolaan status lead.  

  3. Meng-export data ke CSV atau Google Sheets untuk follow

- **Scope MVP (Minimum Viable Product):**  

  - Halaman landing dengan penjelasan singkat.  

  - Form input: kota, kategori bisnis, radius pencarian.  

  - Tombol “Cari Leads” yang memanggil backend Flask.  

  - Menampilkan hasil dalam tabel dengan kolom: nama bisnis, kota, kategori, status website, skor peluang, kontak, link Google Maps.  

  - Fitur export CSV.  

  - Tampilan responsif (desktop-first, later mobile

- **Platform:** Web (Vue 3 + Vite) di frontend, Flask API di backend, dapat diakses di desktop Windows maupun Linux (Kali).



## 2. Persona & Pengguna

| Nama | Usia | Pekerjaan | Goal | Pain Points |

|------|------|-----------|------|-------------|

| **Raka** | 28 | Freelance Web Developer | Mendapatkan 20–30 lead per hari untuk ditawarkan layanan website. | Membuka 10+ tab Chrome manual, RAM terpakai ~4 GB, proses pencarian berulang dan memakan waktu. |

| **Dewi** | 32 | Pemilik Web Studio (UKM) | Meningkatkan konversi proposal melalui lead yang tervalidasi. | Tidak ada sistem scoring, leads terasa sama-sama, follow

| **Bagus** | 24 | Mahasiswa Teknik Informatika (magang) | Belajar proses pencarian lead dan membuat portfolio. | Kurangnya dokumentasi serta contoh UI yang baik untuk referensi belajar. |



## 3. Goal & Pain Points

- **Goal:** Mengurangi waktu pencarian lead dari jam/menit menjadi beberapa klik, menyediakan informasi yang terstruktur (nama, kontak, skor, link maps) untuk ambil keputusan cepat.

- **Pain Points:**  

  1. Proses manual melalui Google Maps satu per satu sangat memakan waktu dan tidak efisien.  

  2. Tidak ada mekanisme untuk memprioritaskan lead berdasarkan peluang (website tidak ada, skor, dll.).  

  3. Hasil pencarian tersebar di banyak tab, sulit untuk dieksport atau dibagikan dengan tim.  

  4. Tidak ada standar visual yang konsisten sehingga tampilan terasa amateur.



## 4. User Journey (Alur Pengguna)

1. **Buka Aplikasi** – landing page dengan penjelasan singkat dan tombol “Mulai”.  

2. **Pilih Parameter** – isi kotak kota, pilih kategori bisnis (dropdown multiselect), set radius (km).  

3. **Tekan “Cari Leads”** – sistem memanggil API backend, menampilkan loading spinner.  

4. **Hasil Pencarian** – tabel menampilkan lead dengan kolom: nama, kota, kategori, status website, skor, kontak, link Maps.  

5. **Filter & Sort** – pengguna dapat filter berdasarkan status website (Belum ada/Hanya sosial media/Sudah ada), sort skor naik/menurun.  

6. **Detail Lead (opsional)** – klik bar untuk menampilkan modal dengan informasi lengkap dan tombol “Salin Kontak”.  

7. **Export** – pilih format (CSV atau Google Sheets), tekan “Export”, unduh file atau buka spreadsheet.  

8. **Follow



## 5. Information Architecture (IA)

- **Halaman Utama (Landing)** → penjelasan + CTA ke Dashboard.  

- **Dashboard** → filter form + tabel hasil + tombol export.  

- **Modal Detail Lead** → informasi lengkap + aksi (salIN kontak, buka Maps).  

- **Footer** → hak cipta, link ke dokumentasi.  

- **Navigasi:** Tidak ada navigasi halaman kompleks karena single



## 6. Design System & Style Guide (Ringkasan)

| Elemen | Spesifikasi |

|--------|-------------|

| **Palet Warna** | Primary: `#1E88E5` (biru)<br>Secondary: `#F5F7FA` (abu

| **Tipografi** | Font Utama: **Inter** (Google Font).<br>Ukuran Base: 16 px.<br>Heading: H1 24 px (bold), H2 20 px (semibold), H3 18 px (medium).<br>Line Height: 1.5 untuk teksParagraph, 1.2 untuk heading. |

| **Iconography** | Set ikon: **Feather Icons** (stroke

| **Komponen** | Button (primary, accent, outline), Input (text, select, checkbox), Card, Table, Modal, Toast/Snackbar, Loading Spinner, Pagination. Semua komponen menggunakan kelas Tailwind yang dapat di

| **Spacing & Grid** | Base unit: 4 px. Margin/padding menggunakan kelipatan 4 (p

| **Aksesibilitas** | Kontras warna minimal 4.5:1 untuk teks, 3:1 untuk elemen non



## 7. Wireframe / Mockup (Deskripsi Singkat)

- **Landing Page:** Hero dengan ilustrasi peta + pin, judul “PetaKlien”, subjudul “Temukan UMKM tanpa website dalam hitungan detik”, tombol primer “Mulai”.  

- **Dashboard:** Sidebar kiri berisi form input (kota, kategori, radius) dan tombol “Cari Leads”. Area utama menampilkan statistik kartu (total, hari ini, draft, approved, no

- **Modal Detail:** Menampilkan nama bisnis besar, alamat, telepon, website (jika ada), skor, serta tombol “Salin Kontak” dan “Buka Google Maps”.  

- **Toast:** Muncul di pojok kanan bawah setelah export berhasil atau terjadi error.



## 8. Rencana Implementasi (Milestones)

| Sprint | Tanggal | Fokus | Deliverable |

|--------|---------|-------|-------------|

| Sprint 1 | 12

| Sprint 2 | 01

| Sprint 3 | 06

| Sprint 4 | 11

| Sprint 5 | 16

| Sprint 6 | 21 Jun 2026 | **Checkpoint 50 %** | Demo MVP kepada tim, dokumentasi progres, umpan balik. |

| Sprint 7 | 22

| Sprint 8 | 01

| Sprint 9 | Akhir Jul 2026 | Grand Closing | Pengumuman pemenang, laporan akhir. |



## 9. Kriteria Kesuksesan (KPI)

- **Waktu Pencarian:** rata

- **Keakuratan Data:** minimal 90 % lead yang ditampilkan memiliki status website yang sesuai (validasi manual pada sampel).  

- **Penggunaan:** ≥ 80 % pengguna mampu menyelesaikan alur “Cari → Filter → Export” tanpa bantuan.  

- **Aksesibilitas:** Lulus audit axe

- **Kepuasan:** NPS (Net Promoter Score) ≥ 30 setelah demo akhir.



## 10. Catatan Tambahan

- **Environment Variables:** Disimpan di `.env` (tidak di

- **Version Control:** Gunakan branch `dev` untuk pekerjaan harian, pull request ke `main` setelah review.  

- **CI/CD (opsional):** GitHub Actions untuk lint (ESLint, Prettier) dan menjalankan unit test pada setiap push.  

- **Dokumentasi API:** gunakan Swagger/OpenAPI di `docs/api.yaml` untukReferensi tim frontend.



---

*Dokumen ini dibuat sebagai acuan untuk tim pengembangan PetaKlien dan dapat diperbarui sejalan dengan progres proyek.*  