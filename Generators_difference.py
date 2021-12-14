
def countdown(num):
    result = []
    while num != 0:
        result.append(num - 1)
        num -= 1
    return result

# Generator function allows us to access data in between process of execution
def gen_countdown(num):
    while num != 0:
        yield num - 1
        num -= 1

# out results first func
print(countdown(7))

# out results of generator in console
n = gen_countdown(5)
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))

# stop iteration error
# print(next(n))

for i in gen_countdown(8):
    print(i)


