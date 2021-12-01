a, b = input().split()
a = list(map(int, a))
n = len(a)
b = int(b)
check = [False]*n


def go(index, num):
    if index == n:
        return num
    ans = -1
    for i in range(n):
        if check[i]:
            continue
        if index == 0 and a[i] == 0:
            continue
        check[i] = True
        temp = go(index+1, num*10+a[i])
        if temp < b:
            if ans == -1 or ans < temp:
                ans = max(ans, temp)
        check[i] = False
    return ans

print(go(0,0))