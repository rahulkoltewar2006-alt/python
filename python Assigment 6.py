Develop an application which asks the user to enter a string and prints its statistics as:
a) Number of Vowels
b) Number of Consonants
c) Number of Spaces
d) Number of Lowercase Letters

# Taking input from user
text = input("Enter a string: ")

# Initializing counters
vowels = 0
consonants = 0
spaces = 0
lowercase = 0

# Vowel list
vowel_list = "aeiouAEIOU"

# Loop through each character
for ch in text:
    
    if ch in vowel_list:
        vowels += 1
        
    elif ch.isalpha():   # checks if character is alphabet
        consonants += 1
        
    if ch == " ":
        spaces += 1
        
    if ch.islower():
        lowercase += 1

# Display results
print("Number of Vowels:", vowels)
print("Number of Consonants:", consonants)
print("Number of Spaces:", spaces)
print("Number of Lowercase Letters:", lowercase)
output:
Number of Vowels: 3
Number of Consonants: 7
Number of Spaces: 1
Number of Lowercase Letters: 8

Design a function that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized. Suppose the following input is supplied to the
program:
Practice makes perfect Then, the output should be: PRACTICE MAKES PERFECT

def capitalize_lines(lines):
    for line in lines:
        print(line.upper())

# Taking input
text = input("Enter a sentence: ")

# Converting input into a list (sequence of lines)
lines = [text]

# Calling function
capitalize_lines(lines)
output:
PRACTICE MAKES PERFECT