# input() = A function that prompts the user to enter data
#           Returns the entered data as a string


name = input("Enter your name: ")
age = input("How old are you? ")

# age = age + 1 TypeError: concatenate str with integer.
age = int(age)
age = age + 1

print(f"Your name is {name}")
print(f"You are {age} years old.")