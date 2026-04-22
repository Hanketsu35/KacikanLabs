# ============================================================
# Exercise 1 — Hello World & Personal Info
# ============================================================

# --- Görev 1: "Hello, World!" yazdır ---
print("Hello, World!")

# --- Görev 2: Ad, soyad ve yaş al; birleştirip yazdır ---
first_name = input("First name: ")
last_name  = input("Last name: ")
age        = input("Age: ")

# İlkel yol: str() ile dönüştür, + ile birleştir
print("Hello, " + first_name + " " + last_name + "! You are " + age + " years old.")

# Kısa yol: print() virgülle birden fazla argüman alır
print("Hello,", first_name + " " + last_name + "! You are", age, "years old.")

# --- Görev 3: Doğum yılını hesapla ---
current_year = 2025
birth_year   = current_year - int(age)
print("Birth year: " + str(birth_year))

# --- BONUS: Favori sayı — kendisi, karesi ve küpü ---
favourite = int(input("Favourite number: "))
print("Number : " + str(favourite))
print("Square : " + str(favourite ** 2))
print("Cube   : " + str(favourite ** 3))
