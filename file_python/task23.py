import json

# Create a dictionary
student = {
    "name": "Ali",
    "age": 20,
    "course": "Python"
}


with open("student.json", "w") as file:
    json.dump(student, file)
with open("student.json", "r") as file:
    data = json.load(file)
print(data)