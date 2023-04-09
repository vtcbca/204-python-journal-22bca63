# write a program to check whether string is symmetrical or not.
def even(a): #function to check string is symmetrical or not.
    str=[]
    count=0
    for i in a:
        if(len(i)%2==0):
            str.append(i)
            count=count+1
    if(count>0):
        print(f'The number of even string is {count} and string :{str}')
    else:
        print("No even string available!")

a=[]
for i in range(5):
    b=input("Enter string:{i+1}:")
    a.append(b)    
even(a)    
