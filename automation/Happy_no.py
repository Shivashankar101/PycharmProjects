def happy_no(num):
    while num != 1:

        happy_count = 0
        my_list = []
        trials = 1

        for digit in str(num):
            digit = int(digit)
            my_list.append(digit)

        for n in my_list:
            happy_count += n ** 2

        if happy_count == 1:
            print(f"{num} is a happy number...")
            print(happy_count)
            break

        else:
            trials += 1
            print(my_list)
            print(f'trial no:{trials}, current num value {num}')
            num = happy_count

        if trials > 10:
            print("more than 10 iterations ,, {num} seems to be not a happy no.!")
            break