#Typecasting is the process of converting a variable from one data type
#to another. In pythonm we can use the factory functions int(), float(), str() to convert between data types.

name= "Augusto"
age= 32
height= 1.84
is_student= True

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))


#Typecasting
#String to Integer
age_str = "32"
age = int(age_str)
print(type(age))
print(age)

#String to Float
height_str = "1.84"
height = float(height_str)
print(type(height))
print(height)

#float to Integer
height_int = int(height)
print(type(height_int))
print(height_int)

#boolean

is_student_str = "True"
is_student = bool(is_student_str)
print(type(is_student))