n = int(input())

for _ in range(n):
    string = list(input())
    check = 0
    flag = 1
    while len(string) > 0:
        if (string.pop(-1) == ')'):
            check = check+1
        else:
            check = check-1

        if (check < 0):
            flag = 0
            break
    if (flag == 0 or check != 0):
        print('NO')
    else:
        print('YES')
