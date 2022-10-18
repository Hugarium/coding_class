## Separate intergers, floatsnd strings into different list from the list below #####

list_of_integers = []

list_of_floats = []

list_of_strings = []

list_of_values = ["list", 0.66, 3.6, 33.7, "string", 7, 9, "floats", 1, 3,5]

for integers in list_of_values:

	if(type(integers) is int):

		list_of_integers.append(integers)

print(list_of_integers)


for decimals in list_of_values:

	if(type(decimals) is float):

		list_of_floats.append(decimals)

print(list_of_floats)


for strings in list_of_values:


	if(type(strings) is str):

		list_of_strings.append(strings)

print(list_of_strings)

