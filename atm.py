+
kullanici_bilgileri = [
    {
        "hesap_numarasi": "123456",
        "sifre": "1234",
        "bakiye": 1000
    },
    {
        "hesap_numarasi": "0002",
        "sifre": "5678",
        "bakiye": 500
    }
]

def giris_yap():
    hesap_numarasi = input("Hesap numaranızı girin: ")
    sifre = input("Şifrenizi girin: ")
    
    for kullanici in kullanici_bilgileri:
        if hesap_numarasi == kullanici["hesap_numarasi"] and sifre == kullanici["sifre"]:
            return True
    
    return False

def atm():
    if not giris_yap():
        print("Geçersiz hesap numarası veya şifre!")
        return
    
    while True:
        print("""
        1. Bakiye sorgulama
        2. Para çekme
        3. Para yatırma
        4. Çıkış
        """)
        
        secim = input("Yapmak istediğiniz işlemi seçin (1-4): ")
        
        if secim == "1":
            print("Bakiyeniz:", kullanici_bilgileri[0]["bakiye"])  # İlk kullanıcının bakiyesini yazdırır
        elif secim == "2":
            miktar = float(input("Çekmek istediğiniz miktarı girin: "))
            if miktar <= kullanici_bilgileri[0]["bakiye"]:
                kullanici_bilgileri[0]["bakiye"] -= miktar  # İlk kullanıcının bakiyesinden çeker
                print("Yeni bakiyeniz:", kullanici_bilgileri[0]["bakiye"])
            else:
                print("Yetersiz bakiye!")
        elif secim == "3":
            miktar = float(input("Yatırmak istediğiniz miktarı girin: "))
            kullanici_bilgileri[0]["bakiye"] += miktar  # İlk kullanıcının bakiyesine yatırır
            print("Yeni bakiyeniz:", kullanici_bilgileri[0]["bakiye"])
        elif secim == "4":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçenek!")

atm()
