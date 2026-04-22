# ==========================================
# CENG113M - Lab 5 Solutions
# Sequences: Strings and Lists 
# (Applied Math & Data Science Edition)
# ==========================================

print("--- Exercise 1: Protocol Decryption ---")
message = input("Enter message: ")
# Remove extra spaces from ends
cleaned_msg = message.strip()

# Check protocol and process
if cleaned_msg.startswith("ENC-"):
    # Remove the prefix and convert to lowercase
    secret = cleaned_msg.replace("ENC-", "").lower()
    print("Secret:", secret)
else:
    print("Invalid protocol")
print()


print("--- Exercise 2: Dataset File Formatter ---")
filename = input("Enter filename: ")

# Replace spaces with underscores
safe_filename = filename.replace(" ", "_")

# Find where the extension starts
dot_index = safe_filename.find(".")
print("Dot found at index:", dot_index)

# Check CSV format and fix if necessary
is_csv = safe_filename.endswith(".csv")
print("Is CSV:", is_csv)

if not is_csv:
    # Add .csv using string concatenation (+)
    safe_filename = safe_filename + ".csv"

print("Safe format:", safe_filename)
print()


print("--- Exercise 3: Equation Parser ---")
equation = input("Enter equation: ")

# Remove spaces and make uppercase
clean_eq = equation.replace(" ", "").upper()

# Count occurrences of 'X'
x_count = clean_eq.count("X")
print("Variable 'X' count:", x_count)

# Split into LHS and RHS if '=' is present
if "=" in clean_eq:
    parts = clean_eq.split("=")
    print("LHS:", parts[0])
    print("RHS:", parts[1])
else:
    print("Not an equation (no '=' found).")
print()


print("--- Exercise 4: Cryptographic Key Generator ---")
base_key = ["A", "F", "1"]
n = int(input("Enter multiplier N: "))

# Multiply the list
full_key_list = base_key * n

# Join elements with a hyphen
final_key = "-".join(full_key_list)
print("Generated Key:", final_key)
print()


print("--- Exercise 5: Statistical Mean ---")
samples = []
total_sum = 0.0

for i in range(5):
    val = float(input(f"Enter sample {i+1}: "))
    samples.append(val)
    total_sum = total_sum + val

mean = total_sum / 5
print("Dataset:", samples)
print("Mean:", mean)
print()


print("--- Exercise 6: Binary Dominance ---")
signal = ["1", "0", "1", "1", "0", "0", "1"]

# Use list count method
high_count = signal.count("1")
low_count = signal.count("0")

print("High bits:", high_count)
print("Low bits:", low_count)

if high_count > low_count:
    print("Signal is High dominant")
elif low_count > high_count:
    print("Signal is Low dominant")
else:
    print("Balanced")
print()


print("--- Exercise 7: Scalar Multiplication ---")
vector = [10, -5, 4, 0]
k = int(input("Enter scalar k: "))

new_vector = []
for x in vector:
    new_vector.append(x * k)

print("Scaled vector:", new_vector)
print()


print("--- Exercise 8: The Telemetry Queue ---")
telemetry = [45.2, 46.1, -999.0, 45.8, 1]

# pop() removes and returns the last element
status = telemetry.pop()
print("Status Code:", status)

# Find the index of the error
error_idx = telemetry.index(-999.0)
print("Error found at index:", error_idx)

# remove() deletes the specific value
telemetry.remove(-999.0)

print("Cleaned Telemetry:", telemetry)
print()


print("--- Exercise 9: Sorting the Leaderboard ---")
scores = [450, 120, 890, 340, 999, 210]

# Sort ascending, then reverse to make it descending
scores.sort()
scores.reverse()

print("Standings:", scores)
print("Champion:", scores[0])
print()


print("--- Exercise 10: Matrix Homogeneous Coordinates ---")
vector = [4.5, 3.2]
new_dimensions = [7.1, 2.8]

# extend() adds multiple elements to the end
vector.extend(new_dimensions)

# insert() adds an element at a specific index
vector.insert(0, 1.0)

print("Transformed Vector:", vector)
print()


print("--- Exercise 11: Set Theory & Memory Wipe ---")
my_set = []

for i in range(4):
    coord = input("Enter coordinate name: ")
    # Enforce uniqueness
    if coord not in my_set:
        my_set.append(coord)

# Make a backup using copy()
backup = my_set.copy()

# Wipe the original using clear()
my_set.clear()

print("Backup Set:", backup)
print("Wiped Original:", my_set)
print()