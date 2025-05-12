from typing import List, Set, Tuple

test_cases = [
    (
        [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ],
        1,
    ),
    (
        [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ],
        3,
    ),
    ([["1", "1"], ["1", "1"]], 1),
    ([["1", "0"], ["0", "1"]], 2),
]


class Solution:

    def getPotentialNeighbours(self, row: int, col: int) -> List[Tuple[int, int]]:
        return [
            (row - 1, col),  # above
            (row + 1, col),  # below
            (row, col - 1),  # left
            (row, col + 1),  # right
        ]

    def mapIsland(
        self,
        grid: List[List[str]],
        start_row: int,
        start_col: int,
        n_rows: int,
        n_cols: int,
        visited_land: Set[Tuple[int, int]],
    ) -> Set[Tuple[int, int]]:
        """BFS over the grid from the starting point"""
        visited_land.add((start_row, start_col))
        unvisited_neighbours = set()

        # Populate initial neighbours - check above, left, right and bottom.
        potential_neighbours = self.getPotentialNeighbours(start_row, start_col)
        for r, c in potential_neighbours:
            # out of bound
            if r < 0 or r >= n_rows or c < 0 or c >= n_cols:
                continue

            # water tile
            if grid[r][c] == "0":
                continue

            # visited land
            if (r, c) in visited_land:
                continue

            unvisited_neighbours.add((r, c))

        while len(unvisited_neighbours) > 0:
            # Pop a random location
            # Visit it
            # Find new valid neighbours
            # Add to set (because set only new ones added)

            # Bit jumpy and not an order but anyway.
            loc = unvisited_neighbours.pop()

            # Is there a chance we visited? We can check anyway?
            visited_land.add(loc)
            potential_neighbours = self.getPotentialNeighbours(loc[0], loc[1])
            for r, c in potential_neighbours:
                # out of bound
                if r < 0 or r >= n_rows or c < 0 or c >= n_cols:
                    continue

                # water tile
                if grid[r][c] == "0":
                    continue

                # visited land
                if (r, c) in visited_land:
                    continue

                unvisited_neighbours.add((r, c))

        return visited_land

    def numIslands(self, grid: List[List[str]]) -> int:
        n_islands = 0
        n_rows = len(grid)
        n_cols = len(grid[0])

        visited_land = set()
        for row in range(n_rows):
            for col in range(n_cols):
                if grid[row][col] == "1" and (row, col) not in visited_land:
                    n_islands += 1
                    visited_land = self.mapIsland(grid, row, col, n_rows, n_cols, visited_land)

        return n_islands


if __name__ == "__main__":
    solver = Solution()
    for i, case in enumerate(test_cases):
        grid, n_expected = case
        n_counted = solver.numIslands(grid)
        try:
            assert n_expected == n_counted
            print(f"Test Case [{i}]: PASSED")
        except AssertionError:
            print(f"Test Case [{i}]: FAILED. Expected {n_expected}. Returned {n_counted}")
