from abc import ABC, abstractmethod

# Kelas abstrak (Abstraction)
class Animal(ABC):
    def __init__(self, nama, umur):
        self.__nama = None
        self.__umur = None
        self.set_nama(nama)
        self.set_umur(umur)

    def get_nama(self):
        return self.__nama

    def set_nama(self, nama):
        if nama == "":
            raise ValueError("Nama tidak boleh kosong.")
        self.__nama = nama

    def get_umur(self):
        return self.__umur

    def set_umur(self, umur):
        if type(umur) != int or umur < 0:
            raise ValueError("Umur harus angka positif.")
        self.__umur = umur

    @abstractmethod
    def make_sound(self):
        pass

# Kelas turunannya (Inheritance + Polymorphism)
class Anjing(Animal):
    def make_sound(self):
        return "Guk Guk!"

class Kucing(Animal):
    def make_sound(self):
        return "Meooong!"

class Burung(Animal):
    def make_sound(self):
        return "Cuit Cuit!"

def main():
    daftar_hewan = []

    print("=== Program Data Hewan ===")
    while True:
        try:
            pilih = input("\nMau tambah hewan? (y/n): ").lower()
            if pilih != 'y':
                break

            jenis = input("Masukkan jenis hewan (anjing/kucing/burung): ").lower()
            nama = input("Masukkan nama hewan: ")
            umur = int(input("Masukkan umur hewan: "))

            if jenis == 'anjing':
                hewan = Anjing(nama, umur)
            elif jenis == 'kucing':
                hewan = Kucing(nama, umur)
            elif jenis == 'burung':
                hewan = Burung(nama, umur)
            else:
                print("Jenis hewan tidak ada.")
                continue

            daftar_hewan.append(hewan)
            print(f"Hewan {hewan.get_nama()} berhasil ditambahkan!")

        except ValueError as e:
            print("Error:", e)
        except Exception as e:
            print("Error lain:", e)

    print("\n=== Daftar Semua Hewan ===")
    for h in daftar_hewan:
        print(f"{h.get_nama()} ({h.get_umur()} tahun) bersuara: {h.make_sound()}")

if __name__ == "__main__":
    main()
