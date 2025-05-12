# Leetcode 695: Max Area of Islands
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

## Understand
The objective is to return a single integer which denotes the area of the largest island. The input is a grid of integer 0 or 1 values.

1. The data is a binary integer grid of size m, n where m is not necessarily equal to n.
2. Land is marked by the value 1. Water by value 0
3. The area out of bounds is stated to be water
4. An island is land connected either horizontally or vertically. Diagonal connections are not valid.
5. The area of an island is the number of unique tiles of land

Edge cases:
- if there are no islands, return 0

### Clarifying Questions
If the entire grid is filled with 1's do we assume that is one island, because the area out of bounds is defined to be water? Yes.

## Plan
To solve this problem I will need to break it down into sub-tasks. The sub-tasks seem to be:

1. Determine when to start mapping an island
2. Map an island and determine it's area
3. Track islands and there area. We technically only need to track the size of the biggest island. Therefore it doesn't matter if there are two islands competing to be the largest
4. Determine when we are done exploring the grid

We need to be careful not to double count pieces of an island so we have to track tiles we are visiting

### Approach

1. We should loop over the grid and start exploring when we encounter a piece of land that we have previously unexplored. This should indicate we have found a new island to explore.
2. We then need to keep track of the islands size
3. We then need to find next parts of the island to explore. The valid locations will be those that are in the boundaries of the grid, not water, not unvisited land. 
4. In this case it does not matter what order we visit valid areas of land.

We can take a BFS approach to this

### Data Structures

1. We can use a set to track the pieces of land we have visited
2. We can use a simple counter to keep track of the area. We add 1 to the counter when we add a new piece of land to visited set

