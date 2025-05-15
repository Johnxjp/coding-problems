# Leetcode 53: Maximum Subarray

Given an integer array nums, find the subarray with the largest sum, and return its sum.

## Understand
input: integer array
output: sum of the subarray with largest sum
constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104

clarifications:
Is 0 a valid answer if all numbers are negative? so the subarray = []. No

Examples:
- input: [-2,1,-3,4,-1,2,1,-5,4], output: 6


## Plan
### Approach
Working through an example:
[-2,1,-3,4,-1,2,1,-5,4,6]


What subproblems do I need to solve?

1. When should I move the subarray start forward (or reset) and when should I extend the current subarray?
- When the sum of running_sum + x[j] is less than the value of x[j], then shift the array forward to start from x[j] and that will be the largest sum.
- We keep extending right until we have a new start point that meets the above criteria. 

What algorithm / data structures might best fit this?