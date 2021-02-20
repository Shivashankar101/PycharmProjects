my_list = list(range(2, 21))
print (my_list)
new_list = []

while set(my_list) == {1}:
    for n in my_list:
        for m in range(n, 21):
            if n*m in my_list:
                new_list.append(m)
                my_list[my_list.index(n*m)] = m


print(new_list)
sum_total = 1
for x in new_list:
    sum_total*=x

print(sum_total)



