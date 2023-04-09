#WAS to create list using UDF createList(). Count and Print even and odd number in the list using UDF evenOdd().


def createList():
    # This function creates and returns a list of numbers
    # You can modify this function to create your own list
    return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def evenOdd(lst):
    # This function takes a list as input and counts and prints even and odd numbers
    even_count = 0
    odd_count = 0
    
    for num in lst:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    
    print("Number of even numbers:", even_count)
    print("Number of odd numbers:", odd_count)

# Create a list using the createList() function
myList = createList()

# Call the evenOdd() function with the created list as input
evenOdd(myList)
