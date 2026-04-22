# ============================================================
# Exercise 7 — Currency Converter  (Hard)
# ============================================================

# Sabit dönüşüm katsayıları (büyük harf → sabit değer convention'ı)
USD_TO_EUR = 0.92
USD_TO_GBP = 0.79
USD_TO_TRY = 32.50
USD_TO_JPY = 149.80

amount = float(input("Enter USD: "))

eur = amount * USD_TO_EUR
gbp = amount * USD_TO_GBP
try_ = amount * USD_TO_TRY   # try Python'da anahtar kelime; try_ kullanıyoruz
jpy = amount * USD_TO_JPY

# İlkel yol: str() + manuel boşlukla hizalama
print(str(amount) + " USD =")
print("  " + str(eur)  + " EUR")
print("  " + str(gbp)  + " GBP")
print("  " + str(try_) + " TRY")
print("  " + str(jpy)  + " JPY")

print("")  # boş satır

# --- Extra Challenge 1: Ondalık noktaları hizala ---
# Kısa yol (f-string): sınav/ödevde f-string kullanma yasağı varsa üstteki yolu kullan.
print(str(round(amount, 2)).rjust(10) + " USD =")
print(str(round(eur,  2)).rjust(10)  + " EUR")
print(str(round(gbp,  2)).rjust(10)  + " GBP")
print(str(round(try_, 2)).rjust(10)  + " TRY")
print(str(round(jpy,  2)).rjust(10)  + " JPY")

print("")

# --- Extra Challenge 2: Ters kur (1 birim = kaç USD?) ---
print("1 EUR = " + str(round(1 / USD_TO_EUR, 4)) + " USD")
print("1 GBP = " + str(round(1 / USD_TO_GBP, 4)) + " USD")
print("1 TRY = " + str(round(1 / USD_TO_TRY, 4)) + " USD")
print("1 JPY = " + str(round(1 / USD_TO_JPY, 4)) + " USD")
