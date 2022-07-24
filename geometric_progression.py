def geometric_progression(start: int, q: int, length: int):
    count = 0

    while count < length:
        tmp = yield start
        if tmp == 'stop':
            print('stopped')
            break
        start *= q
        count += 1
    return

x = geometric_progression(3, 5, 6)

for item in x:
    print(item)
    if item > 20:
        x.send('stop')
