# Write GCD as linear combination of a and b (a>b) (Extended Euclidean algorithm)


def find_quotients(a, b):
    x = a
    y = b
    quotients = []
    while y != 0:
        quotients.append(x // y)
        r = x % y
        x = y
        y = r
    return quotients


def linear_combination(a, b):
    s = [1, 0]
    t = [0, 1]
    quotients = find_quotients(a, b)
    for i in range(2, len(quotients) + 1):
        s.append(s[i - 2] - quotients[i - 2] * s[i - 1])
        t.append(t[i - 2] - quotients[i - 2] * t[i - 1])
    return [s[-1], t[-1]]


if __name__ == "__main__":
    a, b = list(map(int, input().split()))
    check = a > b
    if not check:
        a, b = b, a
    x, y = linear_combination(a, b)
    if not check:
        x, y = y, x
    print(x, y)
