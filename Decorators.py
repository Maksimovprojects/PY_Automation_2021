from datetime import datetime

# Decorators

def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        print(datetime.now() - start)
        return result
    return wrapper

@timeit
def gen_even1(num):
    l = []
    for i in range(num):
        if i % 2 == 0:
            l.append(i)
    return l

@timeit
def gen_even2(num):
    l = [x for x in range(num) if x % 2 == 0]
    return l

t1 = gen_even1(100)
t2 = gen_even2(300)

l1 = timeit(gen_even1)
l2 = timeit(gen_even1)(10)  # => wrapper(10) => one(10)
print(type(l1), l1.__name__)
