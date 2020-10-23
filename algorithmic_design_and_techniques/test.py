def matches(expectedFn, actualFn, *args):
    expectedResult = expectedFn(*args)
    actualResult = actualFn(*args)
    if expectedResult != actualResult:
        success = False
    if (success):
        print(actualFn.__name__ + " succeeded")
    else:
        print("expected " + actualFn.__name__ + f'{args} to equal: {expectedResult}. but got {actualResult}')