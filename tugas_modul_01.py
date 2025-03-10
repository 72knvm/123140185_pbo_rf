import json
import sys

class DataMahasiswa:
    def __init__(self):
        self.mahasiswa = {}
        
    def simpan(self, filename):
        with open(filename, "w") as file:
            file.write("mahasiswa = " + json.dumps(self.mahasiswa, indent=4))

    def muatan(self, filename):
        try:
            with open(filename, "r") as file:
                content = file.read()
                if content.startswith("mahasiswa = "):
                    self.mahasiswa = json.loads(content[len("mahasiswa = "):])
        except (FileNotFoundError, json.JSONDecodeError):
            self.mahasiswa = {}
        
    def tambah(self):
        while True:
            nim = input("Masukkan NIM: ")
            if nim.isdigit():
                break
            print("Error!! NIM harus berupa angka!")
        
        if nim in self.mahasiswa:
            print(f"NIM {nim} Sudah Terdaftar!")
            return
        nama = input("Masukkan Nama: ")
        nilai = input("Masukkan Nilai: ")
        self.mahasiswa[nim] = {"nama" : nama, "nilai" : int(nilai)}
        print("Okeh!")
                  
    def hapus(self):
        nim = input("Masukkan NIM yang mau dihapus: ")
        if nim in self.mahasiswa:
            del self.mahasiswa[nim]
            print("Berhasil Dihapus!")
        else:
            print("NIM Tidak Ketemu!")

    def tampilkan(self):
        if not self.mahasiswa:
            print("Tidak Ada!")
        else:
            print("\n==== DATA MAHASISWA ====")
            print("NIM      | Nama   | Nilai")
            print("-------------------------")

            urut = input("Urutkan berdasarkan (1: NIM, 2: Nilai tertinggi): ")
            
            if urut == "2":
                sudah_urut = sorted(self.mahasiswa.items(), key=lambda x: x[1]['nilai'], reverse=True)
            else:
                sudah_urut = sorted(self.mahasiswa.items())
            
            for nim, info in sudah_urut:
                print(f"{nim:<8} | {info['nama']:<5} | {info['nilai']}")

    def cari(self):
        nim = input("Masukkan NIM yang ingin dicari: ")
        if nim in self.mahasiswa:
            info = self.mahasiswa[nim]
            print("\nData Mahasiswa:")
            print(f"NIM: {nim}")
            print(f"Nama: {info['nama']}")
            print(f"Nilai: {info['nilai']}")
        else:
            print("Data Tidak Ditemukan!")

    def edit(self):
        nim = input("Masukkan NIM Yang Ingin Di Ganti: ")
        if nim in self.mahasiswa:
            nim_baru = input("Masukkan NIM Baru: ")
            nama = input("Masukkan Nama Baru: ")
            nilai = input("Masukkan Nilai Baru: ")
            if nim_baru and nim_baru != nim:
                self.mahasiswa[nim_baru] = self.mahasiswa.pop(nim)
                nim = nim_baru
            if nama:
                self.mahasiswa[nim]["nama"] = nama
            if nilai:
                self.mahasiswa[nim]["nilai"] = nilai
            print("Berhasil Di Ubah!")
        else:
            print("Data Tidak Ditemukan!")

if __name__ == "__main__":
    sistem = DataMahasiswa()
    
    while True:
        print("\n=== Data Mahasiswa ===")
        print("1. Tambah Mahasiswa")
        print("2. Hapus Mahasiswa")
        print("3. Cari Mahasiswa")
        print("4. Edit Mahasiswa")
        print("5. Tampilkan Mahasiswa")
        print("6. Simpan Data")
        print("7. Keluar")
        pilih = input("Pilih: ")

        if pilih == "1":
            sistem.tambah()
        elif pilih == "2":
            sistem.hapus()
        elif pilih == "3":
            sistem.cari()
        elif pilih == "4":
            sistem.edit()
        elif pilih == "5":
            sistem.tampilkan()
        elif pilih == "6":
            filename = input("Masukkan nama file penyimpanan: ")
            sistem.simpan(filename)
            print("Data berhasil disimpan!")
        elif pilih == "7":
            print("Terimakasih!")       
        else:
            print("Loh??? Ngapain Disini???")
