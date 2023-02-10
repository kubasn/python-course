person = ('Bob',42,'Mechanic')

name, _, profesion = person

print(name,profesion)

# head - first value, tail - rest values
head, *tail = [1,2,3,4,5]
print(head,tail)

*head, tail = [1,2,3,4,5]
print(head,tail)