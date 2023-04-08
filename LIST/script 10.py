#wriate a script to check if the list contains three consecutive common numbers in Python using udf.

# Define a function to check if the list contains three consecutive common numbers
def cheak_num(lst):
    for i in range(len(lst)-2):
        if lst[i] == lst[i+1] == lst[i+2]:
            return lst[i]
    return None

# Example list
lst = [4, 5, 5, 5, 3, 8]

# Call the function and print the output
result = check_num(lst)
if result:
    print("Output:", result)
else:
    print("List does not contain three consecutive common numbers.")
Footer
© 2023 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
