# =============================================================================
# CENG113M - Lab 4 | Exercise 7: Sum Until Zero
# =============================================================================
# Keep asking the user to enter a number and add it to a running total.
# When the user enters 0, stop the loop and print the total.
# Note: Do NOT add 0 to the total — stop before adding it.
# =============================================================================

total = 0                                 # Accumulator for the sum

while True:                               # Loop indefinitely until we hit break
    number = int(input("Enter a number: "))

    if number == 0:                       # 0 is the sentinel value — stop here
        break                             # Exit the loop without adding 0

    total = total + number                # Add the valid number to the running total

print(f"Total: {total}")
