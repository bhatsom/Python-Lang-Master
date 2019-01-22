my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#          0, 1, 2, 3, 4, 5, 6, 7, 8, 9 -- positive indexes
#        -10,-9,-8,-7,-6,-5,-4,-3,-2,-1 -- negative indexes

# list[start:end:step]

# end is exlusive
print(my_list[0:5])

# leaving stat and blank covers the whole iterable
print(my_list[::])

# every other element
print(my_list[::2])

# using a step - no effect as it cannot go back when starting at the beginning
print(my_list[::-1])

sample_url = 'http://coreyms.com'
print(sample_url)

# Reverse the url
print(sample_url[::-1])

# Get the top level domain
print(sample_url[-4:])

# Print the url without the http://
print(sample_url[7:])

# Print the url without the http:// or the top level domain
print(sample_url[7:-4])

