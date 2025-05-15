# Leetcode 20: Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.


## Understanding

input: string of just bracket
output: boolean, if string valid
constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

clarifications:

- open brackets need to be closed in order so '([)]' would be invalid

## Plan

## Subproblems:

What subproblems do I need to solve?

1. I need to keep track of the open brackets
2. I need to figure out when I encounter a closing bracket if I have the right open bracket. 
3. How do I know if complete?

What algorithm / data structures might best fit this?
- Stack
- Key insight is that strings must be closed in order. So we should keep track of the open brackets and then whenever we encounter the


