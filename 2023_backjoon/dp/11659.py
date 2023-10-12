def main():
    N, M = map(int, input().split(" "))
    nums = list(map(int, input().split(" ")))
    _range = []
    for _ in range(M):
        _range.append(tuple(map(int, input().split(" "))))
    dp = [nums[0]]
    for i in range(1, len(nums)):
        dp.append(dp[i-1] + nums[i])
    for start, end in _range:
        first = dp[end-1]
        second = 0 if start-2 < 0 else dp[start-2]
        print(first-second)


if __name__ == "__main__":
    main()
