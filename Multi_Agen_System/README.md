# Multi-Agent System (MAS) : Simulasi Manajemen Pengiriman Logistik

## Introduction
Program ini adalah simulasi **Multi-Agent System (MAS)** berbasis terminal (CLI) yang memodelkan sistem alokasi pengiriman barang (logistik). 

Dalam arsitektur MAS, penyelesaian masalah tidak dilakukan oleh satu program monolitik yang panjang, melainkan didelegasikan kepada beberapa "Agen" (entitas cerdas/otonom) yang memiliki tugas spesifik. Para agen ini saling berkomunikasi, bertukar data, dan bekerja sama untuk mendistribusikan pesanan secara efisien berdasarkan jarak terdekat dan kapasitas muatan.

## Arsitektur & Peran Agen (Agent Roles)
Sistem ini menggunakan arsitektur OOP (*Object-Oriented Programming*) di mana seluruh agen mewarisi kelas dasar `Agent`. Terdapat tiga jenis agen utama:

1. **Coordinator Agent (Dispatcher):**
   Bertindak sebagai pusat komando. Menerima pesanan masuk, menyortir kurir mana yang kapasitasnya masih tersedia, dan secara cerdas menghitung jarak *Euclidean* (jarak garis lurus) antara posisi kurir saat ini dengan koordinat tujuan. Kurir terdekat akan dipilih secara otomatis.
2. **Delivery Agent (Kurir):**
   Agen fisik yang bergerak di dalam grid koordinat (X, Y). Memiliki muatan maksimal (*capacity*). Setiap kali menyelesaikan pesanan, agen ini akan berpindah koordinat (koordinatnya diperbarui ke lokasi pesanan) dan kapasitas muatannya berkurang.
3. **Monitoring Agent (Auditor):**
   Agen pengawas yang menerima komunikasi dari *Coordinator* setiap kali pengiriman sukses. Agen ini merekam riwayat (*history*) transaksi dan bertugas mencetak laporan akhir.

## Requirement & Library
**Kebutuhan Perangkat Lunak:**
- Python 3.10 atau lebih baru.
- Terminal, Command Prompt, atau PowerShell.

**Library:**
Proyek ini sepenuhnya menggunakan pustaka bawaan Python, khususnya library `math` untuk melakukan kalkulasi matematis (akar kuadrat) pada perhitungan jarak Euclidean. Tidak diperlukan instalasi library eksternal (tidak perlu `pip install`).

## How to Run

1. **Buka Terminal / VS Code**
   Pastikan Anda sudah berada di dalam direktori repositori (contoh: `AI-TE-1403/Multi_Agen_System`).
2. **Jalankan Program**
   Ketik perintah berikut pada terminal:
   ```bash
   python multi_agent_system.py
   ```
   *(Untuk pengguna macOS/Linux, gunakan perintah `python3 multi_agent_system.py`)*
3. Program akan berjalan secara otomatis tanpa memerlukan input manual, menampilkan proses delegasi agen, dan mencetak laporan akhir.

## Running & Output

```text
=== MULTI-AGENT DELIVERY SYSTEM ===

-------------------------
[Coordinator-1] Menerima pesanan P001
[Coordinator-1] Menugaskan Kurir-A
[Kurir-A] Mengirim pesanan P001
[Kurir-A] Pesanan P001 selesai.
[Monitor-1] Mencatat pesanan P001

-------------------------
[Coordinator-1] Menerima pesanan P002
[Coordinator-1] Menugaskan Kurir-C
[Kurir-C] Mengirim pesanan P002
[Kurir-C] Pesanan P002 selesai.
[Monitor-1] Mencatat pesanan P002

-------------------------
[Coordinator-1] Menerima pesanan P003
[Coordinator-1] Menugaskan Kurir-B
[Kurir-B] Mengirim pesanan P003
[Kurir-B] Pesanan P003 selesai.
[Monitor-1] Mencatat pesanan P003

-------------------------
[Coordinator-1] Menerima pesanan P004
[Coordinator-1] Menugaskan Kurir-C
[Kurir-C] Mengirim pesanan P004
[Kurir-C] Pesanan P004 selesai.
[Monitor-1] Mencatat pesanan P004

-------------------------
[Coordinator-1] Menerima pesanan P005
[Coordinator-1] Menugaskan Kurir-A
[Kurir-A] Mengirim pesanan P005
[Kurir-A] Pesanan P005 selesai.
[Monitor-1] Mencatat pesanan P005

=== LAPORAN PENGIRIMAN ===
Pesanan P001 dikirim oleh Kurir-A
Pesanan P002 dikirim oleh Kurir-C
Pesanan P003 dikirim oleh Kurir-B
Pesanan P004 dikirim oleh Kurir-C
Pesanan P005 dikirim oleh Kurir-A
Total selesai: 5

=== STATUS AKHIR AGENT ===
Kurir-A | Posisi: (1, 1) | Sisa kapasitas: 0 | Selesai: 2
Kurir-B | Posisi: (4, 4) | Sisa kapasitas: 1 | Selesai: 1
Kurir-C | Posisi: (9, 10) | Sisa kapasitas: 0 | Selesai: 2
```

## Penjelasan Hasil Kalkulasi Sistem
Sistem berjalan sangat dinamis berkat kalkulasi *CoordinatorAgent*. Sebagai contoh:
1. **Delegasi P001 (Tujuan 2,3):** Koordinator menghitung jarak, dan menemukan `Kurir-A` (berada di titik 0,0) adalah yang terdekat. Kurir-A dieksekusi dan posisinya sekarang berpindah ke (2,3).
2. **Delegasi P004 (Tujuan 9,10):** Koordinator menugaskan `Kurir-C` karena posisinya saat itu berada di (8,9)—efek dari pengiriman pesanan P002 sebelumnya. Jaraknya sangat dekat.
3. Setelah menyelesaikan P004, `Kurir-C` kehabisan kapasitas (sisa 0), sehingga sistem otomatis mengecualikan `Kurir-C` saat melakukan pencarian agen untuk pesanan berikutnya (P005). 

## Kesimpulan
Simulasi ini berhasil mendemonstrasikan konsep dasar sistem cerdas logistik modern (seperti yang digunakan pada algoritma layanan ojek *online* atau manajemen armada paket). Penggunaan agen otonom memungkinkan penyelesaian beban kerja didistribusikan secara *real-time* menyesuaikan pergerakan koordinat masing-masing agen.
