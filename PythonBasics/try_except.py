# Try and except are used to catch errors
try:
    userInput = int(input("Enter an integer:\n"))
    print("Good job, you entered an integer. It was " + str(userInput))
    print("Now I'm going to divide by zero to show error handling with finer control")
    print(userInput / 0)
except ZeroDivisionError as err:
    print("Hey you can't just go around dividing by zero like that!")
    print("Actual error encountered: " + str(err))
except ValueError as err:
    # This is a ValueError, but it's being used as a catch-all
    print("Entering an integer was a simple request but you couldn't even get that right.")
    print("Actual error encountered: " + str(err))


'''

Also this is a multi-line comment, neat

'''