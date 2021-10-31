

class Node(object):
    def __init__(self, key):
        self.key = key
        self.wlen = {}
        self.children = {}


class Trie(object):
    def __init__(self):
        self.head = Node(None)


    def insert(self, string):
        curr_node = self.head
        if len(string) not in curr_node.wlen:
            curr_node.wlen[len(string)] = 1
        else:
            curr_node.wlen[len(string)] += 1

        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            curr_node = curr_node.children[char]
            if len(string) not in curr_node.wlen:
                curr_node.wlen[len(string)] = 1
            else:
                curr_node.wlen[len(string)] += 1


    def search(self, string):
        curr_node = self.head
        for char in string:
            if char == '?':
                try:
                    return curr_node.wlen[len(string)]
                except KeyError:
                    return 0

            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return 0


def solution(words, queries):
    answer = []
    t = Trie()
    r_t = Trie()

    for word in words:
        t.insert(word)
        r_t.insert(word[::-1])

    for query in queries:
        if query.startswith("?"):
            answer.append(r_t.search(query[::-1]))
        else:
            answer.append(t.search(query))

    print(answer)
    return answer

solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["?????"])