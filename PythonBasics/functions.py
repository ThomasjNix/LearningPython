
# Syntax for declaring a function
def say_hello():
    print("Hello") # Indenting matters - all code within the function has to be indented

say_hello() # Call the function

# Passing parameters
def say_provided_text(say_this):
    print(say_this)

say_provided_text("This was a parameter!")

# Optional parameters
def say_additional_information(basic_info, additional_info="No second value provided"):
    print(basic_info + " " + additional_info)

say_additional_information("First argument")
say_additional_information("first argument", "second argument")

# Object returns
def cube(num):
    return num**3 # Return breaks out of the function, any code after return is unreachable
    # print("something") - unreachable code

print(cube(3))
print(cube(cube(3)))
print(cube(cube(cube(cube(3)))))