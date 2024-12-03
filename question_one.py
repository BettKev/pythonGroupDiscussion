# Write a function that takes a list of numbers and returns a new list with only the unique numbers from the original list.(list methods)

our_initial_list = [2, 6, 3, 2, 5, 12, 6]

# print(f"This is our initial list {our_initial_list}")

def new_unique_list():
    new_list = set(our_initial_list)
    print(f"This is our new list {new_list}")

new_unique_list()
