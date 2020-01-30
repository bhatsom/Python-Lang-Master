# what is lambda?
"""
- simple 1 line function
- doesnt use def or return keywords
- it is implicit
- syntactic sugar / shorthand for simple and small functions
"""

print("===== Addition using traditional function VS lambda =======")
def add_two_numbers(x, y):
    return x + y


print("(10 + 20) using explicit function: {}".format(add_two_numbers(10, 20)))

add_lambda = lambda x, y: x + y
print("(10 + 20) using lambda function: {}".format(add_lambda(10, 20)))


print("===== MaxOfTwoNumbers using traditional function VS lambda =======")
def max_of_two_nums(x, y):
    if x > y:
        return x
    else:
        return y


print("\n\nMaxOfTwoNumbers (18, 17) using explicit function: {}".format(max_of_two_nums(18, 17)))


max_of_two_lambda = lambda x, y: x if x > y else y
print("MaxOfTwoNumbers (18, 17) using lambda function: {}".format(max_of_two_lambda(18, 17)))

