#Write a Python program to enter sentence of atleast 10 words. Take user input of lengtho of word. 

# Take input string from the user
input_string = input("Enter a sentence of at least 10 words: ")

# Take input word length from the user
min_length = int(input("Enter the minimum word length: "))

# Split the input string into words
words = input_string.split()

# Create a dictionary of words that have length >= min_length
result_dict = {}
for word in words:
    if len(word) >= min_length:
        result_dict[word] = len(word)

# Print the resulting dictionary
print(result_dict)
