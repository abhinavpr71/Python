# While loop

# count = 1

# while count <= 5:
#     print(count)
#     count +=1


# count = 1

# while count  <= 10:
#     if count == 5:
#         break
#     print(count)
#     count +=1

# count = 0

# while count < 5:
#     count +=1

#     if count == 3:
#         continue
#     print(count)

# /////////// while loop with input //////////////

# password = ""

# while password != 'python123':
#     password =input('Enter password : ')
#     if password != 'python123':
#         print('Incorrect password')
# print('Access granted!')


# //  reverse a number //

# number = int(input('Enter a number : '))
# reversed_number = 0

# while number > 0:
#     digit = number % 10
#     reversed_number = reversed_number * 10 + digit
#     number = number // 10

# print(reversed_number)


# //// count digits in number /////

# number = int(input('Enter a number : '))

# digits_in_number = 0

# while number > 0:
#     number = number // 10
#     digits_in_number += 1
    
# if digits_in_number == 4:
#      print('Thousand')
# elif digits_in_number == 5:
#      print('Ten thousand')
# elif digits_in_number == 6:
#      print('Lakh')
# else:
#      print('value unknown')


# print(digits_in_number)


# // factorial ///

number = int(input('Enter a nubmer : '))

fact = 1

while number >= 1:
    fact = fact * number 
    number -= 1

print(f'Factorial : {fact}')