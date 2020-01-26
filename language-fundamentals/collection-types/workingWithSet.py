# https://www.techbeamers.com/python-set/

my_set_1 = {} # will create dictionary
print('type(my_set_1)): ', type(my_set_1))

my_set_2 = set() # will create empty set
print('type(my_set_2)): ', type(my_set_2))

my_set = {7, 8}
try:
    print(my_set[0]) # set does not support index based access
except Exception as ex:
    print("Error accessing my_set[0]", ex)

print('my_set: ', my_set)

print("\n\n=== ADD ===")
# add ONE element to the set
my_set.add(9)
# add MULTIPLE element to the set
my_set.update([1, 2, 3])
print('my_:_set: ', my_set)

# Let's add a LIST and a SET to the set
my_set.update([5.5, 6.6, 4.4], {10, 20, 30})
print('my_set: ', my_set)

print("\n\n=== DELETE ===")
# discard() - does not throw Error if target item is not present
my_set.discard(99)
my_set.discard(4.4)
print('my_set: ', my_set)

# remove() - throws "KeyError" if target item is not present
try:
    my_set.remove(my_set, 99)
except Exception as ex:
    print("Error deleting 99 from set: ", ex.__str__())
    print("Error type deleting 99 from set: ", ex.__class__)
    print("Is KeyError deleting 99 from set: ", isinstance(ex, KeyError))

my_set.remove(1)
print('my_set: ', my_set)

# pop() - item is picked randomly nnd removed
print("Popped item:", my_set.pop())
print('my_set: ', my_set)

# Native Operations - UNION, INTERSECTION, DIFFERENCE, SYMMETRIC DIFFERENCE, and COMPLEMENT
print("\n\n===Native Operations - UNION, INTERSECTION, DIFFERENCE, SYMMETRIC DIFFERENCE, and COMPLEMENT===")
setA = {'a', 'e', 'i', 'o', 'u', 'g', 'h'}
setB = {'a', 'e', 'z', 'b', 't', 'o', 'u'}

# union() / |
print("setA | setB:", setA | setB, "length of (setA I setB): ", len(setA | setB))
print("setA union setB:", setA.union(setB), " length of (setA.union(setB)):", len(setA.union(setB)))

# intersection() / &
print("setA & setB:", setA & setB)
print("setA intersection setB:", setA.intersection(setB))

# difference() / -
print("setA difference setB: ", setA - setB)
print("setA difference setB: ", setA.difference(setB))

# symmetric_ difference() / ^
print("setA symmetric_difference setB: ", setA ^ setB)
print("setA symmetric_difference setB: ", setA.symmetric_difference(setB))

# Access elements of a Set
print("\n\n=== Access elements of a Set ===")
basket = set(["apple", "mango", "banana", "grapes", "orange"])
for fruit in basket:
    print(fruit)

# check if 'apple' is in the basket
print("Is 'apple' in the basket?", 'apple' in basket)

# Frozen Sets - immutable and doesn't allow modification after assignment.
frozen_set = frozenset(["apple" , "mango", "orange"])

# Below code will raise an error as we are modifying a frozen set
try:
    frozen_set.add("banana")
except Exception as ex:
    print("Error:", ex)

