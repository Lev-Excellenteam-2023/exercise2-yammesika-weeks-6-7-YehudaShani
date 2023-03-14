
# write a function that receives another function and other parameters
# the function will calculate how long f takes to run with those parameters
# and return the time it took to run


def timer(f, *args):
    import time
    start = time.time()
    f(*args)
    end = time.time()
    return end - start


print(timer(sum, range(1000000)))
