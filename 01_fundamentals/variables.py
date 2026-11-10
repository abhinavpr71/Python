# VARIABLES

age = 22 #int
height = 165.5 #float
name = "Lui" #string
is_learning = True #Boolean

#type checking
print(type(age)) 
print(type(height))
print(type(name))
print(type(is_learning))

#type conversion - changing a value from one data type to antoher.
print(int('25'))  

first_num = int(input('Enter First number : '))
second_num = float(input("Enter Second number : "))

print(type(first_num))
print(type(second_num))

total = first_num + second_num
total = str(total)
print(total)
print(type(total))
