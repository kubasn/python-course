day_of_week = input('What day of the week is it today')


if day_of_week == 'Monday':
    print("It's monday today")
elif day_of_week == 'Tuesday':
    print("It's tuesday")
else:
    print('Another day of week')
    
# in

table = ['Mark','George','Kathy']

print('Mark' in table)

# ######
# if and in


movies_watched = {"The Matrix", "Green Book", "Her"}
user_movie = input("Enter something you've watched recently: ")

if user_movie in movies_watched:
    print(f"I've watched {user_movie} too!")
else:
    print("I haven't watched that yet.")

# --

number = 7
user_input = input("Enter 'y' if you would like to play: ")

if user_input in ("y", "Y"):
    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("You guessed correctly!")
    elif number - user_number in (1, -1):
        print("You were off by 1.")
    else:
        print("Sorry, it's wrong!")

# --
# -- Part 1 --
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

evens = []
for number in numbers:
    if number % 2 == 0:
        evens.append(number)


# -- Part 2, must be completed before submitting! --
user_input = input("Enter your choice: ")
if user_input == "a":
    print("Add")
elif user_input == 'q':
    print('Quit')