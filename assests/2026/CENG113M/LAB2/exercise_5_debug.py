# ============================================================
# Exercise 5 — Debug: Find & Fix the 5 Bugs
# ============================================================
# Orijinal hatalı kod aşağıda yorum satırı olarak verilmiştir.
# Her hatanın açıklaması ve düzeltmesi altında gösterilmiştir.

# ----- Orijinal (hatalı) kod -----
# num1 = input("First number: ")       # Bug 1
# num2 = input("Second number: ")      # Bug 2
# average = num1 + num2 / 2            # Bug 3
# Print("The average is: " average)    # Bug 4
# massege = "Done"                     # Bug 5
# print(Massege)

# ----- Düzeltilmiş kod -----

# Bug 1 & 2: input() her zaman str döndürür; aritmetik için int() veya float() şart.
num1 = float(input("First number: "))
num2 = float(input("Second number: "))

# Bug 3: Operatör önceliği! Orijinalde: num1 + (num2 / 2) → yanlış.
#         Ortalama formülü: (a + b) / 2  → parantez gerekli.
average = (num1 + num2) / 2

# Bug 4: Python'da yerleşik fonksiyon adları küçük harfle yazılır: print(), input() ...
#         "Print" diye bir fonksiyon yok — NameError verir.
#         Ayrıca "The average is: " ile average arasında + veya virgül olmalı.
print("The average is: " + str(average))

# Bug 5: Değişken adı tutarlı olmalı. "massege" tanımlanmış ama "Massege" kullanılmış.
#         Python büyük/küçük harfe duyarlıdır (case-sensitive).
message = "Done"
print(message)
