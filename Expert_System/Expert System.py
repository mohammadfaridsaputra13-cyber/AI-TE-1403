# ==========================================
# SISTEM PAKAR: DIAGNOSA MOTOR INDUKSI 3 FASA
# Metode: Forward Chaining (Decision Tree)
# ==========================================

# Basis Pengetahuan (Knowledge Base) dimodelkan sebagai Node dalam Graf
# Setiap node memiliki 'pertanyaan' dan cabang tujuan 'y' (ya) atau 'n' (tidak)
# Jika nilai 'y' atau 'n' berawalan 'SOLUSI_', maka itu adalah hasil akhir.

knowledge_base = {
    'start': {
        'pertanyaan': "Apakah motor gagal start (tidak mau berputar sama sekali)?",
        'y': 'cek_suara',
        'n': 'cek_panas'
    },
    'cek_suara': {
        'pertanyaan': "Apakah terdengar suara mendengung (humming) keras dari motor?",
        'y': 'SOLUSI_SINGLE_PHASING',
        'n': 'cek_power'
    },
    'cek_power': {
        'pertanyaan': "Apakah tegangan suplai pada panel terukur masuk (MCB/Kontaktor aktif)?",
        'y': 'SOLUSI_ROTOR_LOCKED',
        'n': 'SOLUSI_NO_POWER'
    },
    'cek_panas': {
        'pertanyaan': "Apakah bodi motor terasa sangat panas (overheating) saat beroperasi?",
        'y': 'cek_beban',
        'n': 'cek_getaran'
    },
    'cek_beban': {
        'pertanyaan': "Apakah arus (Ampere) yang terukur melebihi nameplate motor?",
        'y': 'SOLUSI_OVERLOAD',
        'n': 'SOLUSI_VENTILASI'
    },
    'cek_getaran': {
        'pertanyaan': "Apakah terjadi getaran mekanis (vibrasi) yang tidak wajar / bising?",
        'y': 'SOLUSI_BEARING',
        'n': 'SOLUSI_NORMAL'
    }
}

# Daftar Solusi Akhir
solusi_db = {
    'SOLUSI_SINGLE_PHASING': "DIAGNOSA: Single Phasing (Kehilangan 1 Fasa).\nTINDAKAN: Segera matikan motor! Cek fuse, kontaktor, atau jalur kabel fasa R, S, T. Jika dibiarkan, belitan stator akan terbakar.",
    'SOLUSI_ROTOR_LOCKED': "DIAGNOSA: Rotor Terkunci (Locked Rotor) atau Masalah Mekanis Beban.\nTINDAKAN: Cek apakah beban mekanis macet (gearbox/pompa). Putar as motor secara manual dalam kondisi mati.",
    'SOLUSI_NO_POWER': "DIAGNOSA: Suplai Daya Terputus.\nTINDAKAN: Periksa sumber listrik utama, MCB trip, atau rangkaian kontrol (push button/relay) yang tidak terhubung.",
    'SOLUSI_OVERLOAD': "DIAGNOSA: Kelebihan Beban (Overload).\nTINDAKAN: Kurangi beban mekanis pada motor atau cek setting thermal overload relay (TOR).",
    'SOLUSI_VENTILASI': "DIAGNOSA: Pendinginan Buruk.\nTINDAKAN: Cek kipas pendingin (cooling fan) di belakang motor, bersihkan sirip bodi motor dari kotoran.",
    'SOLUSI_BEARING': "DIAGNOSA: Kerusakan Bearing / Misalignment.\nTINDAKAN: Lumasi bearing atau ganti bearing baru. Lakukan alignment ulang antara poros motor dan beban.",
    'SOLUSI_NORMAL': "DIAGNOSA: Motor beroperasi dalam batas normal.\nTINDAKAN: Lakukan perawatan preventif (preventive maintenance) rutin."
}

def jalankan_diagnosa():
    print("="*50)
    print("SISTEM PAKAR DIAGNOSA MOTOR INDUKSI 3 FASA")
    print("Jawablah dengan 'y' (Ya) atau 'n' (Tidak)")
    print("="*50)
    
    current_node = 'start' # Titik awal diagnosa
    
    # Looping selama current_node belum berupa solusi (tidak berawalan 'SOLUSI_')
    while not current_node.startswith('SOLUSI_'):
        node_data = knowledge_base[current_node]
        
        while True:
            jawaban = input(f"\n[?] {node_data['pertanyaan']} (y/n): ").strip().lower()
            if jawaban in ['y', 'n']:
                break
            print("Input tidak valid. Harap masukkan 'y' atau 'n'.")
            
        # Pindah ke node selanjutnya berdasarkan jawaban pengguna
        current_node = node_data[jawaban]
        
    # Menampilkan hasil akhir
    print("\n" + "="*50)
    print("KESIMPULAN & REKOMENDASI TINDAKAN")
    print("="*50)
    print(solusi_db[current_node])
    print("="*50)

if __name__ == "__main__":
    jalankan_diagnosa()