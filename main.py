import sympy as sp

x = sp.symbols("x")

# Kullanıcıdan fonksiyon ve değişken sayısını alma
fonksiyon = input("Fonksiyonu ve değişken sayısını girin (örneğin: x**2 + 2*x, 1): ")

# Girdiyi virgülle ayırarak fonksiyon ve değişken sayısını alma
fonksiyon, degisken_sayisi = fonksiyon.split(',')
fonksiyon_ifadesi = sp.sympify(fonksiyon)
degisken_sayisi = int(degisken_sayisi)

# Girilen fonksiyonu matematiksel ifadeye çevirme
fonksiyon_ifadesi = sp.sympify(fonksiyon)

# Fonksiyonun türevini al
turev = sp.diff(fonksiyon_ifadesi, x)
turev_metni = f"Fonksiyonun türevi: {turev}\n"

# Kökleri bul
kokler = sp.solve(turev, x)
kokler_metni = f"Fonksiyonun kökleri: {kokler}\n"

# İkinci Türev
turev_ikinci = sp.diff(turev, x)
turev_ikinci_metni = f"Fonksiyonun ikinci türevi: {turev_ikinci}\n"

# Yerel minimum ve yerel maksimum değerlerini bul
min_deger = sp.solve(turev, x)
max_deger = sp.solve(turev_ikinci, x)
min_deger_metni = f"Yerel minimum değerleri: {min_deger}\n"
max_deger_metni = f"Yerel maksimum değerleri: {max_deger}\n"

# Dosyaya yazma işlemi
with open("fonksiyon_ciktilari.txt", "w") as dosya:
    dosya.write(turev_metni)
    dosya.write(kokler_metni)
    dosya.write(turev_ikinci_metni)
    dosya.write(min_deger_metni)
    dosya.write(max_deger_metni)

print("Çıktılar dosyaya kaydedildi.")
