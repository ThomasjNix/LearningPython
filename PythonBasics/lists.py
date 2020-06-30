# List can have multiple types

list_that_makes_no_sense = ["Tim", 2, 34.7, ["another list", 7]] # Valid!

# List references
cool_cars = ["Ford Mustang", "Chevrolet Corvette", "Dodge Viper"]
print(cool_cars[1]) # Chevrolet Corvette

# Negative list reference from the back of the list (starts at -1)
print(cool_cars[-1]) # Dodge Viper

# Partial lists
print(cool_cars[1:]) # Grabs everything after (but NOT including) the first index (not starting at 0) - e.g. ["Chevrolet Corvette", "Dodge Viper"]
print(cool_cars[1:3]) # Grab everything up to (but NOT including) the end index (not starting at 0) - e.g. ["Ford Mustang", "Chevrolet Corvette"]

# In place modification
cool_cars[2] = "Lamborghini Huracan"
print(cool_cars) # ["Ford Mustang", "Chevrolet Corvette", "Lamborghini Huracan"]

# List extension / concatenation
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7,9]
even_numbers.extend(odd_numbers) # NOTE: Does not return data, in place modification
print(even_numbers) # [2,4,6,8,1,3,5,7,9]

# List sorting (default increasing)
even_numbers.reverse()
print(even_numbers)
even_numbers.sort() # NOTE: Does not return data, in place modification
print(even_numbers)

# Append to list
even_numbers.append(10)
print(even_numbers) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# List insertion (index starts at 0)
even_numbers.insert(1, 1.5)
print(even_numbers) # [1, 1.5, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Pop
even_numbers.pop()
print(even_numbers) # [1, 1.5, 2, 3, 4, 5, 6, 7, 8, 9]

# Removing by value
even_numbers.remove(1.5)
print(even_numbers) # print(even_numbers) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Removing by index (starts at 0)
even_numbers.pop(8)
print(even_numbers)

# clear list
even_numbers.clear()
print(even_numbers)