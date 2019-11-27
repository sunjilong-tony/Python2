# coding= utf-8
def func(n):
    arr = [1]
    index = 0
    while index < n:
        yield arr
        arr = [arr[x] +arr[x+1] for x in range(len(arr) - 1)]
        arr.insert(0, 1)
        arr.append(1)
        index += 1


g = func(5)
for i in g:
    print(i)
