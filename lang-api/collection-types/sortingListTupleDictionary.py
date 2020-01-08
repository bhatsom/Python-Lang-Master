# Sorting List
my_list = [9, 2, 4, 1, 5, 15, 3, 10]
my_sorted_list = sorted(my_list)

print("my sorted list: {}".format(my_sorted_list))
# sort a list without using a new list
my_list.sort()
print("my list sorted: {}".format(my_list))

# reverse sorted
my_list_rev_sorted = sorted(my_list, reverse=True)
print("my list reverse sorted: {}".format(my_list_rev_sorted))
# reverse sort a list without using a new list
my_list.sort(reverse=True)
print("my reverse list sorted: {}".format(my_list))


tuple = (9, 2, 4, 1, 5, 15, 3, 10)
# tuple.sort() -- doesnt work as Tuple has no sort() method
# but we can always use the sorted() method
print("sorted tuple: {}".format(sorted(tuple)))

# sorting dictionaries
student = {'name': 'John Doe', 'age': 25, 'courses': ['Math', 'CompSci']}

# sorted() returns a sorted list of keys
print("sorted student:", sorted(student))


