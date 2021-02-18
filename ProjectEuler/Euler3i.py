# What is the largest prime factor of the number 600851475143 ?


def prime_max(x):
    num = 3
    primes = []
    if x <= 2:
        print(2)
    else:
        while num <= x:
            for n in range(int(num*.7), num):

                if num % n == 0:
                    num+= 2
                    break
            else:
                primes.append(num)
                num += 2
                continue

    print(max(primes))

prime_max(600851475143)


