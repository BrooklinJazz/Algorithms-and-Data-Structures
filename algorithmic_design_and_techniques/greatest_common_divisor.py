def naive_gcd(a, b):
    result = 1
    for d in range(1, min(a, b) + 1):
        if a % d == 0 and a % d == 0:
            result = d
    return (int(a / result), int(b / result))

# their version, I'm not sure the if d > gcd is necessary since it counts up
def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

def gcd_test(fn, times):
    a = 1
    b = 2
    success = True
    for _ in range(times):
        a = a * 2
        b = b * 2
        if fn(a, b) != (1, 2):
            success = False
            print('failed on: ', a, b, fn(a, b))
    print("succeeded: " if success else "failed: ", fn.__name__)


def euclid_gcd(a, b):
    if b == 0:
        return a
    r = a % b
    return euclid_gcd(b, r)

def euclid_fract(a, b):
    d = euclid_gcd(a, b)
    return (int(a / d), int(b / d))

gcd_test(naive_gcd, 15)
gcd_test(euclid_fract, 10000)

