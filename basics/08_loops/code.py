friends = ['Mark','Ted','Jerry']

for friend in friends:
    print(f'friend: {friend}')


points = [35,234,756,123]
summary=0

for point in points:
    summary += point

print(summary)

# or you can write
print(sum(points))

# length
print(len(points))

# avg
print(sum(points)/len(points))