

points = [1, 2, 5, 10, 20, 50, 100, 200]
points = [i for i in reversed(points)]


def func(num):
    operators = [None for i in points]
    start_index = 0
    result = []

    while start_index >= 0:
        pre_sum = sum([operators[i] * points[i] for i in range(start_index)])
        res = num - pre_sum
        val = 0
        if operators[start_index] == None:
            operators[start_index] = int(
                float(num) / float(points[start_index]))
        elif operators[start_index] < 0:
            operators[start_index] = None
            start_index -= 1
            if start_index < 0:
                break
            operators[start_index] -= 1
        else:
            val = operators[start_index] * points[start_index]
            if res == val:
                result.append(operators)
                operators[start_index] -= 1
            elif res - val > 0:
                if start_index == len(points) - 1:
                    operators[start_index] -= 1
                else:
                    start_index += 1
            elif res - val < 0:
                operators[start_index] -= 1

    return len(result)


print func(200)
