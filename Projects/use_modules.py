import useful_tools

'''
Modules are a great way to make code reusable and write useful applications without reinvinting the wheel
'''
numMiles = float(input("How many miles would you like to convert?\n"))
print("There are " + str(useful_tools.feetInAMile * numMiles) + " feet in a mile.")

diceRoll1 = useful_tools.random_number_generator(1,6)
diceRoll2 = useful_tools.random_number_generator(1,6)
print("You rolled two dice and got " + str(diceRoll1) + " and " + str(diceRoll2) + ", totalling " + str(diceRoll1 + diceRoll2))

fileData = input("Enter a file name\n")
seperatedFileData = useful_tools.get_file_name_and_extension(fileData)
print("File data for " + fileData + ":")
print("File name: " + seperatedFileData["fileName"])
print("File extension: " + seperatedFileData["fileExtension"])