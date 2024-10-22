my_dict={"januari": 31, "febuari": 28, "march":30 }
print(my_dict)
print(my_dict["januari"])
print(my_dict.get("april"))
my_dict["april"]=32
my_dict["may"]=33
del my_dict["march"]
print(my_dict)
my_set = {1.5, 3, 6,"list", 3,6,7,"list"}
print(my_set)
my_set.add((1,2,3,4))
my_set.add(True)
my_set.remove(1.5)
print(my_set)