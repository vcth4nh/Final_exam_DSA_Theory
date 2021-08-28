import numpy as np
import re


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    YEALLOW = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def left(node):
    return node * 2


def right(node):
    return node * 2 + 1


# def heapify(remain, lastPos, node):
#     L = left(node) + 1
#     R = right(node) + 1
#     if L <= lastPos and remain[L] > remain[node]:
#         largest = L
#     else:
#         largest = node
#     if R <= lastPos and remain[R] > remain[largest]:
#         largest = R
#     if largest != node:
#         remain[node], remain[largest] = remain[largest], remain[node]
#         heapify(remain, lastPos, largest)

def show(formatType, remain, node, largest, lastPos):
    print("[", end="")
    for i in range(1, lastPos + 1):
        if i == node:
            print(f"{formatType}{remain[i]}{bcolors.ENDC}", end="")
        elif i == largest:
            print(f"{formatType}{remain[i]}{bcolors.ENDC}", end="")
        else:
            print(remain[i], end="")
        if i == lastPos:
            print("]")
        else:
            print(", ", end="")


def heapify1(remain, lastPos, node=1, flag=True):
    L = left(node)
    R = right(node)
    if L <= lastPos and remain[L] > remain[node]:
        largest = L
    else:
        largest = node
    if R <= lastPos and remain[R] > remain[largest]:
        largest = R
    if largest != node:
        if flag:
            show(bcolors.UNDERLINE, remain, node, largest, lastPos)
        remain[node], remain[largest] = remain[largest], remain[node]
        if flag:
            show(bcolors.OKGREEN, remain, node, largest, lastPos)
        heapify1(remain, lastPos, largest)


# def buildHeap0(remain, lastPos):
#     print(lastPos)
#     for node in reversed(range(lastPos // 2)):
#         heapify(remain, lastPos, node)
#     return remain


def buildHeap1(remain, lastPos):
    # print(remain[1:])
    # print(lastPos)
    # print(list(reversed(range(1, lastPos // 2 + 1))))
    for node in reversed(range(1, lastPos // 2 + 1)):
        heapify1(remain, lastPos, node)
    return remain


def insert(remain, val):
    remain.append(val)
    buildHeap1(remain, len(remain) - 1)


def extractMax(remain, i=0, lastPos=-1):
    lastPos = len(remain) - 1 if lastPos == -1 else lastPos
    max = remain[1]
    remain[1] = remain[lastPos - i]
    heapify1(remain, lastPos - i, flag=False)
    return max


def heapSort(remain, lastPos):
    for i in range(lastPos):
        print(str(i) + ":")
        print(remain[1:])
        remain[lastPos - i] = extractMax(remain, i, lastPos)
    print("-" * 20 + "\nResult:")
    return remain[1:]


org = "15, 13, 9, 5, 12, 8, 7, 4, 0, 6, 2, 1"  # 10
org = [int(x) for x in re.findall(r'\d+', org)]
org = [np.nan] + org
tmp = org[:]

# print(buildHeap0(org, len(org) - 1))

buildHeap1(tmp, len(tmp) - 1)
print("Extract max:")
print(extractMax(tmp))
print("Insert value:")
insert(tmp, 10)
print(tmp[1:])
print("Sort:")
print(heapSort(tmp, len(tmp) - 1))
