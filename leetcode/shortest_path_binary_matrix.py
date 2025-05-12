from typing import List, Set, Tuple

test_cases = [
    ([[0, 1], [1, 0]], 2),
    ([[0, 0, 0], [1, 1, 0], [1, 1, 0]], 4),
    ([[1, 0, 0], [1, 1, 0], [1, 1, 0]], -1),
    ([[1, 0], [0, 0]], -1),
    ([[0, 0], [0, 1]], -1),
    ([[0, 0, 0], [0, 1, 1], [1, 1, 0]], -1),
    ([[0, 0, 0], [0, 1, 0], [0, 0, 0]], 4),
]


class Solution:

    def validAdjacentCells(
        self, grid: List[List[int]], row: int, col: int, n_rows: int, n_cols: int
    ) -> List[tuple[int, int]]:

        valid_adjacent_cells = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                # Skip current cell
                if i == 0 and j == 0:
                    continue

                new_row = row + i
                new_col = col + j

                # Check out of bounds
                if new_row < 0 or new_row >= n_rows or new_col < 0 or new_col >= n_cols:
                    continue

                # Check valid cell value
                if grid[new_row][new_col] == 1:
                    continue

                valid_adjacent_cells.append((new_row, new_col))
        return valid_adjacent_cells

    def dfs(
        self,
        grid: List[List[int]],
        curr_row: int,
        curr_col: int,
        end_row: int,
        end_col: int,
        n_rows: int,
        n_cols: int,
        visited: Set[Tuple[int, int]],
    ) -> int:

        # Reached our termination point successfully — we previously checked if termination point was reachable
        if curr_row == end_row and curr_col == end_col:
            return 1

        # Current cell is zero because we wouldn't have added it to cells to explore otherwise
        # We need to keep track of visited over full path

        # If there are no valid cells we will return -1
        unvisited_valid_neighbours = [
            cell
            for cell in self.validAdjacentCells(grid, curr_row, curr_col, n_rows, n_cols)
            if cell not in visited
        ]
        shortest_length = -1
        for next_row, next_col in unvisited_valid_neighbours:

            # Create new copy each iteration. Do we need to retain? Are we risking running into ourselves again
            # Not as we go deeper but as we surface and explore an adjacent cell, we are likely to walk down
            # the same path. Could optimise later.
            new_visited = set(visited)

            # This could be termination cell as a neighbour
            new_visited.add((next_row, next_col))
            path_length = self.dfs(
                grid, next_row, next_col, end_row, end_col, n_rows, n_cols, new_visited
            )
            if path_length != -1 and (shortest_length == -1 or path_length < shortest_length):
                shortest_length = path_length

        # We add 1 for the current cell unless we have not found a path
        return shortest_length + 1 if shortest_length != -1 else -1

    def bfs(self, grid: List[List[int]], n_rows: int, n_cols: int, end_row: int, end_col: int) -> int:
        visited = set()
        path_length = 1
        to_explore = set({(0, 0)})
        next_explore = set()
        while len(to_explore) > 0:
            for (r, c) in to_explore:
                if r == end_row and c == end_col:
                    # Add 1 because end cell is 0
                    return path_length

                visited.add((r, c))
                next_explore.update([
                    cell
                    for cell in self.validAdjacentCells(grid, r, c, n_rows, n_cols)
                    if cell not in visited and cell not in to_explore
                ])
            
            to_explore = next_explore
            next_explore = set()
            path_length += 1

        return -1

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n_rows = len(grid)
        n_cols = len(grid[0])

        # Edge Cases
        if grid[0][0] != 0:
            return -1

        if grid[n_rows - 1][n_cols - 1] != 0:
            return -1

        # DFS Algorithm
        # visited_cells = set({(0, 0)})
        # shortest_path = self.dfs(grid, 0, 0, n_rows - 1, n_cols - 1, n_rows, n_cols, visited_cells)
        shortest_path = self.bfs(grid, n_rows, n_cols, n_rows - 1, n_cols - 1)

        return shortest_path


if __name__ == "__main__":
    solver = Solution()
    for i, case in enumerate(test_cases):
        grid, n_expected = case
        n_counted = solver.shortestPathBinaryMatrix(grid)
        try:
            assert n_expected == n_counted
            print(f"Test Case [{i}]: PASSED")
        except AssertionError:
            print(f"Test Case [{i}]: FAILED. Expected {n_expected}. Returned {n_counted}")
