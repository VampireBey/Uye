import os
import sys

SESSION = "userbot"

def temizle():
    os.system("clear" if os.name == "posix" else "cls")

def menu():
    temizle()
    print("=== BLAYZEN ÜYE ÇEKME BOTU ===\n")
    print("1. Hesap ekle")
    print("2. Hesap kaldır")
    print("3. Botu başlat")
    print("0. Çıkış\n")

    secim = input("Seçiminizi girin: ")
    if secim == "1":
        os.system("python3 login.py")
    elif secim == "2":
        try:
            os.remove(f"{SESSION}.session")
            print("Oturum kaldırıldı.")
        except:
            print("Oturum bulunamadı.")
        input("\nDevam etmek için Enter'a basın...")
        menu()
    elif secim == "3":
        os.system("python3 userbot_grup_aktar.py")
    elif secim == "0":
        sys.exit()
    else:
        input("Geçersiz giriş. Enter'a basarak tekrar deneyin...")
        menu()

if __name__ == "__main__":
    menu()
