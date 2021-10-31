def search_room(k_dict, room_num):

    if room_num not in k_dict:
        k_dict[room_num] = room_num + 1
        return room_num

    cur_room = search_room(k_dict, k_dict[room_num])
    k_dict[room_num] = cur_room + 1
    return cur_room


def solution(k, room_number):
    answer = []
    k_dict = {}
    for i in room_number:
        answer.append(search_room(k_dict, i))
    print(answer)
    return answer

solution(10, [1,3,4,1,3,1])