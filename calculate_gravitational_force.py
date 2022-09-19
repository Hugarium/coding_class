##calculate the gravitational force

## F = GMm/r**2

##F- gravitational force

##G- gravitational constance

##M- mass of object1

##m- mass of object2

##r- distance between the two objects (radius)


gravitational_constance = 6.67e-11

mass_of_object1 = float(input("enter the mass of object1: "))

mass_of_object2 = float(input("enter the mass of object2: "))

radius = float(input("enter the distance between the objects: "))

gravitational_force = (gravitational_constance * mass_of_object1 *mass_of_object2)/(radius**2)

print(gravitational_force)