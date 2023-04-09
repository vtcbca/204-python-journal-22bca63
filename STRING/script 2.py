#Write a script to enter any sentence and print those word which is palindrom. Also print total number of palindrom word.
def p_palindrome(word):#fuction for reversing
    return word == word[::-1]

def a_palindromes(sentence):#fuction 
    palindromes = []
    words = sentence.split()
    for word in words:
        if p_palindrome(word):
            palindromes.append(word)
    return palindromes

sentence = input("Enter a sentence: ")
palindromes = a_palindromes(sentence)
count = len(palindromes)

if count > 0:
    print("Palindrome words in the sentence:")
    for word in palindromes:
        print(word)
    print(f"\nTotal {count} palindrome word(s) in string: {palindromes}")
else:
    print("No palindrome words found in the sentence.")
