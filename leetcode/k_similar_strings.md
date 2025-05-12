# Leetcode 854: K-Similar Strings
Strings s1 and s2 are k-similar (for some non-negative integer k) if we can swap the positions of two letters in s1 exactly k times so that the resulting string equals s2.

Given two anagrams s1 and s2, return the smallest k for which s1 and s2 are k-similar.

Constraints:

    1 <= s1.length <= 20
    s2.length == s1.length
    s1 and s2 contain only lowercase letters from the set {'a', 'b', 'c', 'd', 'e', 'f'}.
    s2 is an anagram of s1.

## Understanding
Input: two strings which are anagrams. They are always anagrams!
Objective: return minimum number of swaps

1. Important, here is that they are anagrams. So they have the same count of letters
2. They only contain lowercase letters
3. They only contain letters from [a-f]. I'm not sure why this is significant just yet
4. The number of letters out of place is not always even

Edge cases:
1. A == B, in which case k = 0

## Approach
We need to use the fact they are anagrams to solve this. One approach is to fix one string, and then compare

Sub-problems:

1. How to know when we are done? We know when we are done when S1 = S2. They are short so this is a quick check
2. We need to keep track of which letters are in the right place and which aren't
3. We need to decide where to place a letter that needs to be swapped
4. We need to track which swaps we have previously made

Solving the tracking
2. As there could be multiple characters which are the same, we can't use a set.
- We could possibly use a list of some kind which simply stores the out of place letters / indexes.
- We could have a binary list which marks letters in the correct place as 1 and otherwise 0
- We could have a map where keys are the letters and values is a list of incorrect positions.

3. We need to decide where to place a letter that needs to be swapped. 
- We can do a look up in a map that shows correct positions. This can be built from the second string.

Approach:

0. Initialise the problem. Create a map of the letters and their correct position from S2. Set k = 0. incorrect indexes = []
1. Loop through the string and mark indexes where letters in S1 != S2. If no positions are marked then stop and return k
2. Go through the out of place indexes one by one. Look up the right position
3. Take the first right position which doesn't have a correct letter in that place already and swap.
4. Pass the new string along and increment swaps. Repeat steps 1-3 until right. 
5. Come back up and try another order of swaps

This is probably inefficient. Because we can swap two letters and end up in the same position e.g. we can swap (a, 1)->(f, 3) or (f, 3)->(a, 1). We
already solved this problem so we are repeating work. We could store a map with {string: k, ...}

Thoughts. 
1. We should decide to swap letters if we can get them both into the right position rather than swapping a letter where only one
would end up in the right spot. This is an infrequent case but can happen if you have multiple letters in a string which is the 
case in this problem

For example:
- aabca & abaac. We should not do acbaa -> acaba -> aaabc -> abaac. We should do abaca -> abaac

There might even be a way to figure out the optimal number of swaps simply from the number of letters, set length and number of letters
out of place.

## Milestones
Get a solution working on short strings
