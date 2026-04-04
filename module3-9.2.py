def get_odds():
    for number in range(10):
        if number % 2 == 1:
            yield number

count = 0

for odd in get_odds():
    count += 1
    if count == 3:
        print(odd)
        break
