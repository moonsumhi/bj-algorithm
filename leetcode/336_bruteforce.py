# bruteforce

from typing import List
from itertools import permutations


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        str_len = len(words)
        results = []
        for a, b in permutations(range(str_len), 2):
            st = words[a] + words[b]
            if st == st[::-1]:
                results.append([a, b])
        print(results)
        return results


sol = Solution()
sol.palindromePairs(["abcd", "dcba", "lls", "s", "sssll"])
