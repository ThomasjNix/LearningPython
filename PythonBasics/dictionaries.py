# Dictionaries are key-value pair objects in Python

# Numeric key dictionary
monthNumeric = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
}
print(monthNumeric[1])

# String key dictionary
jobRoles = {
    "manager": "Mike",
    "team lead": "Jerry",
    "intern": "Bill"
}
print(jobRoles["team lead"] + " is the team lead.")

# .get works for retrieval as well

print(jobRoles.get("intern") + " started in " + monthNumeric.get(3))

# Default values can be provided for when the provided key is not valid
print("There's no 13th month! See: " + monthNumeric.get(13, "You gave an input that doesn't match a key!"))