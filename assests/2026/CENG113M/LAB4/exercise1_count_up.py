# =============================================================================
# CENG113M - Lab 4 | Exercise 1: Count Up!
# =============================================================================
# Ask the user for a positive integer n, then print all integers from 1 to n.
# Rule: Use a for loop with range() — no while loop allowed.
# =============================================================================

n = int(input("Enter n: "))

# range(1, n+1) generates numbers starting from 1 up to and including n
for i in range(1, n + 1):
    print(i)
