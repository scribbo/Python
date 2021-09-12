src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [el for el in src if src.count(el) == 1]
# print(result)


my_dict = {k: n for k, n in zip(src, range(len(src)))}
index = [my_dict.pop(src[i], -1) for i in range(len(src)) if my_dict.get(src[i]) != i]
result = list(my_dict.keys())

print(result)
