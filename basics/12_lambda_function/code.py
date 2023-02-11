# doesn't have name and it's used for return values (almost never used for perform actions)


add =lambda x,y : x+y

print(add(5,6))


print((lambda x,y : x+y)(5,12))


# numbers = [1,2,3,4,5]
# doubled = [x*2 for x in numbers]
# print(doubled)

def double(x):
    return x*2


# numbers=[1,2,3,4,5]
# doubled = [double(x) for x in numbers]
# print(doubled)

numbers=[1,2,3,4,5]
doubled = map(double,numbers)
print(doubled) #map object adress?
# converting to list
doubled = list(doubled)
print(doubled) #list

# or with lambda function

numbers1 = [1,2,3,4,5]
doubled1 = map(lambda x:x*2,numbers1)
print(list(doubled1))


