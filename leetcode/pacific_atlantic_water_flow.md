# Leetcode 417: Pacific Atlantic Water Flow
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

## Understand

input: 
1. heights: integer m x n grid representing an entire island. 
- each integer at a (row, column) represents heigh above sea level for that cell
output: 2d list of coordinates where rain can flow into both pacific and atlantic.  
constraints:

m == heights.length
n == heights[r].length
1 <= m, n <= 200
0 <= heights[r][c] <= 105


clarifications:
1. m not necessarily equal to n
2. left and top edge of grid represent pacific ocean. Top-right = pacific
3. right and bottom edge of grid represent atlantic ocean. bottom-left = atlantic
4. 'rain' water can flow to neighbour cell's above, left, right and bottom.
5. 'rain' cannot flow diagonally to neighbours
6. 'rain' only flows if neighbour's cell height is less than or equal to current cell height
7. 'rain' can flow into the ocean as well [off-grid]

## Plan
### Approach
What this problem is asking me is to compare cell values and check if there is a route from a given cell to the edges of the board. The condition though is that the water
must reach both the atlantic and pacific which is a combination of at least (left, bottom), (top, bottom), (left, right), (top, right). We only need to check that it gets
to an edge or one of the diagonals. If touching edge, we are at a termination point.

What algorithm / data structure best fits this problem?
1. I think BFS would work well here. Because we just need to find any path to the edges or stop when there is no path and BFS will likely find this first.
2. Not sure if we'd benefit from a queue here to manage order we visit neighbours. That I think is an optimisation. I don't think we can kill a path early unless we have already visited


### Execution
What subproblems do I need to solve?
1. Iterating through every cell
2. Determining from a given source cell what oceans we can reach?
    a. Choosing neighbours we can visit from a given cell
    b. have we reached the ocean?
    b. have we reached a local minima so we no longer have any neighbours to visit?
3. Storing the results for each cell to identify which meet our criteria

Algorithm
1. Iterate through every single cell [we may be able to rule some cells out immediately but can figure that out later]
2. Run a BFS with every cell. From this function, return the oceans it has reached as a boolean value
    a. Choose neighbours
    b. keep track of those we have visited
    c. determine when we are at an edge and which ocean it belongs to
    d. track which oceans reached in a set. 
    e. Early stopping once reached both oceans. Otherwise keep going to no more neighbours
3. Store coordinates to return at the end


## Review
What esdge cases might break my solution?