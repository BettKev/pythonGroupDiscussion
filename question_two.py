# Implement a function that takes a list and returns True if the list is sorted in ascending order, otherwise False.

our_initial_list = [2, 6, 3, 2, 5, 12, 6, 1]

print(f"This is our initial list {our_initial_list}")

def sorted_list():
    our_sorted_list = sorted(our_initial_list, reverse=False)
    print(f"This is our sorted list {our_sorted_list}")

    if our_sorted_list == sorted(our_initial_list, reverse=False):
        print("True, list is sorted in ascending order.")
    else:
        print("False, list is sorted in descending order.")
    
sorted_list()


