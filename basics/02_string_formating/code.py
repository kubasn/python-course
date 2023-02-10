name = "Henry"
greeting = "Hello, Mark"

print(greeting)

greeting = f"Hello, {name}"

print(greeting)


# formatting


name = "George"
greeting = "Hello, {}"
with_name = greeting.format(name)
print(with_name)

# long string formatting
date = "Friday"
longer_phrase = 'Hello {}, today is {}'
with_name_date = longer_phrase.format(name,date)
