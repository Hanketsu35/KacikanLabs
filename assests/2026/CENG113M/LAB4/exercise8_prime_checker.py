# =============================================================================
# CENG113M - Lab 4 | Exercise 8: Prime Number Checker
# =============================================================================
# Ask the user for a positive integer n, then check if it is prime.
# A number is prime if it has no divisors other than 1 and itself.
# Loop from 2 to n-1 and test if any number divides n evenly.
# If a divisor is found → use break and print "Not prime"
# If no divisor is found → print "Prime"
# =============================================================================

n = int(input("Enter n: "))

is_prime = True                  # Assume the number is prime until proven otherwise

for i in range(2, n):            # Test every integer from 2 up to n-1
    if n % i == 0:               # Found a divisor → n is not prime
        is_prime = False
        break                    # No need to keep checking — exit the loop early

# Ternary expression: print the result based on the flag
if is_prime == True:
    print("Prime")
else:
    print("not prime")
