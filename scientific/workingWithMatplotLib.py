import numpy as np
from matplotlib import pyplot as plt

print("===== length of words in a list =======")
x = np.arange(0, 10, 1)
print("numpy arange() 0->10 with incr of 1 : {}".format(x))
print("numpy arange() 1->10 with incr of 2 : {}".format(np.arange(1, 10, 2)))

x = np.arange(0, 10, 1)
y = np.arange(0, 10, 1)

plt.plot(x, y)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("X vs Y")

data = {"apple": 50, "banana": 20, "orange": 30}
names = data.keys()
values = data.values()
plt.bar(names, values)






