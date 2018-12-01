from time import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, *kwargs)
        print("solution time is: {}".format(time() - start))
        return result
    return wrapper


