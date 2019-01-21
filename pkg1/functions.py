# define an empty function

def emptyFunc():
    pass

emptyFunc()

print(emptyFunc)
print(emptyFunc())

print("---------------------------Function with default value--------------------------------------------")
def greetingFunc(greeting, name='You'):
    return '{} {}'.format(greeting, name)

print('Hi. {}'.format(greetingFunc('John')))
print('Hi. {}'.format(greetingFunc('John', 'Welcome!')))

print("-----------------------------------------------------------------------")
def studentInfo(*args, **kwargs):
    print(args)
    print(kwargs)

studentInfo('Math', 'CompSci', name='John', age=22)
#studentInfo('Math', 'CompSci', 'name': 'John', 'age': 22) # SyntaxError
print("-----------------------------------------------------------------------")
courses = ['Math', 'CompSci']
info = {'name': 'John', 'age': 22}
studentInfo(courses, info)
print("-----------------------------------------------------------------------")
studentInfo(*courses, **info)

