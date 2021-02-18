
# Find the sum of all the primes below two million.
# def prime_sum_till(x):
#     num = 3
#     primes = [2]
#     if x <= 2:
#         print(2)
#     else:
#         while num <= x:
#             for n in range(1, (2000000**.5)+1, 2):
#                 for m in range(3, n)
#                 if n%m == 0:
#                     num += 2
#                     break
#             else:
#                 primes.append(num)
#                 num += 2
#
#     print(len(primes))
#     print(sum(primes))
#
# prime_sum_till(2000000)
#################################################
# hi = 2000000
#
# # create a set excluding even numbers
# numbers = set(range(3, hi + 1, 2))
#
# for number in range(3, int(hi ** 0.5) + 1):
#     if number not in numbers:
#         #number must have been removed because it has a prime factor
#         continue
#
#     num = number
#     while num < hi:
#         num += number
#         if num in numbers:
#             # Remove multiples of prime found
#             numbers.remove(num)
#
# print (2 + sum(numbers))
#************************************************************
#             Sieve of Eratosthenes
#************************************************************
num = 2000000

prime_list = set(range(3, num+1, 2))

for i in range(3, int(num**.5)+1):

    j = i
    while j < num:
        j += i
        if j in prime_list:
            prime_list.remove(j)
print( 2 + sum(prime_list))