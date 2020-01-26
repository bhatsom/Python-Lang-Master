# dictionary is equivalent to Map in Java

student = {'name': 'John Doe', 'age': 25, 'courses': ['Math', 'CompSci']}

# values can by retrieved using get function
print('student={}'.format(student))
print('student name={}'.format(student.get('name')))
print('student age={}'.format(student.get('age')))
print('student courses={}'.format(student.get('courses')))
print('student is enlisted for Math={}'.format('Math' in student.get('courses')))
print('student is enlisted for Biology={}'.format('Biology' in student.get('courses')))
print("-----------------------------------------------------------------------")
# values can also be retrieved using []
print('student name={}'.format(student['name']))
print('student courses={}'.format(student['courses']))
print("-----------------------------------------------------------------------")
# accessing val using [] for a key that doesn't exist gives KeyError
#print('student phone #: {}'.format(student['phone']))

# accessing val using GET for a key that doesn't exist returns None - NO Error
print('student phone using get#: {}'.format(student.get('phone')))

# using default value if the key doesnt exist
print('student phone using default value#: {}'.format(student.get('phone', 'Not Found')))
print("-----------------------------------------------------------------------")
# add phone number
student['phone'] = '123-456-7777'
print('student phone #: {}'.format(student['phone']))

# update or add multiple keys at a time
student.update({'name': 'Jane Davies', 'id': '101'})
print(student)
print("-----------------------------------------------------------------------")
# now lets delete student's age
del student['age']
print(student)

# now lets delete student's phone using pop (deletes the entry and returns the value if key exists)
phone = student.pop('phone')
print('deleted phone#: {} from student info'.format(phone))
print(student)
print("-----------------------------------------------------------------------")
# size of the dictionary - usign 'len(dictionary)'
print('Number of Keys={}'.format(len(student)))

# all keys or all values
print('all keys= {}'.format(student.keys()))
print('all values= {}'.format(student.values()))

# all items or entries
print('all items= {}'.format(student.items()))
