# https://www.techbeamers.com/python-tuple/

print("\n\n=== Creating Tuple in different ways ===")
# Creating A Tuple Of Size One
# A single element surrounded by parenthesis will create string/int/float etc. instead of a tuple
my_tuple = ("single")
print("type( my_ tuple )-1 ", type(my_tuple))

my_tuple = (10)
print("type(my_tuple)-2", type(my_tuple))

my_tuple = (10.5)
print("type(my_tuple)-3", type(my_tuple))

# We need to place a comma after the first element to create a tuple of size "one"
my_tuple = ('single',)
print("type(my tuple )-4", type(my_tuple))

# We can use a list of one element and convert it to a tuple
my_tuple = tuple([10])
print("type(my_tuple)-5", type(my_tuple))

# We can use a set ofone element and convert it to a tuple
my_tuple = tuple( { 10.5})
print("type(my_tuple)-6", type(my_tuple))

print("\n\n=== accessing elements from Tuple ===")
vowel_tuple = ('a','e','i','o','u')
print("The tuple:", vowel_tuple, "Length:", len(vowel_tuple))

# Accessing the first element
print("vowel_tuple[0]:", vowel_tuple[0])

# Accessing the last element
print("vowel_ tuple[length-1]: ", vowel_tuple[len(vowel_tuple) - 1])

# Indexing mechanism in a tuple of tuples
t_o_t = (('Jan', 'feb', 'mar'), ('sun', 'mon', 'wed'))
# Accessing elements from the first sub tuple
print("t_o_t[0][2]:", t_o_t[0][2])
# Accessing elements from the second sub tuple
print("t_o_t[1][2]:", t_o_t[1][2])

print("\n\n=== Modify/Update A Tuple ===")
# Tuples are immutable - once we assign a set of elements, Python won't allow it to change
# But, there is a catch. If the items are mutable, we can change the elements instead of directly modifying the tuple
py_tuple = (22, 33, 55, 66, [88, 99])
print("Tuple before modification:", py_tuple)

# Let's try to modify py_tuple. It wll return TypeError
try:
    py_tuple[0] = 11
except Exception as ex:
    print("py_tuple[0] Error:", ex)

# We can change the values of mutable elements inside the py_tuple i.e. the List
py_tuple[4][0] = 808
py_tuple[4][1] = 909
print("Tuple after modification:", py_tuple)

# We can assign a tuple with new data
py_tuple = ('mon', 'tue', 'wed')
print("Tuple after reassignment:", py_tuple)

print("\n\n===  + (concatenation) and * (repeat) operators. ===")
first_tuple = ('p', 'y', 't')
second_tuple = ('h', 'o', 'n')
full_tuple = first_tuple + second_tuple
print("full_tuple: ", full_tuple)

init_tuple =("fork",)
fork_tuple = init_tuple * 5
print("fork_tuple: ", fork_tuple)


print("\n\n=== Remove/Delete A Tuple ===")
py_tuple = ('p', 'y', 't', 'h', 'o', 'n')
# we can't delete a particular item from a tuple
try:
    del py_tuple[0]
except Exception as ex:
    print("del py_tuple[0] Error:", ex)

# but you can delete a whole tuple
del py_tuple
try:
    print(py_tuple)
except Exception as ex:
    print("print(py_Juple) =>. Error:", ex)

print("\n\n=== Existence check ===")
py_tuple = ('p', 'y', 't', 'h', 'o', 'n')
print("Does 'p' exist?", 'p' in py_tuple)
print("Does 'Z' exist?", 'Z' in py_tuple)

print("\n\n=== Traversing A Tuple ===")
for item in py_tuple:
    print("Item: ", item)

# Usage of Tuple
"""
Used For Grouping Data: The tuple provides a quick way of grouping and arranging data. It helps combine any
number of elements into a single unit.

Tuple helps us represent information in the form of records such as 'the employee record'. It allows us to group
related information and use it as a single entity.
"""

emp_records = ('John', 'hr', 2010, 'robert', 'account', 2015, 'bill', 'mis', 2018)
print("emp_record: ", emp_records)

# tuple assignment
(emp_name, emp_dept, empjoin_date) = emp_records[0:3]
print("emp_name:", emp_name, "emp_dept:", emp_dept, "empjoin_date", empjoin_date)

# Using Tuples In Functions As Return Value
def square(n1, n2):
    return (n1 * n1, n2 * n2)


print("square(2, 3): ", square(2, 3))

# ----ENOUGH---- #

