name = input("What is a name: ")

# 1. Append to the file
with open("names.txt", "a") as file:
    file.write(f"{name}\n")

# 2. Read the file
print("\nHere are all the names in the file:")

with open("names.txt", "r") as file:
    for i, line in enumerate(file):
        print(f"{i+1}. {line.strip()}")
