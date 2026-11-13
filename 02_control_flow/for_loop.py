# for loop

# for i in range(1,6):
#     print(i)

# looping through list

# fruits = ['apple', 'banana', 'orange', 'mango']

# for fruit in fruits:
#     print(fruit)


# // break - immediatley terminates a loop //

# for number in range(1,11):
#     if number == 5:
#         break
#     print(number)


# // continue - skips the current iteration and moves to the next one ///

# for number in range(1,6):
#     if number == 3:
#         continue
#     print(number)


# looping thorugh a dictionary

# student = {
#     'name' : 'Anakin',
#     'age' : 22,
#     'course': 'Pyhon'
# }

# for key , value in student.items():
#     print(f'{key} : {value}')


# //////////// challenge1 ///////

# number_list = [10, 15, 20, 25, 30, 35]

# even = []
# odd = []

# for number in number_list:
#     if number == 25:
#             continue
#     elif number % 2 == 0:
#         even.append(number)
#     else:
#         odd.append(number)

# print(even)
# print(odd)

# enumerate()  lets us access both the index and value while looping through a sequence

fruits =['apple', 'banana', 'mango']

for index , fruit in enumerate(fruits):
    print(index , fruit)