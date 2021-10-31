N = int(input())
nums = list(map(int, input().split()))
X = int(input())
nums.sort()
p1 = 0
p2 = N-1
ans = 0

while p1 < p2:
    cur_sum = nums[p1] + nums[p2]
    if cur_sum == X:
        print(p1, p2)
        ans += 1
        p1 += 1
        continue
    elif cur_sum > X:
        p2 -= 1
        continue
    else:
        p1 += 1
        continue
print(ans)






# 9
# 5 12 7 10 9 1 2 3 11
# 13