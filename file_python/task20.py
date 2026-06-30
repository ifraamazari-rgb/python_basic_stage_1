
with open("sample.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("Welcome to Python File Handling.\n")
    file.write("This is the third line.\n")


with open("sample.txt", "r") as file:
    content = file.read()


print("File Content:")
print(content)