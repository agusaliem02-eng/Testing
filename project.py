# === Program Hitung Gaji Karyawan ===

def gaji_pokok(jabatan):
    """Mengembalikan gaji pokok berdasarkan jabatan"""
    if jabatan.lower() == "manager":
        return 10000000
    elif jabatan.lower() == "supervisor":
        return 8000000
    elif jabatan.lower() == "staf":
        return 5000000
    elif jabatan.lower() == "magang":
        return 3000000
    else:
        return 0

def hitung_tunjangan(gaji):
    """Tunjangan sebesar 20% dari gaji pokok"""
    return 0.2 * gaji

def hitung_potongan(gaji):
    """Potongan sebesar 5% dari gaji pokok"""
    return 0.05 * gaji

def hitung_total(gaji, tunjangan, potongan):
    """Menghitung total gaji bersih"""
    return gaji + tunjangan - potongan

def tampilkan_slip(nama, jabatan, gaji, tunjangan, potongan, total):
    """Menampilkan slip gaji"""
    print("\n===============================")
    print(f"Slip Gaji Karyawan")
    print("===============================")
    print(f"Nama Karyawan  : {nama}")
    print(f"Jabatan        : {jabatan}")
    print(f"Gaji Pokok     : Rp {gaji:,}")
    print(f"Tunjangan (20%): Rp {tunjangan:,}")
    print(f"Potongan (5%)  : Rp {potongan:,}")
    print("-------------------------------")
    print(f"Total Gaji Bersih : Rp {total:,}")
    print("===============================\n")

def main():
    """Program utama"""
    while True:
        print("=== Program Hitung Gaji Karyawan ===")
        nama = input("Masukkan nama karyawan: ")
        jabatan = input("Masukkan jabatan (Manager/Supervisor/Staf/Magang): ")

        gaji = gaji_pokok(jabatan)
        if gaji == 0:
            print("⚠️ Jabatan tidak dikenali. Silakan coba lagi.\n")
            continue

        tunjangan = hitung_tunjangan(gaji)
        potongan = hitung_potongan(gaji)
        total = hitung_total(gaji, tunjangan, potongan)

        tampilkan_slip(nama, jabatan, gaji, tunjangan, potongan, total)

        ulang = input("Hitung gaji karyawan lain? (y/n): ")
        if ulang.lower() != 'y':
            print("\nTerima kasih! Program selesai.")
            break

# Jalankan program
main()
