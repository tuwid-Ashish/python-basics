import time
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Elapsed time to ran function {func.__name__}: {end-start}")
        return result
    return wrapper

@timer
def ex_func(n):
    return time.sleep(n)

ex_func(2)

def debug(func):
    def wrapper(*args,**kwargs):
        args_value = " , ".join(str(arg) for arg in args)
        kwargs_value = " , ".join(f"{k} = {v}" for k,v in kwargs.items()) 
        print(f"In function {func.__name__} the args =  {args_value if len(args_value)>0 else "no arguments"} and kwargs = {kwargs_value if len(kwargs_value)>0 else "no keyword arguments"}")
    return wrapper

@debug
def add(a,b):
    return a+b

add(2,3, age = 21)

def cache(func):
    cache_value = {}
    print(cache_value)
    def wrapper(*args, **kwargs):
         if args in cache_value:
             return f" this out from cache_stack :{cache_value[args], cache_value}"
         
         results = func(*args)
         cache_value[args] = results
         return results
    return wrapper
        # key = (args, tuple(kwargs.items()))
        # if key not in wrapper.cache:
        #     wrapper.cache[key] = func(*args, **kwargs)
        # return wrapper.cache[key]
@cache
def sumji(a,b):
     return a+b

print(sumji(2,3))
print(sumji(2,3))
print(sumji(5,8))