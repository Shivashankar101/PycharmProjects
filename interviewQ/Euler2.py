# even fibonacci:
a = 0
b = 1


# for n in range(0, 30):
#     a, b = b, a+b
#     if b%2 == 0 and b < 999999:
#         print(b, end=" ")
#     elif b>=1000000:
#         break

while b< 1000000:
    a, b = b, a+b
    if b % 2 == 0:
        print(b)



