########################  LIST #############################

list_of_countries = ["Japan", "Iraq", "Afganistan", "Ghana", "Nigeria", "Israel", "France"]


######################## Add Egypt and Congo to the list

list_of_countries.append("Egypt")

list_of_countries.append("Congo")

print(list_of_countries)


##################### Replace Egypt with Burundi ##################

list_of_countries[7] = "Burundi"

print(list_of_countries)

#################### Replace Congo with Brazil ####################

list_of_countries[8] = "Brazil"

print(list_of_countries)


################### Finding the positions of items ###############

#####Finding the position of Brazil #########
index_position_of_Brazil = list_of_countries.index("Brazil")

print(index_position_of_Brazil)

########### Finding the index position of Israel ###############

index_position_of_Israel = list_of_countries.index("Israel")

print(index_position_of_Israel)


############# Slicing ########################################

list_of_countries[0:4]

print(list_of_countries[0:4])



