# https://www.techbeamers.com/python-list/

#using[]
listl = []
list2 = [1 , 2, 3]
list3 = [1, "Hello World!", 3.7]

# using list() constructor
list4 = list()
list51 = list([1, "test", 5.2])
list52 = ([1, "test", 5.2])
print(type(list51))
print("list51=", list51, "list52", list52)

# list of sub-lists
list6 = [1, 2, [3, 4, 5]]
list7 = list([1, 2, [3, 4, 5]])
print('list6:', list6)
print('list7: ', list7)

# Using comprehension -intuitive way of creating List

# Syntax: theList = [expression(iter) for iter in oldList if filter(iter)]
theList = [i for i in range(5)]
# [0, 1, 2, 3, 4]

listOfCountries = ["India", "America", "England", "Germany", "Brazil", "Vietnam"]
firstLetters = [country[0] for country in listOfCountries]
print('firstLetters: ', firstLetters)

allCombinations = list([x+y for x in 'abc' for y in 'def'])
print('aUCombinations: ', allCombinations)

combinationsWithFilter = [x+y for x in 'abc' for y in 'def' if x != 'b' and y != 'e']
print("combinationsWithFilter: {}", combinationsWithFilter)

# with index _ using enumeration
months = ['.jan', 'feb', 'mar', 'apr', 'may', '.jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dee']

oddMonths = [month for index, month in enumerate(months) if (index% 2 == 0)]
for e in enumerate(months):
    print(e)
print("oddMonths: ", oddMonths)

# Creating Multi-Dimensional List
singleList = [0] * 3
print("singleList: {}".format( singleList))

# not the right way - only one reference is created for all sub-lists - change to one will affect all
multiList = [[0] * 3] * 3
print("multiList: {} ".format(multiList))

multiList[0][2] = 5
print("multiList: {} ".format(multiList))

# instead use list comprehension
multiList = [[0] * 3 for i in range(3)]
print("multiList: {} ".format(multiList))

multiList[0][2] = 5
print("multiList: {} ".format(multiList))

#TODO
# Extend List using ExtendO And AppendO
# slicing List
theList = [i for i in range( 5)]
print('theList: {}'.format( theList))
print('theList sliced 2-5: {}'.format(theList[1:5]))