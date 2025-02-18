
def reverse_string(input_string):
    output = ""
    for c in input_string:
        output = c + output
    return output

print("1) 'ABCD' reversed = {}".format(reverse_string("ABCD")))


# using character Array instead of string concatenation
from array import array


def reverse_string_2(input_string):
    input_len = len(input_string)
    output = [None] * input_len
    #output = array('u')
    index = input_len - 1

    for c in input_string:
        output[index] = c
        index -= 1

    return "".join(output)

print("2) 'ABCD' reversed = {}".format(reverse_string_2("ABCD")))

