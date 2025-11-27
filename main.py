                         ##             git s   # HTTP = istemci ↔ sunucu konuşma kuralı
                                        # HyperText Transfer Protocol (Köprü Metni Aktarım Protokolü)
import requests                          # HTTP : isteği yapmak (internet üzerinden veri çekmek) için kullanılıyor.
from colorama import Fore, Style, init           # Konsolda renkli metin yazdırmak için kullanılıyor.
from datetime import datetime, timedelta, timezone   # Tarih/saat işlemleri ve zaman dilimi (timezone) için gerekli.


   # Colorama kütüphanesinin içindeki bir “başlatma / ayarlama (initialize)” fonksiyonudur.
init()                                  # Colorama’nın Windows da dahil düzgün çalışması için gerekli başlangıç ayarı.


city = input("Sehir Adı: ")
                                 # API (Application Programming Interface)
# Bir yazılımın, başka bir yazılımla nasıl konuşacağını tanımlayan kurallar ve yöntemler setidir.
API_KEY = "a586dc1195cc8c684b41390cd6c74f99"
                               # OpenWeatherMap API’sine erişim için kullanılan özel anahtar


                                         # URL (Uniform Resource Locator), internet üzerindeki bir kaynağın adresi
                                         # requests.get(url) ile bu adrese bir HTTP isteği gönderiyoruz ve OpenWeatherMap bize JSON verisi döndürüyor.
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=tr"
                                         # f → “bu string içinde süslü parantezle değişken kullanacağım” anlamına gelir.

                                          # response: Sunucudan gelen cevabı (status code, body vs.) içerir.
response = requests.get(url)              # Verdiğimiz URL’ye bir HTTP GET isteği gönderir.
data = response.json()                    # Cevabın gövdesini JSON formatından Python sözlüğüne (dict) çevirir.
                                          # data: Artık bir Python dict; içine data['main']['temp'] gibi ulaşabiliriz.

# Renkli yazma Fonksiyonu
def ccolored(label, value, color=Fore.YELLOW):       # varsayılan renk Sarı
    print(f"{color}{label}:{Style.RESET_ALL}{value} ")


if response.status_code == 200:            #  Sunucu cevabının HTTP durum kodu.
    # Şehir Adı
    colored("🌤 Şehir", data['name'], Fore.RED)

    # Şehrin Saat ve Tarihi
    timezone_offset = data['timezone']            # Şehrin UTC’ye göre zaman farkını saniye cinsinden verir
    utc_now = datetime.now(timezone.utc)                # Şu anki UTC zamanını alır (zaman dilimi bilgisiyle).
    local_time = utc_now + timedelta(seconds=timezone_offset)    # UTC zamanına ofseti ekleyerek şehrin yerel zamanını hesaplar.



    colored(f"⏱ Local Time", local_time.strftime('%I:%M %p'), Fore.CYAN)   # Saati HH:MM AM/PM formatında yazar
    colored(f"📅 Date", local_time.strftime('%b %d, %Y'), Fore.CYAN)      # Tarihi Mon 12, 2024 gibi formatlar (%b = kısa ay adı).
                                                                        # farklı renk için satır sonuna ekleme

    # Hava Durumu
    colored("🌡 Sıcaklık", f"{data['main']['temp']}°C")
    colored("💧 Nem", f"{data['main']['humidity']}%")
    colored("☁️ Durum", data['weather'][0]['description'])

    # Eğlence
    temp = data['main']['temp']
    if temp > 30:
        print('\n🔥 Çok sıcak! Şapka ve güneş kremi almayı unutma!')
    elif temp < 10:
        print("\n🥶 Çok soğuk! Montunu giy ve dışarı çık.")
    else:
        print("\n🙂 Hava güzel, dışarı çıkıp keyfini çıkarabilirsin!")

else:
    print("⚠️ Şehir bulunamadı veya bir hata oluştu.")
