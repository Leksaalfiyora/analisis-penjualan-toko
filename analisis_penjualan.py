
# Studi Kasus: Analisis Data Penjualan Toko

data_penjualan = [
    {"produk": "Buku", "jumlah": 10, "harga": 5000},
    {"produk": "Pulpen", "jumlah": 20, "harga": 3000},
    {"produk": "Pensil", "jumlah": 15, "harga": 2000},
    {"produk": "Buku", "jumlah": 5, "harga": 5000},
    {"produk": "Penghapus", "jumlah": 8, "harga": 2000},
]

# 1. Memahami dan membersihkan data
data_bersih = []

for data in data_penjualan:
    if (
        data["produk"]
        and data["jumlah"] > 0
        and data["harga"] > 0
    ):
        data_bersih.append(data)

# 2. Menghitung pendapatan setiap produk
pendapatan_produk = {}
total_pendapatan = 0

for data in data_bersih:
    produk = data["produk"]
    pendapatan = data["jumlah"] * data["harga"]

    pendapatan_produk[produk] = (
        pendapatan_produk.get(produk, 0) + pendapatan
    )

    total_pendapatan += pendapatan

# 3. Menampilkan hasil analisis
print("=== ANALISIS PENJUALAN TOKO ===")
print("Total pendapatan: Rp", total_pendapatan)

print("\nPendapatan setiap produk:")
for produk, pendapatan in pendapatan_produk.items():
    print(f"{produk}: Rp {pendapatan}")

produk_terlaris = max(
    data_bersih, key=lambda data: data["jumlah"]
)["produk"]

print("\nProduk dengan jumlah penjualan tertinggi:",
      produk_terlaris)
