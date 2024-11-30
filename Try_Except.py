try:
    x = int(input("Enter the number: "))
    if x > 0:
        print("Positive")
    else:
        print("Non-positive")
except ValueError:
    print("Please enter a valid number.")
