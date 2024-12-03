#Write a Python program to print all numbers between two user-provided integers, skipping numbers divisible by 7.

def print_numbers_skipping_sevens(start, end):
    print(f"Numbers between {start} and {end}, skipping multiples of 7:")
    for num in range(start, end + 1):
        if num % 7 != 0:
            print(num, end=" ")
    print()  # Newline for cleaner output

# Get input from the user
try:
    start = int(input("Enter the starting integer: "))
    end = int(input("Enter the ending integer: "))
    print_numbers_skipping_sevens(start, end)
except ValueError:
    print("Please enter valid integers.")
