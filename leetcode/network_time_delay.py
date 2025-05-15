from collections import defaultdict
from typing import List

test_cases = [
    (([[2, 1, 5], [1, 2, 3], [2, 3, 1], [3, 4, 1]], 4, 2), 5),
    (([[1, 2, 1]], 2, 1), 1),
    (([[1, 2, 1], [2, 3, 2], [1, 3, 2]], 3, 1), 2),
]


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        node_map = defaultdict(list)
        for source, target, time in times:
            node_map[source].append((target, time))

        # Memoisation — shortest time to get to a node
        shortest_times = {i: float('inf') for i in range(1, n+1)}
        shortest_times[k] = 0  # Start node

        def dfs(node, current_time):
            # Check all neighbors
            for neighbor, time in node_map[node]:
                # Calculate new time to reach this neighbor
                new_time = current_time + time
                
                # If we found a shorter path to the neighbor
                if new_time < shortest_times[neighbor]:
                    shortest_times[neighbor] = new_time
                    dfs(neighbor, new_time)
        
        # Start DFS from node k
        dfs(k, 0)
        
        # Check if all nodes are reachable
        max_time = max(shortest_times.values())
        return max_time if max_time < float('inf') else -1


if __name__ == "__main__":
    solver = Solution()
    for i, case in enumerate(test_cases):
        inputs, n_expected = case
        times, n, k = inputs
        n_counted = solver.networkDelayTime(times, n, k)
        try:
            assert n_expected == n_counted
            print(f"Test Case [{i}]: PASSED")
        except AssertionError:
            print(f"Test Case [{i}]: FAILED. Expected {n_expected}. Returned {n_counted}")
