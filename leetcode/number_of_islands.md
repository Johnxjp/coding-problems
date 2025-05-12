# Leetcode 200: Number of Islands
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Constraints are given as follows:
m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.


## Understand

1. The grid is composed of strings and each cell is filled with either '1' (land) or '0' (water).
2. The definition of an island is plots of land surrounded by water. 
3. The area 'out of bounds' is water. It is not a continuous grid that wraps around.
4. Land can be connected horizontally or vertically but not diagonally.

Clarifying Questions: 
If the entire grid is filled with 1's do we assume that is one island, because the area out of bounds is defined to be water? Yes.

## Plan
The challenge with this problem appears to me to determine which pieces of land are connected to each other and to not double count. This requires keeping track of which areas of land you have already visited. 

What do I need to do
1. Identify a starting point to start mapping an island. 
    - Is the current tile I am on a '1'? 
    - Next, is it a tile I have visited or not?
2. Map an island
    - Tag the tile I am on as visited 
    - Determine where to move to next to keep searching the island.
    - Stop once I've run out of new land to visit.

3. Keep track of the number of independent islands.
- Requires determining whether I have fully mapped an island and I am now mapping a new island.

### Data Structures and Approach:
I think this approach lends itself well to grid search plus breadth first search. 
1. Loop through the grid and find unexplored land to start mapping. Add to the count of islands that you have visited.
2. From that starting point mark all adjacent land points as visted that are horizontal or vertically connected. I think I can use a breadth first search for this and run this in a separate function. In theory, each island is independent and should be fully explored one at a time so that function could just return the sets of land that have been visited rather than take in all visited land. But that's an optimisation can consider later
3. Stop when there are no more neighbours to visit. No neighbours when there is no new land, or surrounded by water either '0' tile or boundary of grid
4. Continue looping through the grid until get to the end. Return the count of islands

Question
1. When do I stop? When I have visited all pieces of land in the grid and determined which island do they belong to.
