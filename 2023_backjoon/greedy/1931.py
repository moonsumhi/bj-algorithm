def main():
    meeting_cnt = int(input())
    meetings = []
    for _ in range(meeting_cnt):
        meetings.append(tuple(map(int, input().split(" "))))

    end_tm_order = sorted(meetings, key=lambda x: (x[1], x[0]))
    cur_meeting_end_tm = end_tm_order[0][1]

    answer = 1

    for start_tm, end_tm in end_tm_order[1:]:
        if cur_meeting_end_tm > start_tm:
            continue
        cur_meeting_end_tm = end_tm
        answer += 1

    return answer 


if __name__ == "__main__":
    answer = main()
    print(answer)