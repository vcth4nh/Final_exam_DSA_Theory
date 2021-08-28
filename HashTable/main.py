import numpy as np
import re
import random

"""sequence of keys"""
# s = random.sample(range(1, 1000), 11)
s = "2341, 4234, 2839, 430, 22, 397, 3920"
"""table size"""
n = 11
"""c1 and c2 for quadratic probing"""
c1 = 1
c2 = 1
"""second hash function for double hashing"""


def h2(k):
    return (2 * k - 1) % 7


"""output file"""
out = open("res.txt", "w")


def init():
    return [np.nan for _ in range(n)]


def init_chain():
    return [[np.nan for _ in range(n)]]


"""functions for linear probing"""


def linear_prob(k, n, res):
    hashRes = k % n
    while not np.isnan(res[hashRes]):
        # print(str(i), str(res[hashRes]), str(hashRes), sep=" : ")
        hashRes = (hashRes + 1) % n
    return hashRes


"""functions for quadratic probing"""


def quadratic_prob(k, n, res):
    i = 0
    hashRes = ((k % n) + c1 * i + c2 * i * i) % n
    while not np.isnan(res[hashRes]):
        # print(str(i), str(res[hashRes]), str(hashRes), sep=" : ")
        i += 1
        hashRes = ((k % n) + c1 * i + c2 * i * i) % n
    return hashRes


"""functions for double hashing"""


def h1(k, n):
    return k % n


def double_hashing(k, n, res):
    i = 0
    hash1 = h1(k, n)
    hash2 = h2(k)
    hashRes = (hash1 + i * hash2) % n
    while not np.isnan(res[hashRes]):
        # print(str(i), str(res[hashRes]), str(hashRes), sep=" : ")
        i += 1
        hashRes = (hash1 + i * hash2) % n
    return hashRes


def chaining(s, res):
    row = 0
    for i in s:
        level = 0
        hashRes = i % n
        while not np.isnan(res[level][hashRes]):
            level += 1
            if level > row:
                res.extend(init_chain())
                row += 1
        res[level][hashRes] = i


"""core function"""


def loop(hashType, s, res, id):
    types = {
        1: "Linear",
        2: "Quadratic",
        3: "Double"
    }
    print(f"\n{types.get(id)} probing:")
    print(res)
    for i in s:
        if np.isnan(res).any():
            # print("computing hash for " + str(i))
            res[hashType(i, n, res)] = i
            print(res)
        else:
            print("Hashtable is full")


def start(s):
    resC = init_chain()
    resL = init()
    resQ = init()
    resD = init()

    loop(linear_prob, s, resL, 1)
    loop(quadratic_prob, s, resQ, 2)
    loop(double_hashing, s, resD, 3)
    chaining(s, resC)

    print("\n\n-------------------------\nresult:")
    print("Chaining:")
    for _ in resC:
        for __ in _:
            print(str(__).ljust(6, " "), end="")
        print()
    print("\nLinear probing:", resL,
          "\nQuadratic probing:", resQ,
          "\nDouble probing:", resD, sep="\n")


s = [int(x) for x in re.findall(r'\d+', s)]
print(s)

start(s)
out.close()
