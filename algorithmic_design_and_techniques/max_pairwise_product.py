# Uses python3
# print("provide array size (for some dumb reason even though we autocalculate it): ")
# size = int(input())
# print('provide the array in format "1 2 3"')
# array = [int(x) for x in input().split()]

def max_pairwise_slow(a):
    n = len(a)

    result = 0

    for i in range(0, n):
        for j in range(i+1, n):
            if a[i]*a[j] > result:
                result = a[i]*a[j]

    return result

def max_pairwise(array):
    """
    docstring
    """
    largestNumberIndex = None
    secondLargestNumberIndex = None
    for index, value in enumerate(array):
        # handle undefined second largest index
        if largestNumberIndex is not None and secondLargestNumberIndex is None:
            secondLargestNumberIndex = index
        # handle undefined largest index
        if largestNumberIndex == None:
            largestNumberIndex = index
        if value > array[largestNumberIndex]:
            secondLargestNumberIndex = largestNumberIndex
            largestNumberIndex = index

    return array[largestNumberIndex] * array[secondLargestNumberIndex]

def big_random_arr():
    return [i for i in range(100000)]

array = [100000, 90000]
# array = big_random_arr()

result = max_pairwise(array)
print(result)

if (result == 100000 * 90000):
    print("all good")
# if max_pairwise(array) == max_pairwise_slow(array):
#     print("all good")
# else:
#     print('fuck')