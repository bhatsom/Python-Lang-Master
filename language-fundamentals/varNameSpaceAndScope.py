# https://www.techbeamers.com/python-namespace-scope/

var_a = 10
print("Start: ", dir())

def foo():
    var_b = 20
    print("Inside foo(): ", dir())

foo()
print("End: ", dir())
print("================")


# Another example
def outer_foo():
    outer_var= 3

    def inner_foo():
        inner_var = 5
        print('From inner foo: ', dir())

    outer_var= 7
    inner_foo()
    print('From outer foo: ', dir())


outer_foo()
print('================')

#One more
a_var = 5
b_var = 7

def outer_foo():
    global a_var
    a_var= 1
    b_var= 2

    def inner_foo():
        global a_var
        a_var = 3
        b_var = 4
        print('a_var inside inner_foo :', a_var)
        print('b var inside inner_ foo : ', b_var)

    inner_foo()
    print('a_var inside outer_foo :', a_var)
    print('b_var inside outer_foo :', b_var)


outer_foo()
print('a_var outside all functions: ', a_var)
print('b_var outside all functions: ', b_var)

