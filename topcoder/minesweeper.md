# Minesweeper 
 Minesweeper strings are strings of length N with the following properties:

    Each character is either a '*' (representing a mine) or a digit: '0', '1', or '2'.
    The value of each digit must be equal to the number of mines adjacent to it.

For example, for N = 7:

    "0000000" is a valid minesweeper string with no mines.
    "*******" is a valid minesweeper string with seven mines.
    "0001*2*" is a valid minesweeper string with two mines.
    "0001000" is not a valid minesweeper string because the number of mines adjacent to the '1' in the middle is not 1.
    "**0001*" is not a valid minesweeper string because the number of mines adjacent to the leftmost '0' is not 0.
    "2*1*02*" is not a valid minesweeper string: all digits are wrong.

Suppose we order all valid minesweeper strings lexicographically (i.e., using the ASCII values of the characters that form them) and then number the sorted order starting from 0.

Given the string length N and the non-negative integer X, find the minesweeper string number X in the order described in the previous paragraph. Return that string, or an empty string if no string has the number X. 

Constraints

    N will be between 1 and 60, inclusive.
    X will be between 0 and 10^18, inclusive.

input: minesweeper string length N, rank X of string to return 
output: minesweeper string at position X

will be sorted from smallest to largest, 0-based ordering.

## Approach

Subproblems to solve
1. Is a string valid?
2. How many total valid strings are there?
3. What rank is this string?
4. Is string A > B?
5. How can I find the next (or previous) valid string given a string?

There are up to 10^18 possible combinations which already indicates it will be almost impossible to generate all the possible combinations. It will take too long for an algorithm to do this.

My thinking is maybe we can solve solve this problem by treating it as a search problem instead of a permutation or generation problem. For example, we might be able to figure out how many possible valid strings there are for a given string length. 

This is a combinatorics problem unfortunately, which I don't know how to solve.

The minimum string: '*' * N
The maximum 'valid' string will be a combination of 1s, 2s and *s. It cannot start or end with 2 because board ends at edges. It must be something like
1*2*2*....  * 1, (N - 2 // 2) * 2 [if odd, 2 in the middle], (N - 2 // 2) * 

Something like this might not work depending on string length e.g. 4 chracters. 1 * 2 *, or * 2 * 1. It would end on 1 if (N - 1) = odd. Otherwise will end on '*'

The maximum invalid string = 2 * N

Assuming we have an ordered list already, how would we find the string at X? Just pick it out with the index. 


Is there anyway we can begin to guess at solutions and then probe around that solution for the X position? Or do some kind of smarter search?

Subproblems:

Is a string valid?
- Loop through string, when we encounter a number, check the indexes to the left and right to confirm the number of "*" is equal to that number.


How many total valid strings are there?
We need this because they ask us to return an empty string if no string has the number X, which can only happen if X > number of valid strings. which is true if X > N and X <= N but valid strings < X.


I don't know if this is calculatable. Maybe there's a math formula that uses combinatorics to get the result. Otherwise, perhaps, can I inverse the problem?


Let's see if I can figure out how to generate numbers in order myself: 
N = 4. Valid strings. Order is always * -> 0 -> 1 -> 2

N = 1, 2
*
0


N = 2. 4, From low to high
**
*1
00
1*

N = 3, 8
***
**1
*10
*2*
000
01*
1**
1*1

N = 4, 14
****
***1
**10
**2*
*100
*2**
*2*1
0000
001*
01**
1***
1**1
1*10
1*2*

N = 5, 24
*****
****1
***10
***2*
**100
**2**
**2*1
*1000
*2***
*2**1
*2*10
00000
0001*
001**
001*1
01*10
01*2*
1****
1***1
1**10
1**2*
1*100
1*2**
1*2*1




