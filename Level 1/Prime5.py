def solution(i):
    n = 2
    primes = '2'
    foundprime = False

    while len(primes) < (i + 5):
        while not foundprime:
            n += 1
            foundprime = True
            for j in range(2, (n // 2) + 1):
                if n % j == 0:
                    foundprime = False
                    break
        primes += str(n)
        foundprime = False

    return primes[i:i+5]
