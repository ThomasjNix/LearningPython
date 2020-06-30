'''
 To read files, you must open the file to read it
 The second parameter is the mode to open the file in - in this case, "r" is for read
 Other modes are "w" for write, "a" for append (which only allows information to be added to the end of the file), and
 "r+" which gives read and write access
'''
fileData = open("assets/read_this.txt", "r")

# Make sure the file is actually readable
if fileData.readable():
    # You can read the metadata about the file reading by just printing the variable
    print(fileData)

    # You can read one line at a time with the readline method
    print(fileData.readline())

    '''
    You can read all lines in the file with the readlines() method
    Notice how the first line is not read here - that's because it was already read previously
    '''
    print(fileData.readlines())
else:
    print("Cannot read file")

# You want to make sure to close any files that are open
fileData.close()