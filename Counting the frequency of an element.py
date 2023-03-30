b = [0] * (10)

for x in range(0, 9 + 1, 1):
    print("Enter value in array" + str(x))
    b[x] = int(input())
for y in range(0, 9 + 1, 1):
    t = 0
    for a in range(0, 9 + 1, 1):
        if b[y] == b[a]:
            t = t + 1
    print("The Frequency of element of array" + str(y) + "=" + str(t))
