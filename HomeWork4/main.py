import math


def mean(values):
    return sum(values) / len(values)


def correlation(x, y):
    numerator = sum(map(lambda xi, yi: (xi - mean(x)) * (yi - mean(y)), x, y))
    denominator_1 = math.sqrt(sum(map(lambda xi: (xi - mean(x)) ** 2, x)))
    denominator_2 = math.sqrt(sum(map(lambda yi: (yi - mean(y)) ** 2, y)))

    if denominator_1 == 0 or denominator_2 == 0:
        return 0

    corr = numerator / (denominator_1 * denominator_2)
    return corr


array1 = [1, 3, 7, 15, 52]
array2 = [2, 3, 10, 47, 8]

print(f"Корреляция Пирсона: {correlation(array1, array2)}")
