# Topcoder Wedding Dance Floor
https://archive.topcoder.com/ProblemStatement/pm/18170

## Problem Statement

Maurice is planning a new business: running a hall which one can rent for a wedding reception. He understands that people have two basic needs when renting such a hall: you need to cram as many people as possible in it, and there has to be a large-enough dance floor for them.

The hall Maurice rents is a H by H square.

For a hall this big, the minimum size of a suitable dance floor is a D by D square.

Maurice just found a great deal to make a bulk purchase of dinner tables. Each of these tables (along with room for chairs around it) will exactly cover a 1 by T rectangle. (Each rectangle can be placed either "horizontally" or "vertically".)

Help Maurice: find out whether it's possible to arrange his hall so that there is exactly one dance floor of the smallest possible size, and the rest of the hall is completely covered with tables.

If no such arrangement exists, return an empty String[].

If multiple such arrangements exists, you may pick any one of them. Return a String[] with the bitmap of your arrangement. Use the character 'D' to represent the dance floor, and other letters and numbers (a-z, A-C, E-Z, 0-9) to represent the tables.

(All unit square cells that belong to the same table should have the same character. Each pair of tables that are adjacent must have different characters. You may reuse the same character for multiple mutually non-adjacent tables.) 

## Understanding
From the first sentence we understand that this problem is maximisation under a constraint: maximise number of people, whilst ensuring still enough room to dance. This tells me it is an optimisation problem.


input: 
- H, the length and width of hall space
- D, the minimum size of dance floor. (this is the constraint)
- T, the length of a table (can be arranged vertically or horizontally)

output:
- A bitmap showing the arrangement of dance floor and tables. Represent dance floor with D, and anything else e.g. 0 or '.', as tables.
    - if an arrangement doesn't exist then return empty string.
    - Separate tables must be represented with different letters.

clarification:
- does there have to be a buffer around the table?
- All tables are of the same size 1xT
- Zero tables is valid


## Plan
Questions:
- Does it matter how the tables are arranged? We need to know if there is a DxD space available. If we can remove the area of the rest of the squares, would it be possible to just divide this area by the required tables? Or does shape of space play a part? If it was fragmented space I would say yes, but as the dance floor is space, I'm wondering if this is true.

Given the quetion, I presume it's not that simple. Plus there are constrains on the size of the space and T might be bigger or smaller than these which make it impossible to fill. However, we can use the area constraint to check if we can fit X amount of tables. (HxH - DxD) % 8 == 0, if can fit them all. This is a necessary but not sufficient condition.


We can try to solve this problem first without being concerned with the mapping different tables. If we can fit all tables then afterwards we can assign mapping as we go along, it will just be something that needs to be tracked.

Problems that we need to solve / decisions that we make

1. where should we place the dance floor D?
2. Given position of D, how do we place tables? 
    2a. Where do we place a table?
    2b. Do we place a table horizontally or vertically? This is only a decision if T > 1.

Subproblem 1:
1. How do we place the dance floor? This can easily be done by iterating through the grid starting at 0,0 and ending each row and column at H - D, which represents the top left hand corner of the dance floor.

2. For each position of dance floor, we need to solve table arrangement.
- We can maybe solve this greedily and try to insert a table one at a time. Whenever, we can't insert a table we can undo and try a different arrangement, if we can't insert a table either vertically or horizontally then we backtrack. If we are at the first table then we move the dance floor on. If the dance floor has approached everything then we lose.


- When do we stop? We stop when the remaining area of the floor is zero. If the remaining area is zero then we have successfully solved the issue. 

