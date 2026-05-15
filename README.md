# Latihan Soal PBO

> ### by Ilaa

---

### 1. Sistem Manajemen Ekspedisi
**Deskripsi:** Anda diminta untuk membuat sebuah program manajemen pengiriman barang sederhana untuk sebuah agen ekspedisi menggunakan Python. Program ini harus mampu menangani perhitungan ongkos kirim secara otomatis berdasarkan variabel yang diinput oleh pengguna.

**Ketentuan Logika (Class PengirimanBarang):**

* **Atribut:**
    * `nama_pengirim`
    * `berat_barang` (kg)
    * `jarak_tempuh` (km)
    * `jenis_layanan` (Reguler/Express)
    * `asuransi` (True/False)

* **Metode menghitung ongkir :**
    * Tarif awal ditetapkan sebesar Rp 10.000 untuk 10 km pertama.
    * Jika jarak melebihi 10 km, maka setiap kelebihan per kilometernya dikenakan biaya tambahan sebesar Rp 2.000.

* **Metode menghitung biaya berat :**
    * Tarif berat standar adalah Rp 5.000 per kg.
    * Jika berat barang di atas 20 kg, maka berikan potongan harga sebesar 15% dari total biaya berat tersebut.

* **Metode menghitung biaya layanan :**
    * Jika memilih layanan **Express**, dikenakan biaya tambahan flat sebesar Rp 20.000.
    * Jika layanan **Reguler**, tidak dikenakan biaya tambahan.

* **Metode menghitung asuransi :**
    * Biaya asuransi hanya dihitung jika status asuransi adalah "True".
    * Besar biaya asuransi adalah 3% dari hasil perhitungan **Ongkir Dasar**.

* **Metode menghitung total akhir :**
    * Hitung total biaya sebelum asuransi (Ongkir Dasar + Biaya Berat + Biaya Layanan).
    * Jika total tersebut mencapai minimal Rp 150.000, berikan potongan **Voucher Hemat** senilai Rp 15.000.
    * Total akhir didapat dari: (Total sebelum asuransi - Voucher) + Biaya Asuransi.

* **Metode mencetak resi :**
    * Menampilkan output Nota yang berisi Nama Pengirim, Berat Barang, Jarak, Jenis Layanan, dan Total Biaya Akhir.

---