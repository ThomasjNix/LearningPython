### Variables and data types

# Variables don't have to be declared with a type
name = "John Smith"
age = 35

# Variables can be reassigned
age = 25

### Basic data types

name = "Tom" # string
age = 30 # int
balance = 144.23 # float
married = True # boolean

### String operations

# Strings can be concatenated, but integers and other types must be converted.
print("There was a man named " + name + ".")
print(name + " was " + str(age) + " years old.")

# String transformation examples
print("example".upper()) # EXAMPLE
print("example".upper().isupper()) # TRUE

# String indexing
print("the apple fell out of the tree".index("apple")) # 4

# String replacement
print("the apple fell out of the tree".replace("apple", "orange")) # the orange fell out of the tree