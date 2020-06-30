# Try and except are used to catch errors
try:
    userInput = int(input("Enter an integer:\n"))
    print("Good job, you entered an integer. It was " + str(userInput))
    print("Now I'm going to divide by zero to show error handling with finer control")
    print(userInput / 0)
except ZeroDivisionError:
    print("Hey you can't just go around dividing by zero like that!")
except:
    # This is a ValueError, but it's being used as a catch-all
    print("Entering an integer was a simple request but you couldn't even get that right.")


'''

Also this is a multi-line comment, neat

'''