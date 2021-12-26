list1 = ["hi", int, 888, 7, 78, 8, 2, 4, 1, 3, "who", "*", 6]
dict1 = {}
for typ in list1:
    #print(type(typ))
    if type(typ) == int and typ>6:
        print(typ)
        #dict1[typ] = type(typ)
#print(dict1)