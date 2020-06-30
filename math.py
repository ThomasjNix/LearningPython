from math import *

### Math operations

# Arithmetic
print(1+1) # 2
print(2-1) # 1
print(2*3) # 6
print(6/2) # 3.0 (note decimal)
print(5**3) # 125 (exponentiation)
print(15%4) # modulo

# Conversion
some_number = 7
print("My favorite number is " + str(some_number))

# Absolute value
print(abs(-5)) # 5

# Exponentiation, same as X**Y
print(pow(3,2)) # 9
print(3**2) # 9

# Min / Max
print(min(5,2,7,9,3)) # 2
print(max(5,2,7,9,3)) # 9

# Rounding to n number of digits (default 0, e.g. integer)
print(round(3.141592653, 3)) # 3.142

### From math module

# Floor and ceiling
print(floor(3.141)) # 3
print(ceil(3.141)) # 4

# Square root
print(sqrt(9)) # 3
