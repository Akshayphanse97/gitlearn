import time
from functools import wraps
def time_calculate(function):
    t1=time.time()
    @wraps(function)
    def wrapped_function(*args,**kwargs):
        print(f" {function.__name__}")
        var=function(*args,**kwargs)
        t2= time.time()
        
        total = t2-t1
        print(total)
        return var
    return wrapped_function

@time_calculate
def square(n):
    return [i**2 for i in range(1,n+1)]

square(1000)
