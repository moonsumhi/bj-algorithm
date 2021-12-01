import bisect

def solution(people, limit):
    answer = 0
    people.sort()

    a_idx = bisect.bisect(people, limit-people[0])
    answer = a_idx // 2
    







    return answer

solution([70, 50, 80, 50], 100)