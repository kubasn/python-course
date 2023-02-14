from libs.operations import list_avg
from module import list_avg as operation



print(list_avg(1,2,3,4,5))

print(operation(1,2,3,4,5))




# Consider the following package structure:

# my_project/
#     package1/
#         __init__.py
#         module1.py
#     package2/
#         __init__.py
#         module2.py

# In the module2.py file, you can import the module1.py file using a relative import like this:

# from ..package1 import module1

# The two dots `..` indicate that you want to go up one level in the package hierarchy, 
# and then into the `package1` package to import the `module1` module.

# Another example:

# In module1.py
# def my_func():
#     return "Hello from module1"

# # In module2.py
# from . import module1

# def my_func():
#     return "Hello from module2"

# def call_module1_func():
#     return module1.my_func()

# In this example, the single dot `.` before `import module1` indicates that you want to import the `module1` module 
# from the same package as the current module (`module2`). When you run the `call_module1_func` function, it will return 
# the output of the `my_func` function in `module1`.