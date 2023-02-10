size_input = input("How big is your house (in square feet): ")
square_feet =int(size_input)

calc = square_feet * 10.8

print(calc)

print(f'you provide {square_feet}, it is {calc:.2f} square metres.')