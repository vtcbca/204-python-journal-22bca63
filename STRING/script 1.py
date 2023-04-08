#Write a script to enter any word and check it is palindrom or not.
#program to check whether number is reverse or not.
a=input("enter a string:")
b=a[::-1] #reverse string
if(a==b):
	print('{} is a palindrom word'.format(a))
else:
	print('{} is a  not palindrom word'.format(a))
