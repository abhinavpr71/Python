# FUNCTIONS - a functions is a resusable block of code that performs a specific task

# def greet(name):                       # parameters allow functions to recieve data.Here name is a parameter.
#     print(f'Hello, {name}')

# greet('Alex')  # Alex and Sam are Arguments
# greet('Sam') 

# name = input('Enter your name : ')
# age = int(input('Enter your age : '))

# def introduce(name , age = None):
#     if age is None:
#         return 'Age not provided'
#     else:
#         f'Hello my name is "{name}" and im {age} years old.'

# print(introduce(name='Anakin',age= 20))

# def add(a,b):
#     return a + b

# result = add(12, 8) 

# result = result * 2
# print(result)

def calculate(a,b):
    return a+ b , a- b

sum , difference = calculate(9,10)

print(sum)
print(difference)