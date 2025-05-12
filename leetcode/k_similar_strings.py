from typing import Dict, List
from collections import defaultdict

test_cases = [
    (["ba", "ab"], 1),
    (["abc", "bca"], 2),
    (["aabca", "abaac"], 2),
    (["afafa", "aaffa"], 1),
    (["abccaacceecdeea", "bcaacceeccdeaae"], 9),
]


class Solution:

    def __init__(self):
        self.memo = {}

    def swapChars(self, string: str, index_1: int, index_2: int) -> str:
        """Returns a new string with the characters swapped"""

        if index_1 > index_2:
            index_1, index_2 = index_2, index_1

        a = string[index_1]
        b = string[index_2]
        new_string = string[:index_1] + b + string[index_1 + 1 : index_2] + a
        if index_2 == len(string) - 1:
            return new_string

        return new_string + string[index_2 + 1 :]

    def findShortestPath(
        self, current: str, target: str, swaps: int, mapping: Dict[str, List[int]]
    ) -> int:

        mismatches = [i for i in range(len(current)) if current[i] != target[i]]
        if len(mismatches) == 0:
            return swaps
        
        if current in self.memo:
            return self.memo[current]


        new_swaps = float("inf")
        # Take only first mismatch
        i = mismatches[0]
        char = current[i]
        correct_indexes = mapping[char]
        for j in correct_indexes:
            if current[j] != target[j]:
                new_current = self.swapChars(current, i, j)
                # print("Input", current, "| Swapped", new_current)
                new_swaps = min(
                    new_swaps, self.findShortestPath(new_current, target, swaps + 1, mapping)
                )
        
        self.memo[current] = new_swaps
        return new_swaps

    def kSimilarity(self, s1: str, s2: str) -> int:
        if s1 == s2:
            return 0

        map_s2 = defaultdict(list)
        for index, c in enumerate(s2):
            map_s2[c].append(index)

        print(map_s2)

        return self.findShortestPath(s1, s2, 0, map_s2)


if __name__ == "__main__":
    solver = Solution()
    for i, case in enumerate(test_cases):
        [s1, s2], n_expected = case
        n_counted = solver.kSimilarity(s1, s2)
        try:
            assert n_expected == n_counted
            print(f"Test Case [{i}]: PASSED")
        except AssertionError:
            print(f"Test Case [{i}]: FAILED. Expected {n_expected}. Returned {n_counted}")
