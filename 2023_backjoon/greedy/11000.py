import heapq

def main():
    N = int(input())
    cls_list = []
    for _ in range(N):
        cls_list.append(tuple(map(int, input().split(" "))))
    cls_list.sort(key=lambda x: (x[0], x[1]))

    cur_end_tm = []
    answer = 0
    for start_tm, end_tm in cls_list:
        if len(cur_end_tm) > 0:
            smallest_end_tm = heapq.heappop(cur_end_tm)
            if start_tm < smallest_end_tm:
                heapq.heappush(cur_end_tm, smallest_end_tm)
                answer += 1
        else:
            answer += 1
        heapq.heappush(cur_end_tm, end_tm)

    return answer     


if __name__ == "__main__":
    answer = main()
    print(answer)