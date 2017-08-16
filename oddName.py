"""Joshua Gale"""
second_letter_name = ""
name = input("What is your name: ")
while name == "":
    print("Please enter a valid name: ")
    name = input("What is your name: ")

for char in range(len(name)):
    if char % 2 == 1:
        second_letter_name += name[char]

print(second_letter_name)
