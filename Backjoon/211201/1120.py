a, b = input().split()

answer = 0
for i in range(len(b)):
    cnt = 0
    if i + len(a) > len(b):
        break
    for j in range(len(a)):
        if b[i+j] == a[j]:
            cnt += 1
    if answer < cnt:
        answer = cnt

print(len(a)-answer)