# https://www.techbeamers.com/python-dietionary/

blank_dict = {}

# diet with numeric keys
num_dic = {1: "a", 2: "b"}

# diet with keys as different data types
misc_keys_dict = { 'stringKey': 'stringVal', 1: [1, 2, 3]}
print("misc_keys_dict", misc_keys_dict)
print("misc_keys_dict.get(1)", misc_keys_dict.get(1))

# create a diet with diet() method
dict_from_func = dict({1: 'veg', 2: 'non-veg'})

# Create a diet from a sequence of tuples
dict_from_seq = dict([(1, 'jake'), (2, 'john')])

# Access Elements
dict = {'Student Name': 'Berry', 'Roll No.': 12, 'Subject': 'English'}

# 1 - using Key index - throws KeyError if key is missing / invalid
print("Student Name", dict['Student Name'])

try:
    print("DOB", dict["DOB"])
except Exception as e:
    print("Error using invalid key. Type: ", e.__class__)
    print("Error using invalid key: Args: ", e.args)

# 2 - using get() - doesnt throw KeyError if key is missing / invalid
print("Subject", dict.get('Subject'))

try:
    print("DOB", dict.get('DOB'))
except Exception as e:
    print("Error while using invalid key", e)

# Append a Dictionary
# 1 - using Assignment
dict["DOB"] = "Jan 1, 2001"
# 2 - using update()
dict.update({"Score": "A+"})
print("diet: ", dict)
dict.update(Score = "A")
print("diet: ", dict)

# Remove Elements
sixMonths = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30}

# Delete a specific element
print(sixMonths.pop(6))
print("sixMonths: ", sixMonths)

# Delete a random element
print(sixMonths.popitem())
print("sixMonths:", sixMonths)

# Remove a specific element
del sixMonths[4]
print("sixMonths:", sixMonths)

# Delete all elements from the dictionary
sixMonths.clear()
print("sixMonths:", sixMonths)

# Finally, eliminate the dictionary object
del sixMonths
try:
    print("sixMonths:", sixMonths)
except Exception as e:
    print("Error accessing deleted dictionary: Type: ", e.__class__)
    print("Error accessing deleted dictionary: Args: ", e.args)

# Iterate Dictionary
for key in dict:
    print("key=", key)

for key, value in dict.items():
    print("key=", key, "value=", value)

# Dictionary Comprehension

dict2 = { str(iter): iter for iter in [11, 22, 33, 44] }
print("dict2: ", dict2)

weekdays = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']
dict3 = { w : len(w) for w in weekdays }
print("dict3: ", dict3)

dict4 = { w : indx for indx, w in enumerate(weekdays) }
print("dict4: ", dict4)

# Membership Test
print("55 is in dict2", 55 in dict2)

