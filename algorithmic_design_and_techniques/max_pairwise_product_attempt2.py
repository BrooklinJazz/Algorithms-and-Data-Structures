# Uses python3
# print("provide array size (for some dumb reason even though we autocalculate it): ")
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


def generate_failing_test():
    # failing_arr = [709, 100, 649, 639, 989, 564, 53, 290, 285, 765, 389, 401, 634, 114, 80, 473, 822, 855, 12, 423, 462, 70, 473, 984, 948, 147, 43, 783, 107, 134, 585, 944, 716, 64, 81, 194, 452, 133, 897, 98, 688, 867, 920, 611, 733, 830, 428, 636, 123, 371, 240, 708, 811, 382, 537, 786, 143, 37, 421, 600, 228, 658, 93, 439, 520, 945, 430, 786, 322, 47, 452, 935, 400, 809, 42, 858, 377, 154, 454, 559, 526, 622, 462, 630, 56, 294, 661, 875, 480, 227, 22, 618, 885, 421, 560, 608, 255, 361, 966, 291, 90, 420, 598, 650, 215, 512, 342, 375, 142, 264, 784, 8, 662, 777, 792, 186, 372, 372, 568, 497, 274, 946, 578, 731, 297, 172, 424, 130, 915, 166, 902, 15, 202, 540, 539, 737, 79, 695, 206, 805, 404, 555, 486, 868, 128, 58, 665, 443, 82, 125, 271, 139, 934, 572, 16, 768, 973, 867, 703, 699, 378, 581, 992, 260, 645, 796, 6, 549, 711, 797, 0, 110, 911, 850, 442, 806, 173, 41, 149, 947, 950, 420, 453, 174, 882, 754, 51, 608, 642, 705, 112, 351, 521, 744, 773, 618, 828, 342, 180, 188, 219, 248, 500, 94, 695, 60, 980, 983, 589, 368, 182, 454, 936, 104, 598, 998, 665, 348, 295, 841, 652, 757, 169, 797, 512, 538, 899, 286, 203, 410, 839, 98, 832, 525, 224, 830, 423, 997, 813, 263, 659, 924, 937, 62, 241, 946, 157, 675, 266, 829, 733, 699, 511, 931, 747, 520, 2, 767, 317, 698, 912, 719, 437, 746, 657, 370, 310, 401, 19, 118, 648, 590, 536, 479, 559, 391, 953, 756, 87, 974, 855, 305, 6, 728, 618, 896, 115, 807, 294, 297, 974, 418, 424, 465, 831, 297, 397, 124, 968, 697, 864, 248, 998, 935, 362, 620, 339, 941, 144, 663, 714, 329, 57, 729, 151, 682, 613, 960, 14, 171, 1000, 871, 350, 151, 314, 812, 435, 165, 373, 827, 789, 332, 600, 602, 756, 984, 514, 844, 43, 893, 52, 104, 80, 403, 323, 481, 923, 172, 198, 75, 420]
    failing_arr = [979, 842, 71, 340, 176, 9, 629, 253, 509, 912, 632, 432, 293, 424, 79, 337, 684, 653, 821, 795, 635, 242, 431, 724, 353, 394, 661, 859, 799, 446, 606, 851]
    if(max_pairwise(failing_arr) == max_pairwise_slow(failing_arr)):
        print("all good")
    else:
        print('fuck')

generate_failing_test()
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