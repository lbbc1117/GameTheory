from random import uniform, triangular
from statistics import mean


def float_range(start, stop, steps):
    return [start + float(i) * (stop - start) / (float(steps) - 1) for i in range(steps)]


VALUES = float_range(0, 1, 11)
print("VALUES: {}".format(VALUES))
GAME_TOTAL = 1000


def get_usefulness(v1, v2):
    return 0.5 + 0.5 * (v1 - v2) - 1.5 * v1 * v2


def print_result(result, distribution, args):
    print("*" * 50)
    print("Result with {0}{1}".format(distribution, args))
    print("*" * 50)
    for v1 in VALUES:
        _key = str(v1)
        print("value: {0} -- avg: {1} | max: {2}".format(
            v1, format(result[_key]["avg"], ".2f"), format(result[_key]["max"], ".2f")))
    print("")


def simulate(distribution, args):
    result = {}
    for v1 in VALUES:
        _key = str(v1)
        result[_key] = {}
        result[_key]["max"] = -99
        result[_key]["avg"] = []
        for _ in range(GAME_TOTAL):
            v2 = distribution(*args)
            usefulness = get_usefulness(v1, v2)
            result[_key]["max"] = result[_key]["max"] if usefulness < result[_key]["max"] else usefulness
            result[_key]["avg"].append(usefulness)
        result[_key]["avg"] = mean(result[_key]["avg"])
    print_result(result, distribution.__name__, args)


if __name__ == "__main__":
    # 均匀分布
    simulate(uniform, (0, 1))
    # 三角分布
    modes = float_range(0, 1, 5)
    for mode in modes:
        simulate(triangular, (0.0, 1.0, mode))
