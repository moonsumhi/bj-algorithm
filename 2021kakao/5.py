

def str2sec(string):

    """ 시간 문자열을 초로 바꿔서 int로 반환 """

    hour, min, sec = map(int, string.split(':'))
    return hour * 3600 + min * 60 + sec

def sec2str(seconds):

    """ 초(int)를 시간 문자열로 바꿔서 반환 """

    string = ''
    hour = seconds // 3600
    seconds -= hour * 3600
    min = seconds // 60
    seconds -= min * 60

    return f"{str(hour).zfill(2)}:{str(min).zfill(2)}:{str(seconds).zfill(2)}"

def solution(play_time, adv_time, logs):

    #  전체 재생시간과 광고 재생 시간을 초 단위로 바꿔 준다.
    play_time = str2sec(play_time)
    adv_time = str2sec(adv_time)

    # timeline[i]는 i초에서 몇명의 사람들이 보고 있는지
    timeline = [0] *(play_time+1)

    #logs를 돌면서 timeline의 시작시간에 +1 종료 시간에 -1을 해준다.
    #시작 시간에는 시청자 1, 종료 시간에 시청자 -1
    for log in logs:
        start, end= map(str2sec, log.split('-'))
        timeline[start] += 1
        timeline[end] -= 1

    #for문을 한번 돌면 비어있는 구간에 시청자 수를 알 수 있음
    for i in range(1, play_time+1):
        timeline[i] = timeline[i] + timeline[i-1]

    #for문을 한번 "더" 돌면 timeline[0] ~ timeline[i] 까지의 누적합이 된다.
    #누적합은 0 ~ i 초까지 누적 시청 시간이 된다.
    #이런식으로 하는 이유는 광고 시작 시간 A와 종료시간 B가 주어졌을 때
    #timeline[B] - timeline[A]로 더 빠르게 구할 수 있음
    for i in range(1, play_time+1):
        timeline[i] = timeline[i] + timeline[i-1]

    answer =0
    #0초에 광고를 시작했을때 누적 시간
    max_cnt = timeline[adv_time]


    for start in range(1, play_time):
        #광고 종료 시간이 영상 재생시간을 넘어가면 광고 재생 종료 시간을 영상 종료 시간(play_time)으로 둔다.
        end = play_time if start + adv_time >= play_time else start + adv_time

        #시청자 수가 이전 답보다 많을 때를 찾으면서 값을 업데이트
        if max_cnt < timeline[end] - timeline[start]:
            max_cnt = timeline[end] - timeline[start]
            answer = start + 1
            #여기서 1초를 더해준 이유는 timeline[end] - timeline[start]가
            #start+1초 부터 end초사이의 누적 시간이기 때문에

    return sec2str(answer)
