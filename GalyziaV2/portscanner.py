import socket
from datetime import datetime

# Fungsi untuk memindai port
def scan_port(target, port):
    try:
        # Membuat koneksi socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)  # Batas waktu koneksi 1 detik
        
        # Koneksikan socket ke target dan port
        result = sock.connect_ex((target, port))
        
        # Jika port terbuka, result = 0
        if result == 0:
            print(f"Port {port} terbuka")
        sock.close()
    except KeyboardInterrupt:
        print("\nScan dihentikan oleh pengguna.")
        exit()
    except socket.gaierror:
        print("\nHostname tidak valid.")
        exit()
    except socket.error:
        print("\nTidak dapat terhubung ke server.")
        exit()

# Fungsi utama untuk meminta input dan memindai rentang port
def main():
    print("== Port Scanner ==")
    
    # Meminta input target dari pengguna (alamat IP atau domain)
    target = input("Masukkan IP atau domain yang ingin dipindai: ")
    
    # Memvalidasi domain/IP
    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("Hostname tidak valid.")
        return
    
    print(f"Memulai scan pada target: {target_ip}")
    
    # Meminta rentang port
    start_port = int(input("Masukkan port awal: "))
    end_port = int(input("Masukkan port akhir: "))
    
    # Menyimpan waktu mulai pemindaian
    start_time = datetime.now()
    
    print(f"\nMemindai port {start_port} hingga {end_port}...\n")
    
    # Memindai port dalam rentang yang diberikan
    for port in range(start_port, end_port + 1):
        scan_port(target_ip, port)
    
    # Menyimpan waktu selesai pemindaian
    end_time = datetime.now()
    total_time = end_time - start_time
    
    print(f"\nPemindaian selesai dalam {total_time} detik.")

if __name__ == "__main__":
    main()
