#Write a python menu driven script to create 2d array of 5 student marks of 5 subject to perform following operation.

import numpy as np

# create a 2D array of student marks
marks = np.array([[50, 60, 70, 80, 90],
                  [70, 80, 90, 85, 95],
                  [60, 70, 80, 75, 85],
                  [80, 90, 95, 85, 90],
                  [75, 85, 80, 70, 95]])

while True:
    # display menu options
    print("\nMenu:")
    print("1. Print the minimum marks of each subject")
    print("2. Print the maximum marks of each subject")
    print("3. Print the average marks of each subject")
    print("4. Print the marks which are most repeated in each subject")
    print("5. Find the variance value for each subject marks")
    print("6. Print the total marks of each student")
    print("7. Exit")

    # ask the user for their choice
    choice = int(input("Enter your choice: "))

    # perform the selected operation
    if choice == 1:
        # minimum marks of each subject
        print("Minimum marks of each subject:")
        print(np.min(marks, axis=0))
    elif choice == 2:
        # maximum marks of each subject
        print("Maximum marks of each subject:")
        print(np.max(marks, axis=0))
    elif choice == 3:
        # average marks of each subject
        print("Average marks of each subject:")
        print(np.mean(marks, axis=0))
    elif choice == 4:
        # marks which are most repeated in each subject
        print("Marks which are most repeated in each subject:")
        for i in range(marks.shape[1]):
            values, counts = np.unique(marks[:,i], return_counts=True)
            max_count_index = np.argmax(counts)
            print(f"Subject {i+1}: {values[max_count_index]} (count: {counts[max_count_index]})")
    elif choice == 5:
        # variance value for each subject marks
        print("Variance value for each subject marks:")
        print(np.var(marks, axis=0))
    elif choice == 6:
        # total marks of each student
        print("Total marks of each student:")
        print(np.sum(marks, axis=1))
    elif choice == 7:
        # exit the program
        break
    else:
        # invalid choice
        print("Invalid choice. Please try again.") 
