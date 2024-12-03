def main():
    """Collect 5 numbers from the user and calculate the maximum."""
    max_value = None  # Variable to store the maximum value

    for i in range(1, 6):
        # Prompt the user for input
        user_input = input(f"Enter number {i}: ")

        # Ensure the input is valid (numeric only)
        while not user_input.replace('.', '', 1).isdigit() and not (user_input.startswith('-') and user_input[1:].replace('.', '', 1).isdigit()):
            print("Invalid input. Please enter a numeric value.")
            user_input = input(f"Enter number {i}: ")

        # Convert input to a number
        num = float(user_input)

        # Update max_value if it's the first number or larger than the current max
        if max_value is None or num > max_value:
            max_value = num

    # Display the result
    print(f"The maximum value is: {max_value}")

# Run the program
if __name__ == "__main__":
    main()
