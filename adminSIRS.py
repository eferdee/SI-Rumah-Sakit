import streamlit as st
import pandas as pd

# Simulasi database pasien dan lainnya (bisa diganti dengan database nyata seperti PostgreSQL, MySQL, dll.)
PATIENTS_PATH = "patients.csv"
DOCTORS_PATH = "doctors.csv"
MEDICINES_PATH = "medicines.csv"
PAYMENTS_PATH = "payments.csv"


def load_data(path, columns):
    try:
        return pd.read_csv(path)
    except FileNotFoundError:
        return pd.DataFrame(columns=columns)

def save_data(df, path):
    df.to_csv(path, index=False)

def main():
    st.title("Admin Rumah Sakit")
    menu = ["Dashboard", "Tambah Pasien", "Update Pasien", "Jadwal Dokter", "Pembayaran", "Ketersediaan Obat"]
    choice = st.sidebar.selectbox("Menu", menu)
    patients_df = load_data(PATIENTS_PATH, ["ID", "Nama", "Usia", "Diagnosa", "Status"])
    doctors_df = load_data(DOCTORS_PATH, ["Nama Dokter", "Spesialisasi", "Jadwal"])
    medicines_df = load_data(MEDICINES_PATH, ["Nama Obat", "Stok", "Harga"])
    payments_df = load_data(PAYMENTS_PATH, ["ID Pasien", "Nama", "Total Biaya", "Status Pembayaran"])
    
    if choice == "Dashboard":
        st.subheader("Dashboard Pasien")
        status_filter = st.selectbox("Filter berdasarkan status", ["Semua", "Rawat Inap", "Rawat Jalan", "Sembuh", "Meninggal"])
        if status_filter != "Semua":
            patients_df = patients_df[patients_df["Status"] == status_filter]
        st.dataframe(patients_df)
        
    elif choice == "Tambah Pasien":
        st.subheader("Tambah Data Pasien")
        nama = st.text_input("Nama")
        usia = st.number_input("Usia", min_value=0, max_value=120, step=1)
        diagnosa = st.text_area("Diagnosa")
        status = st.selectbox("Status", ["Rawat Inap", "Rawat Jalan", "Sembuh", "Meninggal"])
        if st.button("Simpan"):
            new_data = pd.DataFrame([[len(patients_df) + 1, nama, usia, diagnosa, status]], 
                                    columns=["ID", "Nama", "Usia", "Diagnosa", "Status"])
            patients_df = pd.concat([patients_df, new_data], ignore_index=True)
            save_data(patients_df, PATIENTS_PATH)
            st.success("Data pasien berhasil ditambahkan!")
            
    elif choice == "Update Pasien":
        st.subheader("Update Status Pasien")
        id_list = patients_df["ID"].tolist()
        pasien_id = st.selectbox("Pilih ID Pasien", id_list)
        new_status = st.selectbox("Update Status", ["Rawat Inap", "Rawat Jalan", "Sembuh", "Meninggal"])
        if st.button("Update"):
            patients_df.loc[patients_df["ID"] == pasien_id, "Status"] = new_status
            save_data(patients_df, PATIENTS_PATH)
            st.success("Status pasien diperbarui!")
            
    elif choice == "Jadwal Dokter":
        st.subheader("Jadwal Dokter")
        st.dataframe(doctors_df)
        
    elif choice == "Pembayaran":
        st.subheader("Pembayaran Pasien")
        st.dataframe(payments_df)
        
    elif choice == "Ketersediaan Obat":
        st.subheader("Ketersediaan Obat")
        st.dataframe(medicines_df)
        obat_terpilih = st.selectbox("Pilih Obat", medicines_df["Nama Obat"].tolist())
        if st.button("Kurangi Stok"):
            medicines_df.loc[medicines_df["Nama Obat"] == obat_terpilih, "Stok"] -= 1
            save_data(medicines_df, MEDICINES_PATH)
            st.success("Stok obat berhasil dikurangi!")

if __name__ == "__main__":
    main()