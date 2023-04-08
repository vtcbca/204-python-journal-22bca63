
# write a menu driven program to peform list operation.
def create_list(): #fuction for creating list
    strings = []
    n = int(input("Enter the number of strings you want to add to the list: "))
    for i in range(n):
        string = input("Enter string {i+1}: ")
        strings.append(string)
    return strings

def print_even_strings(strings):#function string with even character length
    even_strings = []
    for string in strings:
        if len(string) % 2 == 0:
            even_strings.append(string)
    if len(even_strings) > 0:
        print("Strings with even character length:")
        for string in even_strings:
            print(string)
    else:
        print("No strings with even character length found in the list.")

def replace_odd_chars(strings): #function for replace odd character of string with index no.
    new_strings = []
    for string in strings:
        new_string = ""
        for i in range(len(string)):
            if i % 2 == 0:
                new_string += string[i]
            else:
                new_string += str(i)
        new_strings.append(new_string)
    return new_strings

def extract_chars(strings, start, end):  #fuction for enter start and end character and extract character from the list of string.
    extracted_chars = []
    for string in strings:
        extracted_chars.append(string[start:end])
    return extracted_chars

# Main program
print("Menu:")
print("""1. Create list of strings
         2. Print strings with even character length
         3. Replace odd characters in strings with their index
         4. Extract characters from the list of strings""")

strings = []

while True:
    choice = int(input("Enter your choice (1-4): "))
    if choice == 1:
        strings = create_list()
    elif choice == 2:
        print_even_strings(strings)
    elif choice == 3:
        new_strings = replace_odd_chars(strings)
        print("Strings with odd characters replaced with their index:")
        for string in new_strings:
            print(string)
    elif choice == 4:
        start = int(input("Enter the starting index: "))
        end = int(input("Enter the ending index: "))
        extracted_chars = extract_chars(strings, start, end)
        print("Extracted characters from the list of strings:")
        for chars in extracted_chars:
            print(chars)
    else:
        print("Invalid choice. Please try again.")
