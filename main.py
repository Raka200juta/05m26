import json
import os

nama_file = "data_keuangan.json"

if os.path.exists(nama_file):
    with open(nama_file, "r") as file:
        database_transaksi = json.load(file)
else:
    database_transaksi = []

while True:
    print("\n=== Sistem Pengelola Uang [Raka] ===")
    print("1. Catat Pemasukan")
    print("2. Catat Pengeluaran")
    print("3. Lihat Riwayat & Laporan")
    print("4. Keluar")

    pilihan = input("Pilih opsi (1-4): ")

    if pilihan == '1' or pilihan == '2':
        nama = input("Masukkan nama transaksi: ")
        input_uang = input("Masukkan jumlah uang: ")
        jumlah = int(input_uang.replace(".", "").replace(",", ""))
        kategori = "Masuk" if pilihan == '1' else "Keluar"

        data = {
            "nama": nama,
            "jumlah": jumlah,
            "kategori": kategori
        }

        database_transaksi.append(data)

        with open(nama_file, "w") as file:
            json.dump(database_transaksi, file, indent=4)

        print(f"Data {kategori} berhasil disimpan!")

    elif pilihan == '3':
        print("\n=== Riwayat Transaksi ===")
        total_masuk = 0
        total_keluar = 0

        if not database_transaksi:
            print("Belum ada data tersimpan.")
        else:
            for transaksi in database_transaksi:
                print(f"[{transaksi['kategori']}] {transaksi['nama']}: Rp{transaksi['jumlah']}")

                if transaksi['kategori'] == "Masuk":
                    total_masuk += transaksi['jumlah']
                else:
                    total_keluar += transaksi['jumlah']

            saldo_akhir = total_masuk - total_keluar
            print("-" * 30)
            print(f"Total Masuk   : Rp{total_masuk}")
            print(f"Total Keluar  : Rp{total_keluar}")
            print(f"Saldo Akhir   : Rp{saldo_akhir}")

    elif pilihan == '4':
        print("Data tersimpan aman. Sampai jumpa!")
        break
    else:
        print("Pilihan tidak valid!")