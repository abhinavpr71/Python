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

password = ""

while password != 'python123':
    password =input('Enter password : ')
    if password != 'python123':
        print('Incorrect password')
print('Access granted!')