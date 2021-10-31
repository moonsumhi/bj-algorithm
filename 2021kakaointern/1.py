def solution(s):
    num_dict = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven':'7', 'eight':'8', 'nine':'9'}
    dict_keys = list(num_dict.keys())
    answer = ""
    tmp = ""
    for c in s:
        if c.isnumeric():
            answer += c
        else:
            tmp += c

        if tmp in dict_keys:
            answer += num_dict[tmp]
            tmp = ""
    return answer

solution("2three45sixseven")