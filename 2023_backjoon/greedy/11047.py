def main():
    N, K = map(int, input().split(" "))
    coins = []
    for _ in range(int(N)):
        coins.append(int(input()))
    answer = 0 
    while (K > 0):
        coin = coins.pop()
        cnt, K = divmod(K, coin)
        answer += cnt

    return answer

if __name__ == "__main__":
    answer = main()
    print(answer)