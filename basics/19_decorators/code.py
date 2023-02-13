import functools






def make_secure(access_level):
    def decorator(func):
        @functools.wraps(func)
        def secure_func(*args,**kwargs):
            if user['access_level'] == access_level:
                return func(*args,**kwargs)
            else:
                return f'No {access_level} permission.' 
        return secure_func
    return decorator











# def make_secure(access_level):
#     # it tells that secure_function is wrap for func, to not lose the name of get_admin_password
#     def decorator(func):
#         @functools.wraps(func)
#         def secure_function(*args, **kwargs):
#             if user['access_level'] == 'admin':
#                 return func(*args, **kwargs)
#             else:         
#                 return f'No admin permision'

#         return secure_function
    
#     return decorator

    
# @make_secure
# def get_admin_password(panel):
#     if panel == 'admin':
#         return '1234'
#     elif panel == 'billing':
#         return 'super_secure_password'


# get_admin_password = make_secure(get_admin_password)
# user ={'username':'jose','access_level':'guest'}

# it's the same

user ={'username':'jose','access_level':'admin'}


# print(get_admin_password().__name__)

@make_secure('admin')
def get_admin_password():
    return '1234'

@make_secure('name')
def get_dashboard_password():
    return 'super_secure_password'


print(get_admin_password())




