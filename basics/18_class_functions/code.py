# def divide(dividend,divisor):
#     if divisor == 0:
#         raise ZeroDivisionError('Dvisior cannot be 0')
    
#     return dividend/divisor



# def calculate(*args,operator):
#     return operator(*args)


# result = calculate(1, 2, operator=divide())



def search(sequence,expected,finder):
    for elem in sequence:
        if(finder(elem) == expected):
            return elem
    raise RuntimeError(f'Cannot find an element with {expected}.')


friends = [
    {'name':'Rolf','age':40},
    {'name':'Mark','age':55},
    {'name':'Ted','age':30},
    ]


def get_friend_name(elem):
    return elem['name']

print(search(friends,'Rolf',lambda x: x['name']))