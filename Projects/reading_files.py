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

# Appending is a similar process, but keep in mind when you write to a file your changes will persist beyond each code run!
appendFile = open("assets/read_this.txt", "a")
if appendFile.writable():
    appendFile.write("\nAnd now I write text too")
else:
    print("File is not writable")
appendFile.close()

newFile = open("assets/new_file.txt", "w")
if (newFile.writable()):
    newFile.write("And now I've written to another file as well!")
else:
    print("File is not writable")
newFile.close()