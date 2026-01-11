def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

gen = infinite_sequence()

while True:
    print(next(gen))