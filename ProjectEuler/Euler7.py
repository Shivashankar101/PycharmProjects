#10001st prime
def next_prime():

    x = 3
    while x > 2:
        for i in range(2, x):
            if x%i == 0:
                x += 2
                break
        else:
            yield(x)
            x += 2

def the_prime(num):
    y = next_prime()
    for n in range(num):
        x = next(y)
    print(x)

the_prime(10001)




