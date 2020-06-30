# if syntax
some_boolean = True
if some_boolean:
    print("evaluated to true")
else:
    print("evaluated to false")

def is_even(num):
    return round(num) % 2 == 0

def print_based_on_even(number):
    if is_even(number):
        print("the number you provided was even or rounded to an even number")
    else:
        print("the number you provided was odd or rounded to an odd number")

print_based_on_even(1)
print_based_on_even(2)
print_based_on_even(3)

# And and Or
if True and False:
    print("This is unreachable code")
elif False and False:
    print("This is also unreachable")
else:
    print("Finally, some reachable code!")

# not keyword
if True and not False:
    print("The not keyword checks that to provided condition evaluates to false")