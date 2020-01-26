# Loop through a List
print("-------------------Loop through a List---------------------------------")
nums = [1, 3, 5, 7]
target = 3
for num in nums:
    print('item is={}'.format(num))
    if num == target:
        print('Found the target')
        break
    else:
        print('Moving on')
print("---------------------Using continue------------------------------------")
for num in nums:
    if num <= target:
        print('continue')
        continue
    else:
        print(num)
print("-------------------Loop through a Range--------------------------------")
for i in range(5):
    print(i)
print("-----------------------------------------------------------------------")
# use a starting point in a range
for i in range(2, 5):
    print(i)
print("-----------------------------------------------------------------------")

print("-----------------------------------------------------------------------")

print("-----------------------------------------------------------------------")

print("-----------------------------------------------------------------------")
