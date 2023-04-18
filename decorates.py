from functools import wraps
def decorates_function(function):
    @wraps(function)
    def wrapper_function(*args,**kwargs):
        print(f"you call {function.__name__} function") 
        print(f" {function.__doc__}")
        return function(*args,**kwargs)
    return wrapper_function


@decorates_function
def add(a,b):
    '''' this is function takes tow number as parameter and return their number'''
    return a+b

print(add(5,6))