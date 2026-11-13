# # If, elif, else

# age = 20

# if age >= 18:
#     print("Eligible to vote")
# elif age >= 16:
#     print("Not eligible, but close")
# else:
#     print("Not eligible")


# # Multiple conditions

# marks = 85

# if marks >= 90:
#     print("Grade A+")
# elif marks >= 75:
#     print("Grade A")
# elif marks >= 60:
#     print("Grade B")
# else:
#     print("Needs improvement")


# # Logical operators

# username = "admin"
# password = "1234"

# if username == "admin" and password == "1234":
#     print("Login successful")
# else:
#     print("Invalid credentials")


# # Nested if

# number = 10

# if number > 0:
#     if number % 2 == 0:
#         print("Positive even number")
#     else:
#         print("Positive odd number")
# else:
#     print("Zero or negative")


# ////////////// match-case //////////////////

# build a simple atm menu using match-case

option = int(input('Enter an option (1,2,3,4) : '))

match option:
    case 1 :
        print('1.Check balance')
    case 2:
        print('2.Deposit money')
    case 3 :
        print('3.Withdraw money')
    case 4:
        print('4.Exit')
    case _:
        print('Invalid option!!!')