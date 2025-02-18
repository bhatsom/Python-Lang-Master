# Create a function that counts the number of times the word "dog" occurs in a string, ignore edge cases.

def countDog (str):
    i = 0
    list_1 = str.split()
    print(list_1)
    for word in list_1:
        if word.lower() == 'dog':
            i += 1
    return i

def countDog_2 (str):
    i = 0
    for word in str.split():
        if word.lower() == 'dog':
            i += 1
    return i

def countDog_3 (str):
    return len(list(filter(lambda word: word.lower() == 'dog', str.split())))

print("Number of times dog - test 1: {}".format(countDog("This dog runs faster than the other Dog dude!")))
print("Number of times dog - test 2: {}".format(countDog_2("This Dog runs faster than the other dog dude!")))
print("Number of times dog - test 3: {}".format(countDog_3("This dog runs faster than the other Dog dude!")))
