# =============================================================================
# CENG113M - Lab 4 | Exercise 9: Skip Evens, Stop at 7
# =============================================================================
# Loop over numbers 1 to 10 using a for loop:
#   - Use 'continue' to skip even numbers (do not print them).
#   - Use 'break' to stop the loop entirely when the number reaches 7.
#
# continue → skips the rest of the current iteration and jumps to the next one
# break    → exits the loop immediately, regardless of the loop condition
#
# Expected output: 1  3  5
# (7 is never printed because we break before the print statement)
# =============================================================================

for i in range(1, 11):
    if i == 7:
        break            # Stop the entire loop when i reaches 7

    if i % 2 == 0:
        continue         # Skip even numbers — jump to the next iteration

    print(i)             # Only odd numbers less than 7 reach this line
