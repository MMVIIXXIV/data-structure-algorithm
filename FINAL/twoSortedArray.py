def merge(x, y):
    m = len(x)
    n = len(y)
    
    for i in range(m):
        if x[i] > y[0]:
            temp = x[i]
            x[i] = y[0]
            y[0] = temp

            y.sort()

    print(x, y)

if __name__ == '__main__':
    x = [5,6,7,8,9]
    y = [1,2,3,4]
    merge(x,y)
