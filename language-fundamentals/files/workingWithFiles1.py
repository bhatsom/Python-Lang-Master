# https://www.techbeamers.com/python-file-handling-tutorial-beginners/

# open a file - this returns a file handle
# file fileObj = open(file-name [, access-mode] [, buffering])
# default values: access-mode = r, buffering = Q

#Open a file in write and binary mode.
fileObj = open("test-1.txt", "wb")

# access file attributes
print("File name:", fileObj .name)
print("File state:", fileObj.closed)
print("Opening mode:", fileObj.mode)
#print("Softspaee flag: ", fileObj.softspace) -- doesnt work in 3.7

