def solution(numbers, hand):
    answer = ''
    cur_left = [3,0]
    cur_right = [3,2]

    for number in numbers:
        if number in [1, 4, 7]:
            #left
            answer += 'L'
            a,b = divmod(number-1, 3)
            cur_left = [a, b]
        elif number in [3, 6, 9]:
            #right
            answer += 'R'
            a,b = divmod(number-1, 3)
            cur_right = [a, b]
        else:
            #hand
            if number == 0:
                a,b = divmod(10, 3)
            else:
                a,b = divmod(number-1, 3)
            left = abs(a-cur_left[0]) + abs(b-cur_left[1])
            right = abs(a-cur_right[0]) + abs(b-cur_right[1])
            print("number: ", number)
            print("num_loc: ", a, b)
            print("left: ", cur_left, left)
            print("right: ", cur_right, right)
            if left < right:
                answer += 'L'
                cur_left = [a, b]
            elif right < left:
                answer += 'R'
                cur_right = [a, b]
            else:
                if hand == "right":
                    answer += 'R'
                    cur_right = [a, b]
                else:
                    answer += 'L'
                    cur_left = [a, b]

    print(answer)

    return answer

solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")