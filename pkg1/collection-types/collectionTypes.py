# --- List --- #
courses = ['History', 'Math', 'Physics', 'CompSci']
print('courses: {}'.format(courses))
print("-----------------------------------------------------------------------")

courses.insert(0, 'Art')
print('courses with Art added: {}'.format(courses))
courses.append('Biology')
print('courses appended with Biology: {}'.format(courses))
courses_2 = ['Geography']
courses.append(courses_2)
print('courses appended with courses_2: {}'.format(courses))
print("-----------------------------------------------------------------------")

courses.remove('Math')
print('courses after removing Math: {}'.format(courses))
courses.remove(courses_2)
print('courses after removing courses_2: {}'.format(courses))
print("-----------------------------------------------------------------------")

courses.sort()
print('courses sorted: {}'.format(courses))

courses.sort(reverse=True)
print('courses reverse sorted: {}'.format(courses))
print("-----------------------------------------------------------------------")

print('Index of CompSci in courses List: {}'.format(courses.index('CompSci')))
print("-----------------------------------------------------------------------")
num_list = [2, 3, 4, 5, 6]
print('sum of all in num_list = {}'.format(sum(num_list)))
print("-----------------------------------------------------------------------")

print('Printing courses using for loop: ')
print('Items with no index')
for item in courses:
    print('Item={}'.format(item))
print("-----------------------------------------------------------------------")

print('Items with index')
for index, item in enumerate(courses):
    print('Item[{}]={}'.format(index, item))
print("-----------------------------------------------------------------------")

print('Items with a non-zero starting index')
for index, item in enumerate(courses, start=1):
    print('Item[{}]={}'.format(index, item))
print("-----------------------------------------------------------------------")

print('courses concatenated and hyphen separated= {}'.format(' - '.join(courses)))
print("-----------------------------------------------------------------------")

# --- Tuple is immutable--- #
tuple_1 = ('val1', 'val2', 'val3')
print('tuple_1={}'.format(tuple_1))
print('Tuple_1 contains val1 = {}'.format('val_1' in tuple_1))
print("-----------------------------------------------------------------------")

# --- Set --- #
science_courses = {'Math', 'CompSci', 'Physics', 'Chemistry', 'Math'}
art_courses = {'English', 'Design', 'Physics', 'Art', 'Math'}

print(science_courses.intersection(art_courses))
print(science_courses.difference(art_courses))
print('All courses merged: {}'.format(science_courses.union(art_courses)))

print('English is present in merged courses = {}'.format('English' in science_courses.union(art_courses)))

# iteration
# default iteration goes over all the keys

