# https://www.techbeamers.com/python-set/
my_ set_ 1 = {} # will create dictionary
. print 'type(my_set_l)): ', type(my_set_l)
my_set_2 = setO # will create empty set
print 'type(my_set_2)): ', type(my_set_2)
my_set= {7, 8}
try:
print(my_set[0]) # set does not support index based access
except Exception as ex:
print "Error accessing my_set[0]", ex
print 'my_set: ', my_set
print"== ADD=="
# add ONE element to the set
my_ set.add(9)
# add MULTIPLE element to the set
my_set.update([l, 2, 3])
pr:int 'my_:_set: ', my_set'
# Let's add a LIST and a SET to the set
my_:._set.update([5.5, 6.6, 4.4], {10, 20, 30})
print 'my_set: ', my_set
print "==DELETE=="
# discardO - does not throw Error if target item is not present
my_ set.discard(99)
my set.discard( 4.4)
print 'my_ set: ', my_ set
# removeO - throws "KeyError" if target item is not present
try:
my_ set.remove(99)
except Exception as ex:
print "Error deleting 99 from set: ", ex.message
print "Error type deleting 99 from set: ", ex._class_
print "Is KeyError deleting 99 from set: ", isinstance(ex, KeyError)

my_sot.roinoVt.'( 1)
print 'my_set: '. my_set
# pop() - item is picked randomly nnd removed
print "Popped item:", my_set.pop()
print 'my_set: ', my_set
# Native Operations - UNION, INTERSECTION, DIFFERENCE, SYMMETRIC DIFFERENCE, and
COMPLEMENT
setA = {'a', 'e', 'i'. 'o', 'u', 'g', 'h'}
setB = {'a', 'e', 'z', 'b', 't\ 'o'. 'u'}
#unionQ/ I
print "setA I setB: 11
, setA I setB, "length of (setA I setB): ", len(setA I setB)
print "setA union setB: 11
, setA.union(setB), 11 length of (setA.union(setB)): 11
, len(setA.union(setB))
# intersection() / &
print "setA & setB: 11
, setA & setB
print "setA intersection setB: 11
, setA.intersectiop.(setB)
# difference() / -
print ''setA difference setB: 11
, setA - setB
print "setA difference setB: 11
, setA.difference(setB)
# symmetric_ difference() / "
print "setA symmetric_difference setB: 11
, setA" setB
print "setA symmetric_difference setB: 11
, setA.symmetric_difference(setB)
# Access elements of a Set
basket= set(["apple", "mango", "banana", -"grapes", "orange"])
for fruit in basket:-
print fruit
# check if 'apple' is in the basket
print "Is 'apple' in the basket?", 'apple' in basket
#Frozen Sets - immutable and doesn't allow modification after assignment.
frozen_set = frozenset(["apple" , "mango", "orange"])
# Below code will raise an error as we are modifying a frozen set
try:
·frozen_ setadd("banana")
except Exception as ex:
print "Error:", ex

