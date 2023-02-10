l = ['Charlie','Mark','Harry']
t = ('Charlie','Mark','Harry')             #tuple -you can modifed it or add new elements
s= {'Charlie','Mark','Harry'}              #set - you can modify/add element you can't have duplicates

print(l[0])
print(t[0])

l[0]= 'Bobby'

# add to the end
l.append('Tom')
s.add('Tom')

# print(l)
# print(t)
# print(s)

l.remove('Tom')
s.remove('Tom')

# print(l)
# print(t)
# print(s)

# advanced operations

friends = {'Bob','Charlie','Tom','Adam'}


abroad = {'Bob','Charlie','Mark'}

local_friends = friends.difference(abroad)

# print(local_friends)


# elements that are in either set v (exclude dubiplicate)
global_friends = friends.union(abroad)

print(global_friends)

# elements that are in both sets ^
global_friends = friends.intersection(abroad)

print(global_friends)



