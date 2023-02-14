# numbers = [1,2,3]
# doubled = []

# for num in numbers:
#     doubled = numbers.append(num*2)

# or

numbers = [1,2,3]
doubled = [x*2 for x in numbers]

print(doubled)

friends= ['Mark','Mary','Micheal','Sam','Tom']
starts_s = [friend for friend in friends if friend.startswith('M') ]
print(starts_s)

