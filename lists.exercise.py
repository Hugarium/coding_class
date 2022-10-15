list_of_colors = ["turquoise", "cyan", "deepskyblue", "gold", "maroon"]

print(list_of_colors)

list_of_names = ["Kobe", "Gigi", "Phil", "Kyrie"]

print(list_of_names)

list_of_integer_numbers = list(range(1, 21))

print(list_of_integer_numbers)



###################  indexing a list #######################

list_of_colors = ["turquoise", "cyan", "deepskyblue", "gold", "maroon"]

print(list_of_colors[3])

print(list_of_colors[4])

print(list_of_colors[2])

print(list_of_colors[-1])

len(list_of_colors)


########Slicing a list #############################

list_of_colors[1:4]

print(list_of_colors[1:4])

print(list_of_colors[2:])
print(list_of_colors[-1])

print(list_of_colors[:-1])

############################### mutating a list ##############################

print(list_of_names)

list_of_names.append("offei")

print(list_of_names)

list_of_names.append("amoako")

print(list_of_names)

#################################### .append is used to add items to a list ###############################

list_of_names.append("isaac")

print(list_of_names)



##################### finding the index position of items ###########################

index_position_of_offei = list_of_names.index("offei")

print(index_position_of_offei)


#################### Removikng elements from a list ################################

index_position_of_offei = list_of_names.index("offei")

print(index_position_of_offei)



print(list_of_names)

list_of_names.append("Amoako")

print(list_of_names)

list_of_names.append("Kwabena")

print(list_of_names) 

list_of_names.index("Kwabena")

print(list_of_names)

index_position_of_Kwabena = list_of_names.index("Kwabena")

print(index_position_of_Kwabena)


################# Removing value from a list ##########################

index_position_of_Kwabena = list_of_names.index("Kwabena")

print(index_position_of_Kwabena)

list_of_names.pop(index_position_of_Kwabena)

print(list_of_names)