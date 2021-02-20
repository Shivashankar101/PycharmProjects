# What is the value of the first triangle number to have over
# five hundred divisors?

def triangular_no_gen():
    n = 1
    sum = 0

    while True:
        sum += n
        n += 1
        yield sum


def nth_tri_no_gen(n):

    tri_no = n*(n+1)/2
    return tri_no

def factors_gen(num):
    factors = []
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            yield i
            factors.append(i)
    for factor in factors:
        yield factor

def divisors(n):
    return [d for d in factors_gen(n)]


no_divs = 0
i = 1
while no_divs < 500:
    i += 1
    tnum = nth_tri_no_gen(i)
    divs = divisors(tnum)
    no_divs = len(divs)

print(tnum)





