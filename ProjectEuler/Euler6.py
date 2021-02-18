# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.
def sos(num):
    sum_of_sq = 0
    sq_of_sum = 0
    for n in range(1, num+1):
        sum_of_sq += n**2
        sq_of_sum += n
    print ((sq_of_sum)**2 - (sum_of_sq))

sos(100)
