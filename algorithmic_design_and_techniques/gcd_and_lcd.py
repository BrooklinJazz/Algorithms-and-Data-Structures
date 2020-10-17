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
    print("succeeded:" if success else "failed:", fn.__name__)

def euclid_gcd(a, b):
    if b == 0:
        return a
    r = a % b
    return euclid_gcd(b, r)

def euclid_fract(a, b):
    d = euclid_gcd(a, b)
    return (int(a / d), int(b / d))

# gcd_test(naive_gcd, 15)
# gcd_test(euclid_fract, 10000)

# ============================
# LCD
# ============================

def naive_lcd(a, b):
    result = None
    d = 1
    while result == None:
        if d % a == 0 and d % b == 0:
            result = d
        d += 1
    return result

def multiplicative_lcd(a, b):
    highest_multiple = max(a, b)
    d = highest_multiple
    result = None
    while result == None:
        if d % a + d % b == 0:
            return d
        d += highest_multiple

def euclid_lcd(a, b):
    d = euclid_gcd(a, b)
    # floor division? makes tests pass
    return int(a * (b // d))

def lcd_test(fn, x = 6, y = 8, lcd = 24):
    a = x
    b = y
    success = True
    result = fn(a, b)
    if result != lcd:
        success = False
    print(fn.__name__, "succeeded" if success else f'failed: {result}')

# lcd_test(naive_lcd)
# lcd_test(multiplicative_lcd, 28851538, 1183019, 1933053046)
# lcd_test(euclid_lcd)
lcd_test(euclid_lcd, 2000000000, 1999999999, 3999999998000000000)
lcd_test(euclid_lcd, 1999999999, 2000000000, 3999999998000000000)
lcd_test(euclid_lcd, 226553150, 1023473145, 46374212988031350)
lcd_test(euclid_lcd, 1023473145, 226553150, 46374212988031350)