def gen(n):
    for i in range(1, n + 1):
        if i % 2 != 0:
            yield i


gen_10 = gen(10)
print(next(gen_10))
print(next(gen_10))
print(next(gen_10))
print(next(gen_10))
print(next(gen_10))
print(next(gen_10))
print(next(gen_10))
