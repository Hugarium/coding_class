## Separate intergers, floatsnd strings into different list from the list below #####

list_of_integers = []

list_of_floats = []

list_of_strings = []

list_of_values = ["list", 0.66, 3.6, 33.7, "string", 7, 9, "floats", 1, 3,5]

for value in list_of_values:

	if (type(value) is int):

		list_of_integers.append(value)

	elif (type(value) is float):

		list_of_floats.append(value)

	elif (type(value) is str):

		list_of_strings.append(value)

	else:

		continue

print(list_of_integers)

print(list_of_floats)

print(list_of_strings)
