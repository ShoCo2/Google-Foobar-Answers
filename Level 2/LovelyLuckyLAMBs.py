def solution(total_lambs):
    lambs = total_lambs
    minimum = 0
    while lambs >= 0:
        lambs -= pow(2, minimum)
        minimum += 1
    maximum = 1
    nextlambcost = 1
    prevlambcost = 1
    while total_lambs > 0:
        maximum += 1
        total_lambs -= nextlambcost
        tempcost = nextlambcost
        nextlambcost += prevlambcost
        prevlambcost = tempcost
    return maximum - minimum


if __name__ == "__main__":
    print(solution(143))
    print(solution(10))
