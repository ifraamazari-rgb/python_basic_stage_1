
name = input("Enter your name: ")

with open("contacts.txt", "a") as file:
    file.write(name + "\n")

print("Name added successfully!")