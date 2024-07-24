# Task 1, 2, & 3

def add_item_to_list(user_list):
    item = input("Enter an item to add to the list: ")
    user_list.append(item)
    print(f"{item} has been added to the list.")

def remove_item_from_list(user_list):
    if not user_list:
        print("The list is empty. Nothing to remove.")
        return
    
    print("Current list:", user_list)
    item_to_remove = input("Enter the item to remove from the list: ")
    
    if item_to_remove in user_list:
        user_list.remove(item_to_remove)
        print(f"{item_to_remove} has been removed from the list.")
    else:
        print(f"{item_to_remove} is not in the list.")

def print_list(user_list):
    if not user_list:
        print("The list is empty.")
    else:
        print("Current list:")
        for item in user_list:
            print(item)

# Example usage:
my_list = []

while True:
    print("\nOptions:")
    print("1. Add item to list")
    print("2. Remove item from list")
    print("3. Print current list")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        add_item_to_list(my_list)
    elif choice == '2':
        remove_item_from_list(my_list)
    elif choice == '3':
        print_list(my_list)
    elif choice == '4':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")
