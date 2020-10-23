import time

def matches(expected, actual, *args):
    expectedResult = expected
    actualResult = actual
    if callable(expected):
        expectedResult = expected(*args)
    if callable(actual):
        print("calculating result")
        actualResult = actual(*args)
    if (expectedResult == actualResult):
        print(actual.__name__ + f'{args} succeeded')
    else:
        print("expected " + actual.__name__ + f'{args} to equal: {expectedResult}. but got {actualResult}')

def performance(fn, *args):
    start = time.time()
    fn(*args)
    end = time.time()
    total = end - start
    if (total < 5):
        print(fn.__name__ + " succeeded in ", total)
    else:
        print(fn.__name__ + " failed after", total)


