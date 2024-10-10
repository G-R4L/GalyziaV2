import requests

def get_ip_info(ip):
    try:
        # Menggunakan API untuk mendapatkan informasi IP
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()

        if data['status'] == 'fail':
            print("Error: " + data['message'])
            return

        # Menampilkan informasi IP
        print(f"\nInformasi untuk IP: {ip}")
        print(f"Hostname: {data.get('hostname', 'N/A')}")
        print(f"Lokasi: {data.get('country', 'N/A')}, {data.get('regionName', 'N/A')}, {data.get('city', 'N/A')}")
        print(f"Postcode: {data.get('zip', 'N/A')}")
        print(f"ISP: {data.get('isp', 'N/A')}")
        print(f"Lat/Lng: {data.get('lat', 'N/A')}, {data.get('lon', 'N/A')}")

    except requests.exceptions.RequestException as e:
        print("Error while fetching IP information:", e)

def main():
    ip = input("Masukkan alamat IP yang ingin dilacak: ")
    get_ip_info(ip)

if __name__ == "__main__":
    main()
