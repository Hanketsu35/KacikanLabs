# =============================================================================
# CENG113M - Lab 4 | Exercise 5: Guess the Number
# =============================================================================
# The program has a secret number (7). Keep asking the user to guess
# using a while loop. Print "Try again!" for wrong guesses,
# and "Correct!" when the user gets it right — then stop.
# =============================================================================

secret = 7                           # The hidden target number
flag = False
guess = int(input("Guess: "))        # Read the first guess before the loop

# Keep looping as long as the guess does not match the secret
while guess != secret:
    print("Try again!")
    guess = int(input("Guess: "))    # Ask again until the correct number is entered

#2
print("Correct!")
while flag == False:
    print("Try again!")
    guess = int(input("Guess: "))
    if guess == secret:
        flag = True
