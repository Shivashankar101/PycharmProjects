# Find the largest palindrome made from the product of two 3-digit numbers.
palindrome_list = []
for i in range(100, 1000):
    for j in range(i+1, 1000):
        k = i*j
        if str(k) == str(k)[::-1]:
            palindrome_list.append((i, j, i*j))


print(max(palindrome_list))
print(len(palindrome_list))
#
# for x in range(924, 1000):
#     for y in range(962, 1000):
#         z = x * y
#         if str(z) == str(z)[::-1]:
#             print(z)
# else:
#     print('no pal')