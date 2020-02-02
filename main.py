from math import pow, sqrt, log, floor

def evaluate_function(val):
    x = val
    return eval(func)


def frange(start, stop, step):
    i = start
    while i < stop:
        yield i
        i += step


func = input('enter a function: ')

start = float(input('select starting x-value: '))
stop = float(input('select ending x-value: '))
w = float(input('select rectangle width: '))

amt = floor((stop - start) / w)

area = 0.0

for i in frange(start, stop, w):
    y = evaluate_function(i)
    # print('i: ' + str(i) + ' ' + 'y: ' + str(y))
    area += w * y

print("function f(x) = {0} \ngoing from {1} to {2}\ncreating {3} rectangles\ngives area: {4}".format(func, start, stop, amt, round(area, 3)))
