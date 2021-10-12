import math


def solution(area):
    res = []
    while area > 0:
        sqr = int(pow(math.floor(math.sqrt(area)), 2))
        res.append(sqr)
        area -= sqr
    return res


if __name__ == "__main__":
    print(solution(15324))
