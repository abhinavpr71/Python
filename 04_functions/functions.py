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

# def calculate(a,b):
#     return a+ b , a- b

# sum , difference = calculate(12,4)

# print(sum)
# print(difference)

# def calcualtor():
#         try :
#             num1 = int(input('Enter num1 : '))
#             num2 = int(input('Enter num2 : '))
#         except ValueError:
#                 return "Invalid input!"
#         operation = input('Enter operation (+ , - , / , *): ')

#         if operation == "+":
#             sum = num1 + num2
#             return sum
#         elif operation == "-":
#             difference = num1 - num2
#             return difference
#         elif operation == "*":
#             product = num1 * num2
#             return product
#         elif operation == "/":
#             if num2 == 0:
#                 return '0 denominator is not allowed.Enter input again!'
#             else: 
#                 quotient = num1 / num2
#                 return quotient
#         else:
#             return 'Invalid operator'

# print(calcualtor())

# def test():
    # x = 10        ## //// local scope = a variable defined inside function only accessable inside that function ////////
#     print(x)

# test()
# print(x)

# ////////// NESTED FUNCTION //////////////

# a function defined inside another function

# def greet():
#     def message():
#         print('Welcome to python!!')

#     message()

# greet()

def calculate_price(price):
    def apply_discount():
        discount = price - (price / 10)
        return discount
    
    return apply_discount() 
    

reuslt = calculate_price(70)
print(reuslt)