import requests

def get_weather(city):
    api_key = "f7f7dbe1304b0cdeea8f1f3780b8d537"  # Ganti dengan API key Anda dari OpenWeatherMap
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Menggunakan Celsius
    }
    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        print(f"\nCuaca di {city}:")
        print(f"Suhu: {data['main']['temp']}°C")
        print(f"Kondisi: {data['weather'][0]['description']}")
        print(f"Kelembapan: {data['main']['humidity']}%")
        print(f"Kecepatan Angin: {data['wind']['speed']} m/s")
    else:
        print(f"Error: {data['message']}")

def main():
    city = input("Masukkan nama kota: ")
    get_weather(city)

if __name__ == "__main__":
    main()
