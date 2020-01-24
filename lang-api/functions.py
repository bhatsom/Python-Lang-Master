# https://www.techbeamers.com/python-function/


# variable arg functions
def inventory(category, *items):
    print("%s [no of items=%d]" % (category, len(items)), items)
    for item in items:
        print("-", item)


inventory("Electronics", "tv", "refrigerator", "air conditioner", "iPhone")
# Empty inventory - skipping the varargs part altogether
inventory("Books")

# Name Resolution In A Python Function
# LEGB rule applied: Local, Enclosing, Global, Built-in

var = 5
def fn1():
    var = [3, 5, 7, 9]
    def fn2():
        var = (21, 31, 41)
        print("var local:", var)

    fn2()
    print("var enclosing:", var)


fn1() # uncomment var assignments one-by-one and check the output
print("var global: {}\n".format(var))

# Scope Lookup In Functions
# scope lookup remains in action even if the enclosing function has already returned

def fn1():
    print("In fn1")
    X = 100
    def fn2():
        print('In fn2')
        print(X)  # Remembers X in enclosing def scope
    return fn2  # Returns fn.2 but doesn't call it

action = fn1()  # creates and returns function
print('fn2() has not been executed yet')
action()  # Call fn2() now: prints 100
print('\n')

# Python Functions As Objects
# Python treats everything as an object and functions are no different.

def testFunc(a, b):
    print('testFunc called')
fn = testFunc
fn(22, 'bb')
print('\n')

# You can even pass the function object to other functions.
def fn1(a, b): print('fn1 called')
def fn2(fun, x, y): fun(x, y)
fn2(fn1, 22, 'bb')
print('\n')

# You can also embed a function object in data structures.
def fn1(a): print('fn1', a)
def fn2(a): print('fn2', a)

listOfFuncs = [(fn1, "First function"), (fn2, "Second function")]

for (f, arg) in listOfFuncs:
    f(arg)

print('\n')

# You can return a function object from another function.
def FuncLair(produce):
    def fn1(): print('fn1 called')
    def fn2(): print('fn2 called')
    def fn3(): print('fn3 called')

    if produce == 1: return fn1
    elif produce == 2: return fn2
    else: return fn3


f = FuncLair(2); f()

# Function Attributes
'''
Python functions also have attributes.

You can list them via the dir() built-in function.
The attributes can be system - defined.
Some of them can be user - defined as well.
The dir() function also lists the user-defined attributes.
'''

def testFunc():
    print("Im just a test function.")


testFunc.attr1 = "Hello"
testFunc.attr2 = 5
testFunc()
print(dir(testFunc))

