from ecommerce.pricing import hitung_diskom, hitung_total, hitung_pajak
from ecommerce.order import generate_order_id

def main():
    nama_pelanggan = input("Masukkan Nama Pelanggan: ")
    nama_produk = input("Masukkan Nama Produk :")
    harga_asli = float(input("Masukkan Harga Asli :"))
    presentase_diskon = float(input("Masukkan Presentase Diskon :"))
    presentasi_pajak = float(input("Masukkan Presentase Pajak :"))

    diskon = harga_asli * (presentase_diskon / 100)
    total = hitung_total(harga_asli, presentase_diskon, presentase_pajak)
    order_id = generate_order_id()

    print("="40)
    print("Rincian Pembelian")
    print("="*40)
    print(f"{'ID Pesanan' : 20} {order_id}")
    print(f"{'Nama Pelanggan' :20} {nama_pelanggan}")
    print(f"{'Nama Produk' :20} {nama_produk}")
    print(f"{'Harga Asli" :20} {harga_asli:,.2f}"}
    print(f"{'Diskon' :20} RP{diskon:,.2f}")
    print(f"{'Pajak' :20} RP{hitung_pajak(harga_asli - diskon, presentase_pajak):,.2f}")
    print("="*40)
    print(f"{'Total Belanja' :20} RP{total:,.2f}")
    print("="*40)

    if_name_ == "_main_":
    main()
