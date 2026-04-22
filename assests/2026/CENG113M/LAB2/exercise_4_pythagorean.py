# ============================================================
# Exercise 4 — Pythagorean Theorem
# ============================================================
# c² = a² + b²   →   c = √(a² + b²)
# Karekök yoktur; bunun yerine: √x = x ** 0.5  (yani x'in 1/2. kuvveti)

a = float(input("Side a: "))
b = float(input("Side b: "))

# Doğru hesaplama
c = (a ** 2 + b ** 2) ** 0.5
print("Hypotenuse c: " + str(c))

# --- BONUS: Neden parantez önemli? ---
# Şunu dene ve çıktıya bak:
wrong = (a ** 2 + b ** 2) ** 1 / 2
# Neden yanlış?
# Operatör önceliği: ** önce, / sonra çalışır.
# Yani:  (a²+b²)^1  /  2  =  (a²+b²) / 2  →  yanlış!
print("Wrong result (missing parentheses): " + str(wrong))
print("Explanation: ** runs before /, so it reads as ((a2+b2)**1) / 2")

# Doğrusu: parantez içine al
correct = (a ** 2 + b ** 2) ** (1 / 2)
print("Correct with (1/2): " + str(correct))

# --- BONUS: Hipotenüs ve bir kenar verilince diğer kenar ---
# c² = a² + b²  →  b² = c² - a²  →  b = √(c² - a²)
c_given = float(input("Hypotenuse c: "))
a_given = float(input("Known side a: "))

b_found = (c_given ** 2 - a_given ** 2) ** 0.5
print("Missing side b: " + str(b_found))
