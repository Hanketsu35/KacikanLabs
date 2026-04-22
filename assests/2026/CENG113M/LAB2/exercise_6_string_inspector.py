# ============================================================
# Exercise 6 — String Inspector
# ============================================================

text = input("Enter a word or sentence: ")

# 1. Orijinal metin
print("Original       : " + text)

# 2. Tümü büyük harf
print("Uppercase      : " + text.upper())

# 3. Tümü küçük harf
print("Lowercase      : " + text.lower())

# 4. Karakter sayısı
print("Length         : " + str(len(text)))

# 5. İlk karakter
print("First character: " + text[0])

# 6. Son karakter
print("Last character : " + text[-1])

# 7. Ters çevrilmiş metin
print("Reversed       : " + text[::-1])

# 8. Palindrom kontrolü (büyük/küçük harfe duyarsız)
is_palindrome = text.lower() == text.lower()[::-1]
print("Palindrome     : " + str(is_palindrome))
