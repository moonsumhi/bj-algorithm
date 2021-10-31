def solution(stones, k):
    left, right = min(stones), max(stones)
    while left < right:
        mid = (right + left + 1) // 2
        cnt = 0
        for stone in stones:
            if stone < mid:
                cnt += 1
            if stone >= mid:
                cnt = 0
            if cnt >= k:
                right = mid
                break
        else:
            left = mid
    return left