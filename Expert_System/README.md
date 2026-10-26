# Tugas Sistem Pakar : Diagnosa Gangguan Motor Induksi 3 Fasa Menggunakan Forward Chaining (Decision Tree)

## Introduction
Program ini merupakan asisten inspeksi kelistrikan dan mekanis untuk Motor Induksi 3 Fasa berbasis terminal. Berbeda dengan sistem pencarian kata kunci (NLP bebas), program ini menggunakan metode **Forward Chaining interaktif**.

Sistem bertindak layaknya seorang inspektur *maintenance* (pemeliharaan) yang menuntun teknisi lapangan melalui serangkaian observasi dengan pertanyaan Ya/Tidak. Berdasarkan jawaban teknisi, sistem akan mengerucutkan kemungkinan masalah (Triase) hingga menemukan titik kerusakan dan memberikan rekomendasi tindakan perbaikan.

## Arsitektur & Aturan Sistem Pakar (State Machine)
Sistem tidak menggunakan aturan `if-elif-else` linier, melainkan memodelkan *Knowledge Base* ke dalam struktur **Graph/Tree** (Pohon Keputusan). Setiap titik (Node) memiliki pertanyaan spesifik yang menentukan cabang berikutnya:

| Node Observasi | Jika "Ya" (y) Lanjut Ke | Jika "Tidak" (n) Lanjut Ke |
|---|---|---|
| **start** (Gagal start?) | `cek_suara` | `cek_panas` |
| **cek_suara** (Mendengung keras?) | Solusi: *Single Phasing* | `cek_power` |
| **cek_power** (Tegangan panel masuk?)| Solusi: *Locked Rotor* | Solusi: *No Power* |
| **cek_panas** (Bodi sangat panas?) | `cek_beban` | `cek_getaran` |
| **cek_beban** (Arus lebihi nameplate?)| Solusi: *Overload* | Solusi: *Bad Ventilation* |
| **cek_getaran** (Getaran bising?) | Solusi: *Bearing / Misalignment*| Solusi: *Normal* |

Siklus diagnosa akan terus berjalan berpindah dari satu *node* ke *node* lain hingga mencapai hasil yang berawalan `SOLUSI_`.

## Requirement & Library
**Kebutuhan Perangkat Lunak:**
- Python 3.10 atau lebih baru.
- Terminal, Command Prompt, atau PowerShell.
- Git (opsional, untuk mengunduh repositori melalui terminal).

**Library:**
Proyek ini sepenuhnya menggunakan pustaka bawaan Python (Standard Library) berupa `dictionary` dan `loop` dasar. Tidak ada library eksternal yang dibutuhkan sehingga Anda tidak perlu menjalankan `pip install`.

## How to Run

1. **Clone atau Download Repositori**
   Buka terminal di komputer Anda, lalu jalankan perintah berikut:
   ```bash
   git clone [https://github.com/USERNAME/NAMA_REPOSITORI.git](https://github.com/USERNAME/NAMA_REPOSITORI.git)
   cd NAMA_REPOSITORI
   ```
   *(Ganti `USERNAME` dan `NAMA_REPOSITORI` dengan link GitHub asli Anda. Alternatif lain: download ZIP, ekstrak, lalu buka foldernya di VS Code).*

2. **Buka Terminal**
   Jika menggunakan VS Code, pilih menu **Terminal** &rarr; **New Terminal**. Pastikan posisi folder sudah benar berada di tempat file kode tersimpan.

3. **Jalankan Program**
   Ketik perintah berikut untuk menjalankan sistem pakar:
   ```bash
   python main.py
   ```
   *(Untuk pengguna macOS/Linux, gunakan perintah `python3 main.py`)*

4. **Gunakan Program**
   - Baca pertanyaan observasi yang muncul di layar.
   - Ketik `y` untuk Ya, atau `n` untuk Tidak, lalu tekan Enter.
   - Sistem akan terus bertanya hingga diagnosa kerusakan ditemukan.

## Running & Output

**Contoh 1: Diagnosa Single Phasing (Kehilangan 1 Fasa)**
```text
==================================================
SISTEM PAKAR DIAGNOSA MOTOR INDUKSI 3 FASA
Jawablah dengan 'y' (Ya) atau 'n' (Tidak)
==================================================

[?] Apakah motor gagal start (tidak mau berputar sama sekali)? (y/n): y

[?] Apakah terdengar suara mendengung (humming) keras dari motor? (y/n): y

==================================================
KESIMPULAN & REKOMENDASI TINDAKAN
==================================================
DIAGNOSA: Single Phasing (Kehilangan 1 Fasa).
TINDAKAN: Segera matikan motor! Cek fuse, kontaktor, atau jalur kabel fasa R, S, T. Jika dibiarkan, belitan stator akan terbakar.
==================================================
```

**Contoh 2: Diagnosa Overload (Kelebihan Beban)**
```text
==================================================
SISTEM PAKAR DIAGNOSA MOTOR INDUKSI 3 FASA
Jawablah dengan 'y' (Ya) atau 'n' (Tidak)
==================================================

[?] Apakah motor gagal start (tidak mau berputar sama sekali)? (y/n): n

[?] Apakah bodi motor terasa sangat panas (overheating) saat beroperasi? (y/n): y

[?] Apakah arus (Ampere) yang terukur melebihi nameplate motor? (y/n): y

==================================================
KESIMPULAN & REKOMENDASI TINDAKAN
==================================================
DIAGNOSA: Kelebihan Beban (Overload).
TINDAKAN: Kurangi beban mekanis pada motor atau cek setting thermal overload relay (TOR).
==================================================
```

## Penjelasan Hasil
1. **Pada Contoh 1:** Program memulai dari pertanyaan dasar (apakah motor berputar). Karena teknisi menjawab `y` (gagal start), sistem berpindah ke cabang pengecekan suara. Jawaban `y` pada suara mendengung (ciri khas hilangnya salah satu fasa induksi) membuat sistem langsung menyimpulkan masalah sebagai **Single Phasing** tanpa perlu mengecek suhu atau getaran.
2. **Pada Contoh 2:** Teknisi menjawab `n` pada gagal start (artinya motor berputar). Sistem membuang semua kemungkinan kerusakan kelistrikan awal dan berpindah memeriksa anomali saat beroperasi (panas). Karena bodi panas (`y`) dan arus melebihi standar (`y`), sistem menggunakan logika deduksi bahwa motor sedang menarik daya paksa karena **Overload**.

## Keterbatasan
- **Subjektivitas Observasi:** Tingkat kebisingan atau suhu panas seringkali bersifat subjektif di lapangan jika teknisi tidak menggunakan alat ukur presisi (seperti *thermal gun* atau *vibration meter*).
- **Keputusan Tunggal:** Sistem saat ini hanya mendiagnosa satu masalah utama (Root Cause). Di lapangan, motor bisa saja mengalami komplikasi (misal: Overload yang menyebabkan Bearing rusak).
- **Manual Input:** Belum terintegrasi dengan sensor IoT industri (seperti ACS712 untuk arus) sehingga semua data harus diinput manual.

## Kesimpulan
Program ini menunjukkan bagaimana *Knowledge Base* seorang ahli kelistrikan industri dapat direpresentasikan dalam bentuk kode Python sederhana menggunakan struktur data *Graph/Decision Tree*. Pendekatan sistem pakar berbasis observasi Ya/Tidak ini terbukti lebih terarah dan meminimalkan kesalahan input (typo) dibandingkan menggunakan NLP teks bebas untuk masalah teknis perangkat keras.
