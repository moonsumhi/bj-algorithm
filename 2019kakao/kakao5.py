class Node(object):
    def __init__(self, loc, key, left=None, right=None, parent=None):
        self.x = loc[0]
        self.y = loc[1]
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right

class Tree(object):
    def __init__(self, s_loc, s_key):
        self.head = Node(s_loc, s_key)


    def insert(self, loc, node_num):
        cur_node = self.head
        new_x, new_y = loc
        while True:
            if cur_node.x <= new_x:
                if not cur_node.right:
                    cur_node.right = Node(loc, node_num, parent=cur_node)
                    return
                cur_node = cur_node.right
            else:
                if not cur_node.left:
                    cur_node.left = Node(loc, node_num, parent=cur_node)
                    return
                cur_node = cur_node.left


    def preorder(self, t_len):
        cur_node = self.head
        visited = [False]*(t_len+1)
        visited[0] = True
        answer = [cur_node.key]

        while not all(visited):
            visited[cur_node.key] = True
            if cur_node.left and not visited[cur_node.left.key]:
                cur_node = cur_node.left
                answer.append(cur_node.key)
                continue
            if cur_node.right and not visited[cur_node.right.key]:
                cur_node = cur_node.right
                answer.append(cur_node.key)
                continue
            cur_node = cur_node.parent

        return answer


    def postorder(self, t_len):
        cur_node = self.head
        visited = [False]*(t_len+1)
        visited[0] = True
        answer = []

        while not all(visited):
            if cur_node.left and not visited[cur_node.left.key]:
                cur_node = cur_node.left
                continue
            if cur_node.right and not visited[cur_node.right.key]:
                cur_node = cur_node.right
                continue
            visited[cur_node.key] = True
            answer.append(cur_node.key)
            cur_node = cur_node.parent

        return answer


def solution(nodeinfo):
    answer = [[]]
    nodes = [(v, idx+1) for idx, v in enumerate(nodeinfo)]
    nodes.sort(key=lambda x: x[0][1], reverse=True)

    t = Tree(*nodes[0])
    for i in nodes[1:]:
        t.insert(i[0], i[1])
    answer.append(t.preorder(len(nodeinfo)))
    answer.append(t.postorder(len(nodeinfo)))


    return answer

solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]])