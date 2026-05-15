class ekspedisiw:
    

    def hitung_ongkir_dasar(self):
        tarif = 10000  
        if self.jarak_tempuh > 10:
            kelebihan = self.jarak_tempuh - 10
            tarif = tarif + (kelebihan * 2000)
        return tarif


    def hitung_biaya_berat(self):
        biaya = self.berat_barang * 5000 
        if self.berat_barang > 20:
            potongan = 0.15 * biaya
            biaya = biaya - potongan
        return biaya

    def hitung_biaya_layanan(self):
        if self.jenis_layanan.lower() == "express":
            return 20000  
        return 0

    def hitung_biaya_asuransi(self):
        if self.asuransi == "y":
            return 0.03 * self.hitung_ongkir_dasar()
        return 0

    def hitung_total_akhir(self):
        total_sebelum = self.hitung_ongkir_dasar() + self.hitung_biaya_berat() + self.hitung_biaya_layanan()
        
        voucher = 0
        if total_sebelum >= 150000:
            voucher = 15000
            
        total_akhir = (total_sebelum - voucher) + self.hitung_biaya_asuransi()
        return total_akhir

    def cetak_resi(self):
        print(f"Nama Pengirim : {self.nama_pengirim}")
        print(f"Berat Barang  : {self.berat_barang} kg")
        print(f"Jarak Tempuh  : {self.jarak_tempuh} km")
        print(f"Jenis Layanan : {self.jenis_layanan}")
        print(f"Total Bayar   : Rp {int(self.hitung_total_akhir()):}")



lagi = "y"

while lagi.lower() == "y":
    p = ekspedisi()
    
    print("\n--- Form Input Ekspedisi ---")
    
    p.nama_pengirim = input("Masukkan Nama Pengirim: ")
    p.berat_barang  = int(input("Masukkan Berat (kg): "))
    p.jarak_tempuh  = int(input("Masukkan Jarak (km): "))
    p.jenis_layanan = input("Layanan (Reguler/Express): ")
    p.asuransi      = input("Gunakan Asuransi? (y/n): ")

    
    lagi = input("\nTambah data pengiriman lagi? (y/n): ")
