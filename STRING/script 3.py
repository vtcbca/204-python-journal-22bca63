#Write a script to create a list with 5 string and count total number of string with even number of length with string using UDF
def count_even_strings(strings): #fuction defined
    	       even_count = 0
  	       even_strings = []
 	       for string in strings:
       		 if len(string) % 2 == 0:
           		 even_count += 1
          	                 even_strings.append(string)
  	  return even_count, even_strings

	strings = ["OM", "SAI", "RAMA"]
	even_count, even_strings = count_even_strings(strings)

	print("Strings with even number of characters:")
	for string in even_strings:
   	print(string)

	print(f"\nTotal string(s) of even number of characters: {even_count}")


