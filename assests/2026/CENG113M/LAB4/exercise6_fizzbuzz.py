# =============================================================================
# CENG113M - Lab 4 | Exercise 6: FizzBuzz
# =============================================================================
# Loop from 1 to 20 and apply these rules:
#   - Divisible by BOTH 3 and 5 → print "FizzBuzz"
#   - Divisible by 3 only       → print "Fizz"
#   - Divisible by 5 only       → print "Buzz"
#   - Otherwise                 → print the number itself
#
# Important: Check divisibility by 15 (both 3 and 5) FIRST.
# If you check 3 or 5 first, numbers like 15 will match too early
# and never reach the "FizzBuzz" branch.
# =============================================================================

for i in range(1, 21):
    if i % 15 == 0:     # Divisible by both 3 and 5 — must check this first!
        print("FizzBuzz")
    elif i % 3 == 0:    # Divisible by 3 only
        print("Fizz")
    elif i % 5 == 0:    # Divisible by 5 only
        print("Buzz")
    else:
        print(i)        # Not divisible by 3 or 5 — just print the number
