def solution(s):
    ind = 0
    cross = 0
    cached = 0
    while ind < len(s):
        if s[ind] == '>':
            cached += 1
        elif s[ind] == '<':
            cross += cached
        ind += 1
    return cross * 2


if __name__ == "__main__":
    print(solution("<<>><"))
