print("===== using map =======")
# what is map function?
"""
- apply same function to each element of a sequence / list
- return the modified list
"""

list_1 = [1, 2, 3, 4]

def square_up(input_list):
    list_2 = []
    for num in input_list:
        list_2.append(num ** 2)
    return list_2


print("Square up using explicit function: {}".format(square_up(list_1)))

square_map_lambda = list(map(lambda x: x ** 2, list_1))
print("Square up using map+lambda: {}".format(square_map_lambda))

from numpy import square
square_map_lambda = list(map(square, list_1))
print("Square up using map+square: {}".format(square_map_lambda))

square_map_lambda = list(n * n for n in list_1) # OR [n * n for n in list_1]
print("Square up using list comprehension: {}".format(square_map_lambda))


print("\n\n===== using filter =======")
def over_two(input_list):
    list_2 = [n for n in input_list if n > 2]
    return list_2


print("Filter >2 using explicit function: {}".format(over_two(list_1)))
print("Filter >2 using filter+lambda: {}".format(list(filter(lambda x: x > 2, list_1))))
generator_with_over_two = (n for n in list_1 if n > 2)
print("generator_with_over_two from list comprehension: {}".format(generator_with_over_two))
print("generator_with_over_two from list comprehension: {}".format(type(generator_with_over_two)))
print("Filter >2 using list comprehension: {}".format(list(generator_with_over_two)))

print("\n\n===== using reduce =======")
# what is reduce function?
"""
- applies same operation to items of a sequence / list
- uses result of operation as first param of next operation
- returns an item, not a list

Example: 
List = [m, n, o] and Reduce Function = f()
execution would be like this: f(f(m, n), o)
"""

def mult_list_items(list_1):
    if len(list_1) < 1:
        print("Input list is Empty")
        return -1
    result = list_1[0]
    for i in range(1, len(list_1)):
        result *= list_1[i]
    return result


print("Multiply list items using explicit function: {}".format(mult_list_items(list_1)))

from functools import reduce
print("Multiply list items using reduce+lambda: {}".format(reduce(lambda x, y: x * y, list_1)))

