import heapq
from typing import List
from collections import Counter


def leastInterval(tasks: List[str], n: int) -> int:

    counter = Counter(tasks)
    result = 0

    while True:
        sub_count = 0

        print(counter.most_common(n + 1))
        for task, _ in counter.most_common(n + 1):
            sub_count += 1
            result += 1

            counter.subtract(task)

            # 0 이하인 아이템을 목록에서 완전히 제거
            counter += Counter()

        if not counter:
            break

        result += n - sub_count + 1
    return result


if __name__ == "__main__":
    leastInterval(["A", "A", "A", "B", "C", "D"], 2)
