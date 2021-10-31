def solution(food_times, k):
    foods = []
    N = len(food_times)
    for i in range(N):
        foods.append((food_times[i], i+1))
    foods.sort()
    print(foods)

    pretime = 0
    RN = len(food_times)
    for i in range(N):
        food_time, food_num = foods[i]
        diff = food_time - pretime
        if diff != 0:
            spend = diff * RN
            if k-spend >= 0:
                k -= spend
                pretime = food_time
            else:
                sublist = sorted(foods[i:], key=lambda x: x[1])
                k = k % RN
                print(sublist)
                return sublist[k][1]
        RN -= 1

    return -1

solution([3,1,2], 5)