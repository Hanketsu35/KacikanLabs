# =============================================================================
# CENG113M - Lab 4 | Exercise 2: Sum of Numbers
# =============================================================================
# Ask the user for a positive integer n, then calculate the sum 1 + 2 + ... + n.
# Key pattern: accumulator variable — total starts at 0, add each number to it.
# Mathematical shortcut: n × (n + 1) / 2   e.g. n=5 → 5×6/2 = 15
# =============================================================================

n = int(input("Enter n: "))

total = 0                    # Accumulator: starts at zero
for i in range(1, n + 1):
    total = total + i        # Add each number to the running total

print(f"The sum is: {total}")
