# Uses python3
# size = int(input())
# print('provide the array in format "1 2 3"')
# array = [int(x) for x in input().split()]
from random import randint

def max_pairwise_slow(a):
    n = len(a)

    result = 0

    for i in range(0, n):
        for j in range(i+1, n):
            if a[i]*a[j] > result:
                result = a[i]*a[j]
    return result

def max_pairwise(array):
    largestNumberIndex = None
    secondLargestNumberIndex = None
    for index, value in enumerate(array):
        guaranteedIndex = largestNumberIndex if largestNumberIndex is not None else index
        if value >= array[guaranteedIndex]:
            largestNumberIndex = index
    for index, value in enumerate(array):
        guaranteedIndex = secondLargestNumberIndex if secondLargestNumberIndex is not None else index
        if value >= array[guaranteedIndex] and index != largestNumberIndex:
            secondLargestNumberIndex = index
    return array[largestNumberIndex] * array[secondLargestNumberIndex]

def generate_test():
    max = 10000
    size = randint(2, max)
    random_arr = [randint(0, max) for _ in range(size)]
    fast_result = max_pairwise(random_arr)
    slow_result = max_pairwise_slow(random_arr)
    if (fast_result == slow_result):
        print("all good")
    else:
        print('failed on: ', size, random_arr)
        print("fast", fast_result)
        print("slow", slow_result)

while True:
    generate_test()