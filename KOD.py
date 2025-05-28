import hashlib
import itertools
import time

hash_kodu = "b7c60e8b47559cb6d94b8e36fa227fc048afb4c6"
alfabe = "0123456789abcdefghijklmnopqrstuvwxyz"
mesaj_uzunluk = 5
hash_algoritması = hashlib.sha1 #benimki (SHA-1)

print(f"Kullanılacak hash algoritması :{hash_algoritması().name.upper()}")
print(f"Kırılacak kod: {hash_kodu}")
print(f"Kullanılan Alfabe: {alfabe}")
print(f"Mesaj Uzunluğu: {mesaj_uzunluk} karakter")

print(f"Toplam Olasılık Sayısı: {len(alfabe) ** mesaj_uzunluk}")

start_time = time.time()
bulunan_mesaj = None
sayac = 0
rapor = 2000000

kombinasyonlar = itertools.product(alfabe, repeat=mesaj_uzunluk)

try:
    for kombi_tuple in kombinasyonlar:
        sayac += 1
        # string çevirme
        kombi_str = "".join(kombi_tuple)

        # String'i hashlemek için byte dizisine çevir
        kombi_byte = kombi_str.encode('utf-8')

        # sha1 ile  algoritma hash'i hesapla
        hesaplanan_hash = hash_algoritması(kombi_byte).hexdigest()

        # karşılaştır
        if hesaplanan_hash == hash_kodu:
            bulunan_mesaj = kombi_str
            print(f"\n TESPİT EDİLDİ (Deneme #{sayac})")
            break

        # İlerleme raporu
        if sayac % rapor == 0:
            gecen_sure = time.time() - start_time
            # Mevcut denemeyi ve geçen süre
            print(f"Deneme :{sayac}: mesaj:'{kombi_str}' ,Hesaplanan hash kodu:{hesaplanan_hash} Geçen süre:({gecen_sure:.2f} saniye)")

except KeyboardInterrupt:
    print("\nİptal.")
    bulunan_mesaj = None

end_time = time.time()
total_time = end_time - start_time

if bulunan_mesaj:
    print("İŞLEM BAŞARILI!")
    print(f"Orijinal Mesaj: {bulunan_mesaj}")
    # Bulunan mesajın hash'ini tekrar hesaplayarak doğrulama yapalım
    dogrulanan_hash = hash_algoritması(bulunan_mesaj.encode('utf-8')).hexdigest()
    print(f"Doğrulanan Hash: {dogrulanan_hash}")
    print(f"Hedef Hash:{hash_kodu}")
    if dogrulanan_hash == hash_kodu:
        print("(Doğrulama Başarılı)")
    else:
        print("Doğrulama BAŞARISIZ ")
else:
    print("İŞLEM BAŞARISIZ!")
    if sayac == len(alfabe) ** mesaj_uzunluk:
        print(" eşleşen mesaj bulunamadı.")
    else:
        print("İşlem tamamlanmadan bitti veya iptal edildi.")


print(f"Toplam Deneme Sayısı: {sayac}")
print(f"Toplam Geçen Süre: {total_time:.2f} saniye")
