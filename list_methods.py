### list methods #####

mylist = ["happy", "sad", 1, 2, 4, "blue", 0.3, 0.2, 0.89, "white", 88, "happy"]

list1 = mylist.copy()

print(list1)

##print(list1.clear())


## using extend to add elements to a list #########

list1.extend(["hate", "pull", 7, 0.45, "dull"])

print(list1)


##### counting number of times an element appers in a list #####

list1.count("happy")

print(list1.count("happy"))



### using insert, helps fix values in specific positions #########

list1.insert(1, "ash")

print(list1)


###### remove ###########
list1.remove("happy")

print(list1)


##### using sort ####################################

hislist = [0.9, 0.8, 0.01, 0.65, 0.99, 0.32, 0.21]

hislist.sort()

print(hislist)

####### reverse ###########

herlist = ["gym","muscles", "chest"]

herlist.reverse()

print(herlist)
