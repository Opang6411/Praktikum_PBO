class Hewan:
    nama_kebun_binatang = "Zoo Nusantara"
    total_hewan = 0
    status_kesehatan_valid = ["Sehat", "Sakit", "Karantina"]

    def __init__(self, id_hewan, nama_hewan, spesies):
        self.id_hewan = id_hewan
        self.nama_hewan = nama_hewan
        self.spesies = spesies
        self.__umur = 0
        Hewan.total_hewan += 1

    @property
    def umur(self):
        return self.__umur

    @umur.setter
    def umur(self, nilai):
        if not isinstance(nilai, int) or nilai < 0:
            raise ValueError("Umur hewan harus berupa angka dan tidak boleh negatif.")
        self.__umur = nilai

    def tampilkan_info(self):
        print(f"Hewan [{self.id_hewan}]: {self.nama_hewan} ({self.spesies}) - Umur: {self.umur} tahun")

    @classmethod
    def ubah_nama_zoo(cls, nama_baru):
        cls.nama_kebun_binatang = nama_baru
        print(f"[Update] Nama kebun binatang diubah menjadi: {cls.nama_kebun_binatang}")

    @staticmethod
    def cek_kategori_umur(umur_hewan):
        return "Anakan" if umur_hewan < 2 else "Dewasa"


class Kandang:
    total_kandang = 0
    tipe_habitat_valid = ["Darat", "Air", "Udara", "Amfibi"]
    kapasitas_maksimal_sistem = 20

    def __init__(self, id_kandang, tipe_habitat):
        self.id_kandang = id_kandang
        self.tipe_habitat = tipe_habitat
        self.daftar_hewan = []
        self.__kapasitas = 0
        Kandang.total_kandang += 1

    @property
    def kapasitas(self):
        return self.__kapasitas

    @kapasitas.setter
    def kapasitas(self, nilai):
        if nilai <= 0 or nilai > Kandang.kapasitas_maksimal_sistem:
            raise ValueError(f"Kapasitas kandang harus antara 1 - {Kandang.kapasitas_maksimal_sistem} ekor.")
        self.__kapasitas = nilai

    def masukkan_hewan(self, hewan):
        if len(self.daftar_hewan) < self.kapasitas:
            self.daftar_hewan.append(hewan)
            print(f"Berhasil: {hewan.nama_hewan} dimasukkan ke kandang {self.id_kandang}.")
        else:
            print(f"Gagal: Kandang {self.id_kandang} sudah penuh!")

    @classmethod
    def dari_string(cls, data_string):
        id_kandang, habitat = data_string.split("-")
        return cls(id_kandang, habitat)

    @staticmethod
    def validasi_format_id(id_kandang):
        return id_kandang.startswith("K")


class Petugas:
    total_petugas = 0
    daftar_shift = ["Pagi", "Siang", "Malam"]
    gaji_dasar = 3500000

    def __init__(self, id_petugas, nama):
        self.id_petugas = id_petugas
        self.nama = nama
        self.__jam_kerja = 0
        Petugas.total_petugas += 1

    @property
    def jam_kerja(self):
        return self.__jam_kerja

    @jam_kerja.setter
    def jam_kerja(self, jam):
        if jam < 0 or jam > 12:
            raise ValueError("Jam kerja per hari tidak valid (maksimal 12 jam).")
        self.__jam_kerja = jam

    def beri_makan(self, hewan, kandang):
        if hewan in kandang.daftar_hewan:
            print(f"[{self.nama}] memberi makan {hewan.nama_hewan} di kandang {kandang.id_kandang}.")
        else:
            print(f"Peringatan: {hewan.nama_hewan} tidak ditemukan di kandang {kandang.id_kandang}.")

    @classmethod
    def naikkan_gaji(cls, kenaikan):
        cls.gaji_dasar += kenaikan
        print(f"[Update] Gaji dasar seluruh petugas naik menjadi Rp{cls.gaji_dasar}")

    @staticmethod
    def cek_kelayakan_bonus(total_jam_kerja_sebulan):
        return total_jam_kerja_sebulan > 160

if __name__ == "__main__":
    
    singa = Hewan("H01", "Simba", "Mamalia")
    elang = Hewan("H02", "Garuda", "Aves")
    
    kandang_darat = Kandang("K01", "Darat")
    kandang_udara = Kandang.dari_string("K02-Udara")
    
    petugas1 = Petugas("P01", "Pak Joko")
    petugas2 = Petugas("P02", "Bu Siti")

    singa.umur = 4
    elang.umur = 2
    kandang_darat.kapasitas = 2
    kandang_udara.kapasitas = 5
    petugas1.jam_kerja = 8

    print("\n--- INFO HEWAN ---")
    singa.tampilkan_info()
    elang.tampilkan_info()

    print("\n--- INTERAKSI KANDANG & PETUGAS ---")
    kandang_darat.masukkan_hewan(singa)
    kandang_darat.masukkan_hewan(elang)

    petugas1.beri_makan(singa, kandang_darat)
    petugas2.beri_makan(elang, kandang_udara) 

    print("\n--- PENGUJIAN CLASS & STATIC METHOD ---")
    Hewan.ubah_nama_zoo("Kebun Binatang Nasional")
    Petugas.naikkan_gaji(500000)

    print(f"Apakah ID K01 valid? {Kandang.validasi_format_id('K01')}")
    print(f"Kategori umur Simba: {Hewan.cek_kategori_umur(singa.umur)}")

    print("\n--- PENGUJIAN VALIDASI (SETTER) ---")

    try:
        singa.umur = -2
    except ValueError as e:
        print(f"Validasi Umur Berhasil: {e}")

    try:
        kandang_darat.kapasitas = 50
    except ValueError as e:
        print(f"Validasi Kapasitas Berhasil: {e}")

    try:
        petugas1.jam_kerja = 15
    except ValueError as e:
        print(f"Validasi Jam Kerja Berhasil: {e}")