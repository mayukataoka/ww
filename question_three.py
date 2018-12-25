import random


def get_rand_num(n):
    list1 = [random.randint(1, 1000) for _ in range(500)]
    list1.sort()
    return list1[n]


print(get_rand_num(12))
