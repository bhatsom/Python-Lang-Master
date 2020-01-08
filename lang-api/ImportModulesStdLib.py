# importing modules and using Python standard library

courses = ['History', 'Math', 'Physics', 'CompSci']

import modules.testModule # cannot be referred as testModule
import modules.testModule as testModule
index = testModule.find_index(courses, 'Math')
print('Index of Math = {}'.format(index))
print("-----------------------------------------------------------------------")

# import a function from a module
from modules.testModule import find_index
index = find_index(courses, 'CompSci')
print('Index of CompSci = {}'.format(index))
print("-----------------------------------------------------------------------")

# import a varibale from a module
from modules.testModule import testMessage as msg
print(msg)
print("-----------------------------------------------------------------------")

# import both function and variable together from a module
from modules.testModule import find_index as fi, testMessage as testMsg
print('Index of CompSci again = {}'.format(fi(courses, 'CompSci')))
print(testMsg)
print("-----------------------------------------------------------------------")

# playing with sys module
import sys
print(sys.path)
#sys.path.append('/Users/somnath')
print()
print(sys.path)
print("-----------------------------------------------------------------------")

# playing with random module
import random
print('A random course from courses: {}'.format(random.choice(courses)))

# playing with math module
import math
print('Factorial of 5: {}'.format(math.factorial(5)))

# playing with datetime and calender
import datetime
import calendar

today = datetime.date.today()
print('Today\'s date is:{}'.format(today))
print('Is 2018 a leap year? {}'.format(calendar.isleap(2018)))

# playing with operating system module
import os
print('Current working directory is: {}'.format(os.getcwd()))
print('Location of os module: {}'.format(os.__file__))

import webbrowser
#webbrowser.open('http://google.com')

