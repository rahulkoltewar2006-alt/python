Perform the following File Handling O 
a) Construct a program that reads a text file and writes its contents into a new text file with the same content,
but in uppercase.

# Open the input file in read mode
with open("input.txt", "r") as file1:
    data = file1.read()

# Convert content to uppercase
upper_data = data.upper()

# Open the output file in write mode
with open("output.txt", "w") as file2:
    file2.write(upper_data)

print("File content copied in uppercase successfully!")

Output:
HELLO RAHUL
WELCOME TO PYTHON PROGRAMMING

Develop an application using file handling to copy the contents of python script into another without including the comments. Ask the user about the source and destination file names. Print the content of the both the files.

# Function to remove comments from a line
def remove_comments(line):
    # Remove full-line comments
    if line.strip().startswith("#"):
        return ""
    
    # Remove inline comments
    if "#" in line:
        line = line.split("#")[0]
    
    return line


# Taking file names from user
source = input("Enter source file name: ")
destination = input("Enter destination file name: ")

try:
    # Open source file
    with open(source, "r") as file1:
        lines = file1.readlines()

    # Process and write to destination file
    with open(destination, "w") as file2:
        for line in lines:
            clean_line = remove_comments(line)
            if clean_line.strip() != "":
                file2.write(clean_line + "\n")

    print("\nContent copied without comments successfully!\n")

    # Display source file content
    print("----- Source File Content -----")
    with open(source, "r") as file1:
        print(file1.read())

    # Display destination file content
    print("----- Destination File Content -----")
    with open(destination, "r") as file2:
        print(file2.read())

except FileNotFoundError:
    print("Error: Source file not found!")

Output:
print("Hello")
a = 10
print(a)