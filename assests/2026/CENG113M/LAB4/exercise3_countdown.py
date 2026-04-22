# =============================================================================
# CENG113M - Lab 4 | Exercise 3: Countdown Timer
# =============================================================================
# Ask the user for a positive integer n, count down from n to 1,
# then print "END!" after the loop finishes.
# Rule: Use a for loop with a negative step — no while loop allowed.
# =============================================================================

n = int(input("Enter n: "))

# range(n, 0, -1) starts at n, stops before 0, steps by -1
# e.g. range(3, 0, -1) → 3, 2, 1
for i in range(n, 0, -1):
    print(i)

print("END!")
