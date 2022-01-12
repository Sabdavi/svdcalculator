import math


def solve(a, b, c, d):
    if a == 0 and b == 0:
        return [(-d * 1.0) / c]

    elif a == 0:

        d = c * c - 4.0 * b * d
        if d >= 0:
            d = math.sqrt(d)
            x1 = (-c + d) / (2.0 * b)
            x2 = (-c - d) / (2.0 * b)
        else:
            d = math.sqrt(-d)
            x1 = (-c + d * 1j) / (2.0 * b)
            x2 = (-c - d * 1j) / (2.0 * b)

        return [x1, x2]

    f = find_f(a, b, c)
    g = find_g(a, b, c, d)
    h = find_h(g, f)

    if f == 0 and g == 0 and h == 0:
        if (d / a) >= 0:
            x = (d / (1.0 * a)) ** (1 / 3.0) * -1
        else:
            x = (-d / (1.0 * a)) ** (1 / 3.0)
        return [x, x, x]

    elif h <= 0:

        i = math.sqrt(((g ** 2.0) / 4.0) - h)
        j = i ** (1 / 3.0)
        k = math.acos(-(g / (2 * i)))
        l = j * -1
        m = math.cos(k / 3.0)
        n = math.sqrt(3) * math.sin(k / 3.0)
        p = (b / (3.0 * a)) * -1

        x1 = 2 * j * math.cos(k / 3.0) - (b / (3.0 * a))
        x2 = l * (m + n) + p
        x3 = l * (m - n) + p

        return [x1, x2, x3]

    elif h > 0:
        r = -(g / 2.0) + math.sqrt(h)
        if r >= 0:
            s = r ** (1 / 3.0)
        else:
            s = (-r) ** (1 / 3.0) * -1
        t = -(g / 2.0) - math.sqrt(h)
        if t >= 0:
            u = (t ** (1 / 3.0))
        else:
            u = ((-t) ** (1 / 3.0)) * -1

        x1 = (s + u) - (b / (3.0 * a))
        x2 = -(s + u) / 2 - (b / (3.0 * a)) + (s - u) * math.sqrt(3) * 0.5j
        x3 = -(s + u) / 2 - (b / (3.0 * a)) - (s - u) * math.sqrt(3) * 0.5j

        return [x1, x2, x3]


def find_f(a, b, c):
    return ((3.0 * c / a) - ((b ** 2.0) / (a ** 2.0))) / 3.0


def find_g(a, b, c, d):
    return (((2.0 * (b ** 3.0)) / (a ** 3.0)) - ((9.0 * b * c) / (a ** 2.0)) + (27.0 * d / a)) / 27.0


def find_h(g, f):
    return (g ** 2.0) / 4.0 + (f ** 3.0) / 27.0


if __name__ == '__main__':
    n = solve(1, -6, 11, -6)
    for x in n:
        print(x)
