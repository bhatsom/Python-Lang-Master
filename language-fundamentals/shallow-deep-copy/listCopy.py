import copy

print("========== USING OBJECT REFERENCE ===========")
list_1 = [1, 2, 3, 4]
print(f"list_1={list_1}")

list_2 = list_1
print(f"list_2={list_2}")

list_2.append(10)
print(f"list_1={list_1}")
print(f"list_2={list_2}")

print("========== USING copy() ===========")
list_3 = [1, 2, 3, 4]
list_4 = copy.copy(list_3)
list_3.append(15)
print(f"list_3={list_3}")
print(f"list_4={list_4}")
list_3[0] = -1
print(f"list_3={list_3}")
print(f"list_4={list_4}")

print("========== USING deepCopy() ===========")
list_5 = [1, 2, 3, 4]
list_6 = copy.deepcopy(list_5)
list_5.append(15)
print(f"list_5={list_5}")
print(f"list_6={list_6}")
list_5[0] = -1
print(f"list_5={list_5}")
print(f"list_6={list_6}")

# what is the deference between copy() and deepCopy()

