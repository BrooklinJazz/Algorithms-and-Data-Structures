def binary_search(search_elements, to_find):

    def F(elements):
        length = len(search_elements)
        low = 0
        high = length - 1
            mid = length / 2
        if elements[mid] > to_find:
            F(elements[:mid], to_find)
        if elements[mid] < to_find:
            return F(elements[mid:], to_find)
    return F(search_elements)
