Develop a Python program that takes a voltage (V) and resistance (R) as inputs from the user and calculates the
current (I) using Ohm’s Law.

# Take input from the user
voltage = float(input("Enter Voltage (V): "))
resistance = float(input("Enter Resistance (R in ohms): "))

# Check to avoid division by zero
if resistance == 0:
    print("Resistance cannot be zero.")
else:
    current = voltage / resistance
    print("Current (I) =", current, "Amperes")

Modify the above program to display the nature of current:
If current &lt; 0.5 A, print “Low current”
If 0.5 A ≤ current ≤ 2 A, print “Normal current”
If current &gt; 2 A, print “High current
# Take input from the user
voltage = float(input("Enter Voltage (V): "))
resistance = float(input("Enter Resistance (R in ohms): "))

# Check for division by zero
if resistance == 0:
    print("Resistance cannot be zero.")
else:
    current = voltage / resistance
    print("Current (I) =", current, "Amperes")

    # Determine nature of current
    if current < 0.5:
        print("Low current")
    elif 0.5 <= current <= 2:
        print("Normal current")

        In a steel plant, the quality of steel is graded according to the following conditions:
(i) Hardness must be greater than 50
(ii) Carbon content must be less than 0.7
(iii) Tensile strength must be greater than 5600
The grades are as follows:
Grade is 10 if all three conditions are met
Grade is 9 if conditions (i) and (ii) are met
Grade is 8 if conditions (ii) and (iii) are met
Grade is 7 if conditions (i) and (iii) are met
Grade is 6 if only one condition is met
Grade is 5 if none of the conditions are met
Construct a program, which will require the user to give values of hardness, carbon content and tensile strength of
the steel under consideration and output the grade of the steel.


# Taking input from the user
hardness = float(input("Enter Hardness: "))
carbon = float(input("Enter Carbon Content: "))
tensile = float(input("Enter Tensile Strength: "))

# Checking the conditions
cond1 = hardness > 50
cond2 = carbon < 0.7
cond3 = tensile > 5600

# Determining the grade
if cond1 and cond2 and cond3:
    grade = 10
elif cond1 and cond2:
    grade = 9
elif cond2 and cond3:
    grade = 8
elif cond1 and cond3:
    grade = 7
elif cond1 or cond2 or cond3:
    grade = 6
else:
    grade = 5

# Display result
print("The grade of the steel is:", grade)