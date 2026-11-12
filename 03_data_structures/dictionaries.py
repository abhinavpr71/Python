# # DICTIONARIES - key/value pairs

# student = {
#     'name' : 'Anakin',
#     'age' : 22,
#     'course' : 'pyhton'
# }

# # print(student)

# # print(student['age'])
# # print(student['course'])
# # print(student['name'])

# # student['age'] = 23

# # student['city'] = 'Kerala'


# # student.pop('age')

# # print(student)

# # print('name' in student)
# # print('age' in student)

# # print(student.keys())
# # print(student.values())
# # print(student.items())

# for key , value in student.items():
#     print(f'{key} : {value}')


# ///////// Nested Dictionary ///////////////

students = {
    'student1': {
        'name' : 'Alex',
        'age' : 22
    },
    'student2': {
            'name' : 'John',
            'age' : 24
        }
}

print(students['student1']['name'])