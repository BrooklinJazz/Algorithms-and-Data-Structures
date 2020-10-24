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
