#calculate the body mass index of a person

#body_mass_index = kg/m**2

#kilograms - weight of the person in kilograms

#mass - height of the person in meter square

weight = float(input("enter the weight of the person: "))

height = float(input("enter the height of the person: "))

body_mass_index = (weight / height**2)

print(body_mass_index)