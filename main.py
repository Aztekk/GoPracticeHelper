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
