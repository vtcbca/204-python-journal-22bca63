#Write a script to create dictionary from list which contain student id , name and percentage

# Initialize an empty list to store student details
student_list = []

# Take input from user for student details
while True:
    student_id = int(input("Enter student ID: "))
    student_name = input("Enter student name: ")
    student_percentage = float(input("Enter student percentage: "))
    
    # Add student details to the list
    student_list.append(student_id)
    student_list.append(student_name)
    student_list.append(student_percentage)
    
    choice = input("Do you want to enter details for more students? (Yes=Y/y, No=N/n): ")
    if choice.lower() == "n":
        break

# Create a dictionary from the list
student_dict = {}
for i in range(0, len(student_list), 3):
    student_dict[student_list[i]] = [student_list[i+1], student_list[i+2]]

# Print the list and dictionary
print("List:", student_list)
print("Dictionary:", student_dict)
