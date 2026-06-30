# Open the file in read mode
with open("sample.txt", "r") as file:
    lines = file.readlines()     

line_count = len(lines)           

word_count = 0
for line in lines:
    words = line.split()          
    word_count += len(words)

print("Total Lines:", line_count)
print("Total Words:", word_count)