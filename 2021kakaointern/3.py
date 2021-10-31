class Node:
    def __init__(self):
        self.removed = False
        self.next = None
        self.prev = None


def solution(n, k, cmd):
    answer = ''
    node_arr = [Node() for _ in range(n)]
    for i in range(1, n):
        node_arr[i-1].next = node_arr[i]
        node_arr[i].prev = node_arr[i-1]
    mystack = []
    curr = node_arr[k]
    for i in cmd:
        if i[0] == 'D':
            for _ in range(int(i[2:])):
                curr = curr.next
            continue
        if i[0] == 'U':
            for _ in range(int(i[2:])):
                curr = curr.prev
            continue
        if i[0] == 'C':
            curr.removed = True
            mystack.append(curr)
            up = curr.prev
            down = curr.next
            if up:
                up.next = down
            if down:
                down.prev = up
                curr = down
            else:
                curr = up
        if i[0] == 'Z':
            new = mystack.pop()
            new.removed = False
            up = new.prev
            down = new.next
            if up:
                up.next = new
            if down:
                down.prev = new

    for i in range(n):
        if node_arr[i].removed:
            answer += 'X'
        else:
            answer += 'O'
    print(answer)
    return answer

solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"])