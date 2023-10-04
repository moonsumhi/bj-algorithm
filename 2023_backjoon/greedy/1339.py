from collections import defaultdict

def main():
    N = int(input())
    words = []
    for _ in range(N):
        word = input()
        words.append(word)
    
    score = defaultdict(int)
    for word in words:
        word_length = len(word)
        for idx, alphabet in enumerate(word):
            score[alphabet] += 10**(word_length-idx)

    alphabet_tuples = score.items()
    sorted_alphabet_tuples = sorted(alphabet_tuples, key=lambda x: x[1])
    alphabet_map = {}

    for i in range(9, -1, -1):
        if not sorted_alphabet_tuples:
            break
        alphabet = sorted_alphabet_tuples.pop()
        alphabet_map[alphabet[0]] = i
    
    total = 0
    for word in words:
        changed_word = ""
        for alphabet in word:
            changed_word += str(alphabet_map[alphabet])
        total += int(changed_word)

    return total

if __name__ == "__main__":
    answer = main()
    print(answer)