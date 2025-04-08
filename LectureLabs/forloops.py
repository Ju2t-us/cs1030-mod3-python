# Loop through numbers 0 to 4
for i in range(5):
    # Print the current number
    print(i)
print("----")
#Loop through numbers 2 to 5
for i in range(2,6):
    # Print the current number
    print(i)
print("----")
#Loop through numbers 2 to 10 with a step of 2
for i in range (2, 10, 2):
    # Print the current number
    print(i)

#ask for input from the user and set it to the variable "number"
number = int(input("\nEnter your number: "))

#loop through the range of 0 to 10, printing out their chosen number multiplied by the current number in the loop
for i in range(11):
    print(number, "x", i, "=", number * i)