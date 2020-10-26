
def money_change(n):
    (tens, remainder) = divmod(n, 10)
    (fives, ones) = divmod(remainder, 5)
    return tens + fives + ones


def get_capacity_and_items(data):
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    items = []
    for w, v in zip(weights, values):
        items.append({
            "weight": w,
            "value": v,
            "ratio": v / w})

    def byRatio(item):
        return item["ratio"]
    items.sort(key=byRatio, reverse=True)
    return capacity, items


def maximum_loot(data):
    capacity, items = get_capacity_and_items(data)
    result = 0
    remainingCapacity = capacity
    for item in items:
        allowed_weight = min(remainingCapacity, item["weight"])
        remainingCapacity -= allowed_weight
        result += item["ratio"] * allowed_weight
    return result


def maximum_advertising_revenue(slots, profit_per_click, clicks_per_day):
    profit_per_click.sort()
    clicks_per_day.sort()
    result = 0
    for profit, clicks in zip(profit_per_click, clicks_per_day):
        result += profit * clicks
    return result


def low_high_values(segments):
    lowest, highest = segments[0][0], segments[0][1]
    for s in segments:
        lowest = min(lowest, s[0])
        highest = max(highest, s[1])
    return (lowest, highest)


def sort_segments(segments):
    clone = segments

    def lowest_start(segment):
        return segment[0]
    clone.sort(key=lowest_start)
    return clone


# def collect_signatures(segments):
#     lowest, highest = low_high_values(segments)
#     sorted_segments = sort_segments(segments)
#     marks = []
#     for i in range(highest - lowest):
#         n = lowest + i


def is_overlapping(mark, segment):
    return mark >= segment[0] and mark <= segment[1]


def number_of_overlapping(mark, segments):
    result = 0
    for s in segments:
        if is_overlapping(mark, s):
            result += 1
    return result

# def number_of_new_overlapping(mark, marks, segments):
#     def by_is_handled():

#     filtered_segments = filter()


def is_segment_handled(marks, s):
    result = False
    for m in marks:
        if s[0] <= m and s[1] >= m:
            result = True
    return result


# def collect_signatures(unsorted_segments):
#     marks = []
#     segments = sort_segments(unsorted_segments)
#     for s in segments:
#         best_mark = 0
#         for i in range((s[1] + 1) - s[0]):
#             m = i + s[0]
#             overlapping = number_of_overlapping(m, segments)
#             if overlapping >= best_mark:
#                 best_mark = m
#         if best_mark not in marks and not is_segment_handled(marks, s):
#             marks.append(best_mark)

#     return marks


# def has_disjointed(marks, segments):
#     result = False
#     smallest = min(marks)
#     biggest = max(marks)
#     for s in segments:
#         if s[0] > biggest or s[1] < smallest:
#             result = True
#     return result

def has_disjointed(marks, segments):
    disjointed = False

    def no_marks_between_segment(segment):
        result = True
        for m in marks:
            if segment[0] <= m and segment[1] >= m:
                result = False
        return result

    for s in segments:
        if no_marks_between_segment(s):
            disjointed = True
    return disjointed


def get_smallest_right_value(segments):
    result = segments[0][1]
    for s in segments:
        result = min(result, s[2])
    return result


def collect_signatures(segments):
    marks = []
    while segments != []:
        smallest_right = segments[0][1]
        for s in segments:
            smallest_right = min(smallest_right, s[1])
        marks.append(smallest_right)

        def right_is_above_smallest(s):
            return s[0] > smallest_right

        segments = list(filter(right_is_above_smallest, segments))
    return marks


def collect_signatures_broken(segments):
    low, high = low_high_values(segments)
    all_marks = list(range(low, high+1))
    marks = list(range(low, high+1))
    for m in all_marks:
        marks.remove(m)
        if has_disjointed(marks, segments):
            marks.append(m)
    return marks


def collect_signatures_from_string(str):
    n, *data = map(int, str.split())
    segments = list(map(lambda x: [x[0], x[1]], zip(data[::2], data[1::2])))
    return collect_signatures(segments)


def optimal_summands(n):
    arr = []
    i = 0
    while True:
        i += 1
        if n - i <= i:
            arr.append(n)
            break
        else:
            arr.append(i)
            n -= i
    return arr


def is_greater_digit(a, b):
    aStr = str(a)
    bStr = str(b)
    smallest_length = min(len(aStr), len(bStr))
    for i in range(smallest_length):
        x = int(aStr[i])
        y = int(bStr[i])
        if x > y:
            return True
        elif x < y:
            return False
    return True


def maximize_salary(digits):
    answer = ''
    while digits != []:
        maxDigit = 0
        for d in digits:
            if is_greater_digit(int(d), maxDigit):
                maxDigit = int(d)
        answer += str(maxDigit)
        digits.remove(str(maxDigit))

    return int(answer)

# def maximize_salary(numbers):
#     strings = list(map(str, numbers))

#     def highest(s):
#         return int(s)

#     def digit_count(s):
#         return len(s)

#     def highest_start(s):
#         return int(s[0])
#     strings.sort(key=highest, reverse=True)
#     strings.sort(key=digit_count)
#     strings.sort(key=highest_start, reverse=True)
#     return int(''.join(strings))
