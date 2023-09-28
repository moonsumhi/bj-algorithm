from collections import Counter

def main():
    seat_cnt = int(input())
    seat_info = input()
    seat_counter = Counter(seat_info)
    s_cnt = seat_counter["S"]
    ll_cnt = (seat_cnt - s_cnt)//2

    return (s_cnt + ll_cnt) + 1 if ll_cnt > 0 else s_cnt


if __name__ == "__main__":
    answer = main()
    print(answer)