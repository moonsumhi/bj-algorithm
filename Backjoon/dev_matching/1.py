# S는 알파벳 소문자(a ~ z)로 구성된 문자열로 길이는 3 이상 6 이하입니다.
# N는 숫자(0~9)로 구성된 문자열로 길이는 0 이상 6 이하입니다.
# N의 길이가 0이 될 수도 있다는 것은, N이 비어있는 널(null) 문자열이 될 수도 있다는 의미입니다.
# N의 길이가 1 이상이면, N의 첫자리는 "0"이 될 수 없습니다.
# 즉, "034" , "06", "0", "09040", "000"과 같은 문자열은 N이 될 수 없습니다.


# new_id가 registered_list에 포함되어 있지 않다면, new_id를 추천하고 종료합니다.
# new_id가 registered_list에 포함되어 있다면,
#
# 2-1. new_id를 두 개의 문자열 S와 N으로 분리합니다.
# 2-2. 문자열 N을 10진수 숫자로 변환한 값을 n이라고 합니다.(단, N이 비어있는 null 문자열이라면, n은 0이 됩니다.)
# 2-3. n에 1을 더한 값(n+1)을 문자열로 변환한 값을 N1라고 합니다.
# 2-4. new_id를 S+N1로 변경하고 1.로 돌아갑니다.

def solution(registered_list, new_id):
    s = ""
    n = ""
    for i in new_id:
        if i.isalpha():
            s += i
        else:
            n += i

    if n != "":
        n = int(n)
    else:
        n = 0

    registered_dict = {i:1 for i in registered_list}

    while True:
        try:
            answer = registered_dict[new_id]
            n1 = str(int(n) + 1)
            new_id = s + n1
            n = n1
        except KeyError:
            return new_id



print(solution(["card", "ace13", "ace16", "banker", "ace17", "ace14"], "ace15"))
print(solution(["cow", "cow1", "cow2", "cow3", "cow4", "cow9", "cow8", "cow7", "cow6", "cow5"], "cow"))