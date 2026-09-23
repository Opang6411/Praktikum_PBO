Sistem Manajemen Kebun Binatang (Zoo Management System)

Program Python ini adalah implementasi konsep Object-Oriented Programming (OOP) yang dirancang untuk memenuhi kriteria evaluasi praktikum pemrograman (Modul 1: Class & Object, Modul 2: Atribut & Method, Modul 3: Encapsulation & Property).
Deskripsi Program
Sistem ini menyimulasikan interaksi dasar dalam sebuah kebun binatang, mencakup pendataan hewan, pengelolaan kapasitas kandang, dan aktivitas petugas (seperti memberi makan hewan).

Struktur Class Utama
Program ini terdiri dari 3 class yang saling berinteraksi:
Hewan: Merepresentasikan data hewan di kebun binatang. Menyimpan ID, nama, spesies, dan umur
Kandang: Mengelola tempat tinggal hewan. Memiliki kapasitas maksimal dan list untuk menampung objek Hewan di dalamnya.
Petugas: Merepresentasikan pegawai kebun binatang yang memiliki jam kerja dan fungsi untuk berinteraksi dengan Hewan maupun Kandang.
Pemenuhan Kriteria Modul Praktikum

Modul 1: Class & Object
Class Standar: Terdapat 3 class utama (Hewan, Kandang, Petugas) yang independen namun saling berinteraksi (objek Hewan dimasukkan ke Kandang, lalu Petugas memberi makan objek Hewan di Kandang tersebut).
Instansiasi Objek: Pada main code (main), minimal 2 objek telah dibuat untuk masing-masing class.

Modul 2: Atribut & Method
Atribut Kelas: Terdapat minimal 3 atribut kelas yang dipakai bersama (contoh: Hewan.total_hewan, Kandang.tipe_habitat_valid, Petugas.gaji_dasar).
Atribut Instance: Diinisialisasi via init(). Mencakup atribut Public (seperti nama_hewan) dan atribut Private (seperti __umur, __kapasitas, __jam_kerja).
Instance Method: Method dengan parameter self untuk mengolah data spesifik objek (contoh: tampilkan_info(), masukkan_hewan(), beri_makan()).
Class Method (@classmethod): Menerima parameter cls. Digunakan untuk mengubah atribut kelas (ubah_nama_zoo()) dan sebagai Factory Method untuk membuat objek dari string (Kandang.dari_string()).
Static Method (@staticmethod): Method utilitas tanpa self atau cls (contoh: cek_kategori_umur(), validasi_format_id()).

Modul 3: Encapsulation & Property
Akses ke seluruh atribut Private dilindungi menggunakan decorator idiomatis Python (@property sebagai getter dan @nama.setter sebagai setter).
Validasi Setter: Setiap setter memiliki logika validasi menggunakan raise ValueError untuk mencegah masuknya data yang tidak logis (misalnya: umur hewan negatif, kapasitas kandang melebihi batas sistem, atau jam kerja petugas melebihi 12 jam).

Cara Menjalankan Program
Pastikan Python 3 sudah terinstal di komputer.
Jalankan file program melalui terminal atau command prompt dengan mengetikkan perintah: python nama_file_kamu.py
Output program akan menampilkan simulasi pembuatan objek, interaksi (memasukkan hewan ke kandang, petugas memberi makan), demonstrasi semua jenis method, serta pengujian Error Handling ketika memasukkan data yang tidak valid ke dalam setter.
