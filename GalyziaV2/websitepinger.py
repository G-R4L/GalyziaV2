import os
import platform

def ping_website(url):
    # Mendapatkan perintah ping sesuai dengan OS
    param = '-n 1' if platform.system().lower() == 'windows' else '-c 1'
    
    # Jalankan perintah ping
    command = f"ping {param} {url}"
    response = os.system(command)
    
    # Mengecek hasil ping
    if response == 0:
        print(f"{url} is reachable.")
    else:
        print(f"{url} is not reachable.")

def main():
    print("Website Pinger")
    print("=========================")
    
    while True:
        url = input("Masukkan URL (tanpa http/https, misalnya google.com) atau ketik 'exit' untuk keluar: ")
        if url.lower() == "exit":
            break
        ping_website(url)

if __name__ == "__main__":
    main()
