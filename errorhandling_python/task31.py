valid = False

while valid == False:
    try:
        number = int(input("Enter a number: "))
        print("You entered:", number)
        valid = True
    except ValueError:
        print("Invalid input! Please enter a number.")