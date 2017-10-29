primes = [2, 3, 5, 7]
truncatables = []


def isPrime(o):

    n = int(o)

    if n in primes:
        return True

    if n == 1:
        return False

    
    for p in primes:
        if n % p == 0:
            return False

    primes.append(n)
    return True


def l_to_r_truncate(n):
    print n
    if not isPrime(n):
        return False

    if not len(n) == 1:
        l_to_r_truncate(n[-(len(n) - 1):])
    else:
        isPrime(n)


def r_to_l_truncate(n):
    if len(n) == 1:
        return isPrime(n)
    elif isPrime(n):
        r_to_l_truncate(n[:-1])
    else:
        return False



def get_the_answer():
    i = 8
    while len(truncatables) < 1:
        print i
        if isPrime(i):
            print l_to_r_truncate(str(i))
            print r_to_l_truncate(str(i))
            if l_to_r_truncate(str(i)) and r_to_l_truncate(str(i)):
                truncatables.append(i)

        i += 1

    print truncatables

for n in range(1, 4000):
    isPrime(n)

print primes

print r_to_l_truncate('23')