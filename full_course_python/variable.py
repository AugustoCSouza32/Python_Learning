###
# Variable = A container for a value (string,
# integer, float, boolean)
#            A variable behaves as if it was the value it contains
# ###

# Strings
first_name = "Augusto"
food = "Pizza"
email = "augusto.123@email.com"

# Integer
age = 32

#float
price = 9.99


# f-String
print(f"My names is {first_name} and I like {food}. I am {age} years old.\n You can contact me at {email}.")
print(f"The price of the {food} is ${price}.")


# Boolean
is_student = True

if is_student:
    print(f"{first_name} is a student.")
else:
    print(f"{first_name} is not a student.")