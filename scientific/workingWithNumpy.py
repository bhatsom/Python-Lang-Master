import numpy as np

print("===== define one dimensional arrays =======")
one_d_array = np.array([1, 2, 3])
print("one_d_array: {}".format(one_d_array))

print("===== define two dimensional arrays =======")
two_d_array = np.array( [[1, 2, 3], [4, 5, 6]] )
print("two_d_array:\n {}".format(two_d_array))

two_d_array_all_zeros = np.zeros((5, 5))
print("two_d_array_all_zeros:\n {}".format(two_d_array_all_zeros))

print("===== sum of array rows and columns =======")
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
sum_array_cols = np.sum((a, b), axis=0)
print("sum_array_cols: {}".format(sum_array_cols))

sum_array_rows = np.sum((a, b), axis=1)
print("sum_array_rows: {}".format(sum_array_rows))

print("===== array sorting =======")
x = np.array([12, 43, 2, 100, 54, 5])
x_sorted = np.argsort(x)
print("x_sorted: {}".format(x_sorted))

x_sorted = np.argsort(x)[-2:]
print("x_sorted: {}".format(x_sorted))

print("===== replace odd numbers in array with -1 =======")
arr = np.arange(0, 10, 1)
