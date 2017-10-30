primes = [2, 3, 5, 7]
truncatables = []


def isPrime(o):

    n = int(o)

    if n < primes[-1] and n in primes:
        return True
    elif n < primes[-1] and n not in primes:
        return False

    if n == 1:
        return False
    
    for p in primes:
        if n % p == 0:
            return False

    primes.append(n)
    return True


def l_to_r_truncate(n):
    if len(n) == 1 and isPrime(n):
        return True

    if not isPrime(n):
        return False

    if not len(n) == 1:
        return l_to_r_truncate(n[-(len(n) - 1):])


def r_to_l_truncate(n):
    if len(n) == 1:
        return isPrime(n)
    elif isPrime(n):
        return r_to_l_truncate(n[:-1])
    else:
        return False


def get_the_answer():
    i = 8
    while len(truncatables) < 11:
        print i
        if isPrime(i):
            if check_initial_digits(i):
                if l_to_r_truncate(str(i)) and r_to_l_truncate(str(i)):
                    truncatables.append(i)

        i += 1

        print truncatables
    print truncatables


def check_initial_digits(n):
    first = get_digit_at_positions(n, 0)
    last = get_digit_at_positions(n, -1)
    return first in primes and last in primes

def get_digit_at_positions(n, position):
    return int(str(n)[position])

for n in range(1, 4000):
    print ":" + str(n) + " " + str(isPrime(n))


get_the_answer()