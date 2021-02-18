mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15]

for i, num in enumerate(mylist):
    if num % 3 == 0 and num % 5 == 0:
        mylist[i] = 'fizzbuzz'

# for i in range(len(mylist)):
#     if mylist[i] % 3 == 0 and mylist[i] % 5 == 0:
#         mylist[i] = 'fizzbuzz'


print(mylist)