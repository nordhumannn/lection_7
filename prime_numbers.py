def prime_nums(n):
    x = 1

    while x <= n:
        flag = True
        for i in range(2, x):
            if not x % i:
                flag = False
                break
        if flag:
            yield x
        x += 1

prime_nums = list(item for item in prime_nums(100))

print(prime_nums)
