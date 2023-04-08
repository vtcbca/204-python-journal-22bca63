#Write a script to Replace list’s item with new value if found. Take value from user which you want to replace.

# Given list
list1 = [5, 10, 15, 20, 25, 50, 20]

# Take input from user for the value to replace and the new value
value_to_replace = int(input("Enter value you want to replace: "))
new_value = int(input("Enter value from which you want to replace: "))

# Iterate over each item in the list
for i in range(len(list1)):
    # Check if the item is equal to the value to replace
    if list1[i] == value_to_replace:
        # Replace the item with the new value
        list1[i] = new_value

# Print the updated list
print(list1)
