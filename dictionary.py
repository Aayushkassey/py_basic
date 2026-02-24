#Creation 

student={
    'name': 'John Doe',
    'age': 20,
    'roll_no': 101,
}

#Accessing values
print(student.get('Name', 'not found'))  # Output: John Doe

#updating values
student['name'] = 'Jane Doe'
student['age'] = 21

student['contact'] = '123-456-7890'  # Adding a new key-value pair
print(student)

'''#delete
del student['name']
print(student.pop('age'))  # Output: 21
print(dir(student))  # Print all available methods for the student dictionary
print(student)'''

# for  _, values in student.items():
#     print(_,values)


# for i in student.items():
#     print(type(i))

print(type(student.keys()))  # Output: <class 'dict_keys'>
print(type(student.values()))  # Output: <class 'dict_values'>
print(type(student.items()))  # Output: <class 'dict_items

