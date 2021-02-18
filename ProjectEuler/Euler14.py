#
# def collatz_len_gen(num):
#     series = [num]
#     while num != 1:
#         if num % 2 == 0:
#             num = num/2
#             series.append(num)
#
#         else:
#             num = 3*num + 1
#             series.append(num)
#
#     return len(series)
#
# def longest_collatz_below(num):
#     longest = 0
#     number = [1]
#     i = 1
#     while i < num:
#         i += 1
#         collatz_len_gen(i)
#
#         if collatz_len_gen(i) > longest:
#             number.insert(0, i)
#             longest = collatz_len_gen(i)
#
#     print('length is :', longest, 'number is :', number[0])
#
#
# longest_collatz_below(1000000)

# import time
# start = time.time()
#
# def collatz_len(num):
#     series = [num]
#     count = 1
#     while num != 1:
#         if num % 2 == 0:
#             num = num / 2
#             if num in series:
#                 count += series.index(num)
#                 break
#             else:
#                 series.append(num)
#                 count += 1
#
#         else:
#             num = 3 * num + 1
#             if num in series:
#                 count += series[num].index()
#                 break
#             else:
#                 series.append(num)
#                 count += 1
#
#     return count
#
#
# end = time.time()
#
# print(end - start)


#  88888888888888888888888888888888888888888888888888
#problem 14 project euler
# import time
# start=time.time()
# has2={}
# def collatz(x):
#     seq=[]
#     seq.append(x)
#     temp=x
#     while(temp>1):
#         if temp%2==0:
#             temp=int(temp/2)
#             if temp in has2:
#                 seq+=has2[temp]
#                 break
#             else:
#                 seq.append(temp)
#         else:
#             temp=3*temp+1
#             if temp in has2:
#                 seq+=has2[temp]
#                 break
#             else:
#                 seq.append(temp)
#
#
#     has2[x]=seq
#     return len(seq)
#
# num=0
# greatest=0
# for i in range(1000000):
#     c=collatz(i)
#     if num<c:
#         num=c
#         greatest=i
# print('{0} has {1} elements. calculation time ={2} seconds.'.format(greatest,num,time.time()-start))
import time
start = time.time()
def collatz(y):
    num = y
    seq = [num]
    dic = {}

    while num > 1:
        if num % 2 == 0:
            num = int(num/2)
            if num in dic:
                seq += dic[num]
                break
            else:
                seq.append(num)
        else:
            num = int(3*num+1)
            if num in dic:
                seq += dic[num]
                break
            else:
                seq.append(num)

    dic[num] = seq
    return len(seq)

number = 0
length = 0
for i in range(1, 1000000):
    c = collatz(i)
    if length < c:
        length = c
        number = i
end = time.time()
print("\nthe number is :", number , "\nthe length of seq is :", length, "\nexecute time is:", (end - start))




