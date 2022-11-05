name_marks = {
   "Maxwell":{"maths":89, "agric":95}, 
   "Maggie":{"maths":89, "agric":78}
   }

name_marks["Maxwell"]["maths"]=100

name_marks["Maggie"]["agric"] = 100



## Changing marks for Maxwell in agric

name_marks["Maxwell"]["agric"] = 90


##changing the course names and marks for Maxwell

name_marks["Maxwell"] = {"History":76,"Physics":98}

print(name_marks["Maxwell"])


## Adding a student with corresponding marks##
name_marks["offei"] = {"Astronomy":89 , "cartography":99}

print(name_marks)


##### removing a key/value in a dictionary######
name_marks.pop("offei")

print(name_marks)


#### getting items##################
name_marks.items()

print(name_marks.items())



####Adding the another student################
name_marks["offei"] = {"Astronomy":89 , "cartography":99}

print(name_marks)

###### Using .get method ##############
name_marks.get("offei")

print(name_marks.get("offei"))

for keys in name_marks.keys():

   print(keys)

for values in name_marks.values():

   print(values)


if "agric" in name_marks:

   print(name_marks["agric"])

try:
   print(name_marks["Maxwell"])
except:
   print("error")

print(name_marks.items())



