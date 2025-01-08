def calculate_square(n):
    """Return the square of the given number n."""
    return n * n

def main():
    while True:
        try:
            user_input = int(input("Please enter a positive integer: "))
            if user_input > 0:
                break
            else:
                print("The number must be positive. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid positive integer.")
    result = calculate_square(user_input)
    print(f"The square of {user_input} is {result}.")

if __name__ == "__main__":
    main()