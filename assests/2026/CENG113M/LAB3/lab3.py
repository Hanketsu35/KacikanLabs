# ==========================================
# CENG 113M - LAB 3: SOLUTIONS FOR TA
# Topic: Conditions (if, elif, else)
# ==========================================

print("--- MINI-QUIZ ANSWERS ---")
# Mini-Quiz 1
# 1. int(5.4) -> 5
# 2. float("3") -> 3.0
# 3. int("70") + int("3") -> 73
# 4. str(2 + 3) -> "5"

# Mini-Quiz 2
# 1. 5 > 3 -> True
# 2. not True -> False
# 3. 3.0 == 2 + 1 -> True
# 4. 3 < 4 and '5' == 5 -> False (string is not equal to int)
# 5. False or True -> True


# ==========================================
print("\n--- EXERCISE 1: The Discount ---")
amount = float(input("Enter your shopping amount: "))

if amount > 1000:
    amount = amount - 100  # Apply the flat discount

print("Final amount to pay:", amount)


# ==========================================
print("\n--- EXERCISE 2: Even or Odd? ---")
num = int(input("Enter an integer: "))

if num % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")


# ==========================================
print("\n--- EXERCISE 3: Absolute Value ---")
val = int(input("Enter a number: "))

if val < 0:
    print("Absolute value:", val * -1)
else:
    print("Absolute value:", val)


# ==========================================
print("\n--- EXERCISE 4: Piecewise Function ---")
x = float(input("Enter x: "))

if x < 0:
    result = x ** 2
elif x < 10:            # We don't need 'x >= 0 and x < 10' because x < 0 is already handled above!
    result = x
else:
    result = x ** 0.5   # Square root

print("f(x) =", result)


# ==========================================
print("\n--- EXERCISE 5: Coffee Shop Order (Sequential) ---")
price = 50

milk = input("Do you want extra milk? (y/n): ")
if milk == "y" or milk == "Y":
    price = price + 10

syrup = input("Do you want syrup? (y/n): ")
if syrup == "y" or syrup == "Y":
    price = price + 15

print("Final total price:", price, "TL")


# ==========================================
print("\n--- EXERCISE 6: Bank Loan System (Nested) ---")
age = int(input("Enter your age: "))

if age < 18:
    print("Loan rejected. You must be 18 or older.")
else:
    # This block only runs if they are 18 or older
    income = float(input("What is your monthly income? "))
    
    if income > 20000:
        print("Loan approved!")
    else:
        print("Loan requires a guarantor.")


# ==========================================
print("\n--- EXERCISE 7: Triangle Validator (AND) ---")
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    print("Valid Triangle")
else:
    print("Invalid Triangle")


# ==========================================
print("\n--- EXERCISE 8: The Cartesian Plane ---")
x = float(input("Enter x coordinate: "))
y = float(input("Enter y coordinate: "))

if x == 0 and y == 0:
    print("Origin")
elif x == 0:
    print("On the Y-axis")
elif y == 0:
    print("On the X-axis")
elif x > 0 and y > 0:
    print("Quadrant I")
elif x < 0 and y > 0:
    print("Quadrant II")
elif x < 0 and y < 0:
    print("Quadrant III")
else: # Automatically implies x > 0 and y < 0
    print("Quadrant IV")


# ==========================================
print("\n--- EXERCISE 9: Quadratic Equation Solver ---")
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

delta = (b ** 2) - (4 * a * c)

if delta > 0:
    root1 = (-b + (delta ** 0.5)) / (2 * a)
    root2 = (-b - (delta ** 0.5)) / (2 * a)
    print("Two real roots:", root1, "and", root2)
elif delta == 0:
    root = -b / (2 * a)
    print("One real root:", root)
else:
    print("No real roots exist.")


# ==========================================
print("\n--- EXERCISE 10: Sorting 3 Numbers (Pure Logic) ---")
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))

if n1 <= n2 and n1 <= n3:
    # n1 is the smallest
    if n2 <= n3:
        print("Ascending order:", n1, n2, n3)
    else:
        print("Ascending order:", n1, n3, n2)

elif n2 <= n1 and n2 <= n3:
    # n2 is the smallest
    if n1 <= n3:
        print("Ascending order:", n2, n1, n3)
    else:
        print("Ascending order:", n2, n3, n1)

else:
    # n3 is the smallest
    if n1 <= n2:
        print("Ascending order:", n3, n1, n2)
    else:
        print("Ascending order:", n3, n2, n1)


# ==========================================
print("\Exercise 11: The Leap Year ---")
year = int(input("Enter a year: "))

# SOLUTION 1: Nested Ifs (Translating the algorithm step by step)
print("Result using Nested Ifs:")
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year")
        else:
            print("Not a Leap Year")
    else:
        print("Leap Year")
else:
    print("Not a Leap Year")


# SOLUTION 2: Single Complex Condition (Advanced)
print("Result using single complex condition:")
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")