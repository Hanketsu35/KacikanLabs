# ============================================================
# Exercise 2 — Temperature Converter
# ============================================================
# Formüller:
#   Celsius  → Fahrenheit:  F = C * 1.8 + 32
#   Celsius  → Kelvin:      K = C + 273.15
#   Fahrenheit → Celsius:   C = (F - 32) * (5 / 9)

# --- Celsius → Fahrenheit ve Kelvin ---
c = float(input("Enter temperature in Celsius: "))

f = (c * 1.8) + 32
k = c + 273.15

print(str(c) + " °C  =  " + str(f) + " °F")
print(str(c) + " °C  =  " + str(k) + " K")

# --- BONUS: Fahrenheit → Celsius ---
f_input = float(input("Enter temperature in Fahrenheit: "))

c_back = (f_input - 32) * (5 / 9)

print(str(f_input) + " °F  =  " + str(c_back) + " °C")
