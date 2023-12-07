from re import L


def sortBinary(lt):
    zeroLt = []
    oneLt = []
    for i in lt:
        if i == 0:
            zeroLt.append(i)
        else:
            oneLt.append(i)

    return zeroLt + oneLt

input = [1,1,0,1,0,0,0,1,0,1,1,0,1,0]
print(f"output: {sortBinary(input)}")

