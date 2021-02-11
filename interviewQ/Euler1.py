

# If we list all the natural numbers below 10 that are
# multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these
# multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.

# sum_total = 0
# for n in range (1, 1001):
#     if n%3 == 0 or n%5 == 0:
#         sum_total += n

# print(sum_total)


all_num = [n for n in range(1001) if n % 3 == 0 or n % 5 == 0 ]
print(sum(all_num))
