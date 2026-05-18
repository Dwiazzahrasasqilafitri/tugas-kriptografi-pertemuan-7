import hashlib

database_pengguna = {}

def hitung_sha256(password_plain):
    password_bytes = password_plain.encode('utf-8')
    objek_sha256 = hashlib.sha256(password_bytes)
    password_terhash = objek_sha256.hexdigest()
    
    return password_terhash

def menu_registrasi():
    print("\n=== MENU REGISTRASI ===")
    username = input("Masukkan Username Baru: ").strip()
    
    if username in database_pengguna:
        print("Gagal: Username sudah digunakan! Silakan pilih username lain.")
        return

    password = input("Masukkan Password Baru: ")
    
    password_aman = hitung_sha256(password)
    
    database_pengguna[username] = password_aman
    
    print("\n--------------------------------------------------")
    print(f"Status: REGISTRASI BERHASIL!")
    print(f"Password Asli : {password}")
    print(f"Hasil SHA-256 : {password_aman} (Disimpan ke database)")
    print("--------------------------------------------------")

def menu_login():
    print("\n=== MENU LOGIN ===")
    username = input("Username: ").strip()
    password = input("Password: ")
    
    if username not in database_pengguna:
        print("\nStatus: LOGIN GAGAL! (Username tidak ditemukan)")
        return
        
    hash_password_input = hitung_sha256(password)
    
    hash_password_tersimpan = database_pengguna[username]
    
    if hash_password_input == hash_password_tersimpan:
        print("\nStatus: LOGIN BERHASIL! (Selamat datang!)")
    else:
        print("\nStatus: LOGIN GAGAL! (Password salah)")

def main():
    while True:
        print("\n=======================================")
        print("   APLIKASI LOGIN & REGISTRASI AMAN    ")
        print("      TUGAS MAHASISWA NO. URUT 8       ")
        print("=======================================")
        print("1. Registrasi Akun Baru")
        print("2. Login")
        print("3. Keluar")
        
        pilihan = input("Pilih menu (1/2/3): ").strip()
        
        if pilihan == '1':
            menu_registrasi()
        elif pilihan == '2':
            menu_login()
        elif pilihan == '3':
            print("\nTerima kasih! Program selesai.")
            break
        else:
            print("\nPilihan tidak valid. Silakan pilih 1, 2, atau 3.")

if __name__ == "__main__":
    main()