#Create a list of 5 value with filename and extension. Replace extension with".c" with ".py" and print new list.

filenames = ["program.c", "stdio.c", "sample.c", "a.py", "math.py", "hpp.py"]

# Iterate over each filename in the list
for i in range(len(filenames)):
    # Check if the filename ends with ".c"
    if filenames[i].endswith(".c"):
        # Replace ".c" with ".py"
        filenames[i] = filenames[i].replace(".c", ".py")

# Print the new list of filenames
print(filenames)
