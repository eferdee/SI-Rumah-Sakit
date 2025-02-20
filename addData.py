import pandas as pd

# Data contoh
data = {
    "ID": [1, 2, 3],
    "Nama": ["Andi", "Budi", "Citra"],
    "Usia": [25, 30, 22],
    "Diagnosa": ["Flu", "Demam", "Asma"],
    "Status": ["Rawat Jalan", "Rawat Inap", "Rawat Jalan"]
}

# Membuat DataFrame
df = pd.DataFrame(data)

# Simpan ke file CSV
df.to_csv("patients.csv", index=False)

print("File CSV berhasil dibuat!")
