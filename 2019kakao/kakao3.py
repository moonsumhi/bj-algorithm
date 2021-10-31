from itertools import combinations

def solution(relation):
    answer = []
    result = 0
    N = len(relation)
    attributes = list(zip(*relation))
    complex_key = []
    for a in attributes:
        if len(set(a)) == N:
            result += 1
        else:
            complex_key.append(a)
    print("answer: ", answer)
    print("complex_key: ", complex_key)
    print(list(zip(*complex_key)))
    cnt = 2
    while cnt <= N:
        tmp = [i for i in range(len(complex_key))]
        for i in combinations(tmp, cnt):
            print("i : ", i)
            key_combi = []
            for j in i:
                key_combi.append(complex_key[j])
            print("key_combi: ", key_combi)
            print("key_combi_list : ", set(zip(*key_combi)))
            if len(set(zip(*key_combi))) == N:
                answer.append(set(i))
        cnt += 1

    print("answer: ", answer)

    A = len(answer)
    check = [True]*A
    for i in range(A):
        for j in range(i+1, A):
            if answer[i].intersection(answer[j]) == answer[i]:
                check[j] = False

    print(check)
    result += sum(check)


    return result

solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]])