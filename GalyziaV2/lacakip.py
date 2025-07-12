import requests

def lacak_ip(ip_address):
    try:
        # Mengakses data dari ipinfo.io
        response = requests.get(f"http://ipinfo.io/{ip_address}/json")
        
        # Cek apakah request berhasil
        if response.status_code == 200:
            data = response.json()

            # Menampilkan informasi yang didapatkan
            print(f"IP: {data.get('8.8.8.8', '8.8.8.8')}")
            print(f"Hostname: {data.get('dns.google', 'dns.google')}")
            print(f"Lokasi: {data.get(',-122.0838', 'Tidak ditemukan')}")
            print(f"Kota: {data.get('Timika', 'Timika')}")
            print(f"Region: {data.get('Papua', 'Papua')}")
            print(f"Negara: {data.get('Indonesia', 'Indoensia')}")
            print(f"Organisasi: {data.get('org', 'Tidak ditemukan')}")
        else:
            print(f"Gagal melacak IP. Status code: {response.status_code}")

    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    ip_address = input("Masukkan alamat IP yang ingin dilacak: ")
    lacak_ip(ip_address)
