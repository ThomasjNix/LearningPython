# While loops
whileCounter = 0
while whileCounter <= 4:
    print("whileCounter is currently " + str(whileCounter))
    whileCounter += 1

print("while loop ended, whileCounter is currently " + str(whileCounter))

# For loops using a range of numbers (starting at 0, using range)
# Can also provide a start/end index using range(start, end) - NOT including end
for forCounter in range(5):
    print(forCounter)

# For loops using a range of letters in a string
for letterCounter in "This is a string":
    print(letterCounter)

# For loops using a range of elements in an array
for elementCounter in ["Example", "Test", "otherPhrase"]:
    print(elementCounter)