
import os


# =============================================================================
# EX 04 - read() + split
# =============================================================================

with open("temperatures.txt", "r") as f:
    content = f.read()

hottest_city = ""
hottest_temp = -1

for line in content.split("\n"):
    city, temp = line.split(":")
    if int(temp) > hottest_temp:
        hottest_temp = int(temp)
        hottest_city = city

print("Hottest city:", hottest_city)


# =============================================================================
# EX 05 - for line in f
# =============================================================================

count = 0

with open("words.txt", "r") as f:
    for line in f:
        word = line.strip()
        if len(word) > 5:
            print(word)
            count += 1

print("Advanced word count:", count)


# =============================================================================
# EX 06 - write mode ("w")
# =============================================================================

items = ["keyboard", "monitor", "mouse", "headset", "webcam"]

lines = []
for i, item in enumerate(items):
    lines.append(f"{i + 1}. {item}")

with open("inventory.txt", "w") as f:
    f.write("\n".join(lines))


# =============================================================================
# EX 07 - append mode ("a")
# =============================================================================

status = "ok"  # try "error" to test the other branch

if os.path.exists("server_log.txt"):
    with open("server_log.txt", "r") as f:
        entry_number = len(f.read().splitlines()) + 1
else:
    entry_number = 1

if status == "ok":
    message = f"[{entry_number}] Server started\n"
else:
    message = f"[{entry_number}] Error detected\n"

with open("server_log.txt", "a") as f:
    f.write(message)


# =============================================================================
# EX 08 - Read -> Filter -> Write
# =============================================================================

with open("scores.txt", "r") as f:
    scores = [int(line.strip()) for line in f if line.strip()]

passed = [s for s in scores if s >= 50]
failed = [s for s in scores if s < 50]

with open("passed.txt", "w") as f:
    f.write("\n".join(str(s) for s in passed))

with open("failed.txt", "w") as f:
    f.write("\n".join(str(s) for s in failed))

print("passed.txt:")
with open("passed.txt", "r") as f:
    for line in f:
        print(line.strip())

print("failed.txt:")
with open("failed.txt", "r") as f:
    for line in f:
        print(line.strip())


# =============================================================================
# EX 09 - os module: setup
# =============================================================================

if os.path.exists("config.txt"):
    with open("config.txt", "r") as f:
        print(f.read())
else:
    with open("config.txt", "w") as f:
        f.write("theme=dark\nvolume=80\n")

if not os.path.exists("output"):
    os.mkdir("output")

for item in os.listdir("."):
    print(item)


# =============================================================================
# EX 10 - os module: cleanup
# =============================================================================

for i in range(1, 6):
    with open(f"temp_{i}.txt", "w") as f:
        f.write("temporary")

print("Before cleanup:")
for item in os.listdir("."):
    print(item)

for filename in os.listdir("."):
    if filename.startswith("temp_"):
        os.remove(filename)

print("After cleanup:")
for item in os.listdir("."):
    print(item)


# =============================================================================
# BONUS - Notes app
# =============================================================================

if not os.path.exists("notes"):
    os.mkdir("notes")

title = input("Note title: ")
filepath = f"notes/{title}.txt"

if os.path.exists(filepath):
    print("Existing note:")
    with open(filepath, "r") as f:
        for line in f:
            print(line.strip())

if os.path.exists(filepath):
    with open(filepath, "r") as f:
        entry_number = len(f.read().splitlines()) + 1
else:
    entry_number = 1

new_entry = input("New entry: ")

with open(filepath, "a") as f:
    f.write(f"[{entry_number}] {new_entry}\n")

print("All notes:")
for filename in os.listdir("notes"):
    print(filename)

to_delete = input("Delete a note? (leave blank to skip): ")
if to_delete:
    delete_path = f"notes/{to_delete}.txt"
    if os.path.exists(delete_path):
        os.remove(delete_path)
        print(f"{to_delete}.txt deleted.")
    else:
        print("File not found.")
