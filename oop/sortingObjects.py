
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({}, {}, {})'.format(self.name, self.age, self.salary)


e1 = Employee('Carlos', 22, 5000)
e2 = Employee('Sarah', 28, 5000)
e3 = Employee('John', 32, 8000)

emp_list = [e1, e2, e3]

print("emp list:", emp_list)

# below would result in Unorderable Error
# TypeError: '<' not supported between instances of 'Employee' and 'Employee'
#sorted_employees = sorted(emp_list)

# lets define functions that will dictate how to compare employees during sorting
def emp_sort_by_name(emp):
    return emp.name

def emp_sort_by_age(emp):
    return emp.age

sorted_employees = sorted(emp_list, key=emp_sort_by_name)
print("emp list sorted by name:", sorted_employees)

sorted_employees = sorted(emp_list, key=emp_sort_by_age)
print("emp list sorted by age:", sorted_employees)

# using lambda sort key
sorted_employees = sorted(emp_list, key=lambda e: e.salary, reverse=True)
print("emp list sorted by lambda salary:", sorted_employees)

# sort using attrgettr
from operator import attrgetter

sorted_employees = sorted(emp_list, key=attrgetter('name'))
print("emp list sorted by attrgetter name:", sorted_employees)

