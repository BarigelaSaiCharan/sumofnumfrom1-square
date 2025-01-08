while True:
    try:
        num = int(input("Please enter a positive integer: "))
        if num > 0:
            break
        else:
            print("The number must be positive. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid positive integer.")
result = num * num
print(f"The square of {num} is: {result}")