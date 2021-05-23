from math import sqrt


def conversion_difference(n1: int, n2: int, conv1: float, conv2: float, trust: int):
    coefficient = 0
    if trust == 90:
        coefficient = 1.645
    elif trust == 95:
        coefficient = 1.96
    elif trust == 99:
        coefficient = 2.575
    left = (conv2 - conv1 - coefficient * sqrt(((conv1 * (1 - conv1)) / n1) + ((conv2 * (1 - conv2)) / n2))) * 100
    right = (conv2 - conv1 + coefficient * sqrt(((conv1 * (1 - conv1)) / n1) + ((conv2 * (1 - conv2)) / n2))) * 100
    left_rounded = round(left, 2)
    right_rounded = round(right, 2)
    result = "Confidence interval: [{left}%; {right}%]".format(left=left_rounded, right=right_rounded)
    if (left_rounded < 0 < right_rounded) or (left_rounded < 0 < right_rounded):
        significance = "No, the difference is statistically insignificant"
    else:
        significance = "Yes, the difference is statistically significant"

    return result + '. ' + significance


def conficence_interval(n: int, cr: float, trust: int):
    """
    :param n: размер выборки
    :param cr: оценка конверсии
    :param trust: уровень доверия

    :return: доверительный интервал
    """
    value = 0
    if trust == 95:
        value = 1.96

    left = cr - value * sqrt((cr * (1-cr) / n))
    right = cr + value * sqrt((cr * (1-cr) / n))

    rounded_left = round(left * 100, 3)
    rounded_right = round(right * 100, 3)

    print('[{l}%; {r}%]'.format(l=rounded_left, r=rounded_right))


def sample_size(cr: float, conf_int: float, trust: int):
    """
    :param cr: оценка конверсии
    :param conf_int: точность
    :param trust: уровень доверия

    :return: размер выборки
    """
    value = 0
    if trust == 95:
        value = 1.96

    n = value ** 2 * ((cr * (1-cr)) / (conf_int ** 2))

    rounded_n = round(n)

    return rounded_n


if __name__ == "__main__":
    result = conversion_difference(3500, 3500, 0.174, 0.154, 95)
    print(result)
