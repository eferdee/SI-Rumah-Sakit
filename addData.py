import pandas as pd

# Data untuk setiap CSV
doctors_data = [
    ["Dr. Andi", "Umum", "Senin - Jumat 08:00 - 15:00"],
    ["Dr. Budi", "Bedah", "Senin - Rabu 10:00 - 16:00"],
    ["Dr. Clara", "Anak", "Selasa - Kamis 09:00 - 14:00"],
    ["Dr. Dika", "Jantung", "Jumat - Sabtu 08:00 - 13:00"]
]
medicines_data = [
    ["Paracetamol", 100, 5000],
    ["Amoxicillin", 50, 10000],
    ["Ibuprofen", 30, 12000],
    ["Omeprazole", 40, 15000]
]
payments_data = [
    [1, "Amanda", 250000, "Lunas"],
    [2, "Budi", 500000, "Belum Lunas"],
    [3, "Citra", 750000, "Lunas"],
    [4, "Dimas", 400000, "Belum Lunas"]
]

# Simpan ke CSV
pd.DataFrame(doctors_data, columns=["Nama Dokter", "Spesialisasi", "Jadwal"]).to_csv("doctors.csv", index=False)
pd.DataFrame(medicines_data, columns=["Nama Obat", "Stok", "Harga"]).to_csv("medicines.csv", index=False)
pd.DataFrame(payments_data, columns=["ID Pasien", "Nama", "Total Biaya", "Status Pembayaran"]).to_csv("payments.csv", index=False)

print("CSV files have been created successfully!")
