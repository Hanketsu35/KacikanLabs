# =============================================================================
# CENG113M - Lab 4 | Exercise 4: Multiplication Table
# =============================================================================
# Ask the user for an integer n, then print the multiplication table of n
# from 1 to 10. Each line format: "n x i = result"
# =============================================================================

n = int(input("Enter n: "))

# range(1, 11) loops from 1 to 10 inclusive
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
