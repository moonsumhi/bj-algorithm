def solution(param):
    answer = 0
    claps = 0
    for i in range(param):
        num = str(i)
        claps += num.count("3")
        claps += num.count("6")
        claps += num.count("9")
    print(claps)
    return answer

solution(0)