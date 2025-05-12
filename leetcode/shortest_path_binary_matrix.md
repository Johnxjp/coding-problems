# Leedtcode 1091: Shortest Path in Binary Matrix
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

    All the visited cells of the path are 0.
    All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).

The length of a clear path is the number of visited cells of this path.

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] is 0 or 1


## Understanding
Input: A grid of 0s and 1s
Objective: Return an integer that represents the shortest 'clear' path and -1 if there is no 'clear' path. The length of the path is the number of 0 cells.

1. We are working with a square matrix. 
2. It is a binary matrix with integer values
3. A path is valid if it connects 0,0 to n-1, n-1, with only 0s
4. A valid edge is 8-directional e.g. horizontal, vertical and diagonal
5. We should terminate a path when we have reached (n-1, n-1), or when we have no path forward
6. We do not need to return the path only the length of the shortest path
7. There may be many equivalent path so we just need to track the length of that path.


Clarification:
Can we visit a '1' cell? No. Consider this an obstacle.

Thoughts
Is that going to be particularly relevant to the solution?

## Plan

Problems that we need to solve:
1. Identifying valid cells to move to from the current location
2. Choosing the next cell to move to
3. Exploring multiple paths from a given cell
4. Determining when we have finished exploring a path
5. Doing this optimall.

Challenges:
1. The challenge that I see here is how do we track which cells we have already visited. We may want to use a cell as part of many paths e.g. 0,0 and n-1, n-1, is part of all paths. We cannot also assume the greedy path works best i.e. always moving down to the right as there could be dead ends.

2. We might explore the same path multiple times. Thankfully the grid is not that big but if it was a bigger grid, we would want to do some optimisation e.g. given a tile we have previously optimally explored, we check what the shortest path from that tile to the end is before proceeding. 

We can come back to this if it's an issue.

### Approach

1. We always start at the 0, 0 cell and try to get to n-1, n-1
2. We find all the adjacent cells which are valid. These are cells in bound. Cells that are marked by 0
3. We select one cell and keep the rest in reserve.
4. We explore that cell until we reach a termination point.
5. We terminate when we do not have a choice of adjacent valid cells and have not reached the end returning -1. Or we reach end and return length.
6. We keep track of cells we have visited so we don't double back on ourselves. We must take care that the visited cells are unique to a path we are exploring and not global to all paths. 

### Data Structure
This makes sense to me to be a DFS recursive approach. We want to always fully explore a path from a given cell. Once we have explored all adjacent paths
we select the smallest and return smallest + 1 or -1 if we couldn't reach the end. 

From the end cell we will always return 1 assuming it is zero or -1 otherwise.

1. We should not visit a cell more than once. It does not make sense to do this when searching for the shortest path.


Edge cases

1. If (0,0) = 1 return -1
2. If (n-1, n-1) = 1, return -1


