def merge(x, y):

    m = len(x)
    n = len(y)

    for i in range(m):
        if x[i] == 0:
            x[i] = y[0]
            y.remove(y[0])

    x.sort()

x = [0,2,0,3,0,5,6,0,0]
y = [1,8,9,10,15]
merge(x, y)
print(x,y)