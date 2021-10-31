
k, m = map(int, input().split())
candi = []
for _ in range(k):
    candi.append(list(map(int, input().split())))

max_ans = 0
def backtracking(turn, ans):
    global max_ans

    if turn == k:
        max_ans = max(ans % m, max_ans)
        print("max_ans: ")
        print(max_ans)
        return

    for i in candi[turn]:
        print(i, turn, ans)
        backtracking(turn+1, ans + i**2)

backtracking(0, 0)
print(max_ans)




# 3 1000
# 2 5 4
# 3 7 8 9
# 5 5 7 8 9 10
