import random

feetInAMile = 5280

def random_number_generator(lowerBound = 1, upperBound = 100):
    return random.randint(lowerBound, upperBound)

def get_file_name_and_extension(fullFileName):
    return {
        "fileName": fullFileName[0:(fullFileName.index("."))],
        "fileExtension": fullFileName[(fullFileName.index(".")):]
    }