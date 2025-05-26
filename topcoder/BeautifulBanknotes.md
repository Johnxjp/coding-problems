# Problem Statement

The time limit for this task is 5 seconds.

Absurdistan has N different banknote types.

There is a canonical order of all types by beauty, and the types are numbered from 0 (most beautiful) to N-1 (ugliest) in this order.

Each banknote type has a positive integer value. The values are unrelated to the banknotes' beauty, and they are not necessarily distinct. You are given their list in the int[] values.

A stunning collection of banknotes has the property that an uglier type cannot have more pieces in the collection than a more beautiful type. This rule also applies to types that aren't present in the collection: for example, a collection that has no banknotes of type 3 and two banknotes of type 4 is not stunning.

A tolerable collection of banknotes has the property that at most one type of banknotes prevents it from being stunning by having too many pieces. I.e., if the collection is not stunning but can be turned into a stunning collection by removing one or more banknotes, all of the same type, it is still considered tolerable.

Note that the definition says "at most one type", hence each stunning collection is also a tolerable collection.

For example, if we have banknotes of types 0, 0, 1, 2, 2, 2, 2, 2, 3, 4, we have a collection that is tolerable (but not stunning) as we can fix it by removing some banknotes of type 2.

The collection 0, 1, 2, 2, 3, 3 is not tolerable: you have too many banknotes of type 2, but if you remove some of them, you will have too many banknotes of type 3.

Count all tolerable collections of banknotes with the total value total. Return that count modulo 10^9 + 7. 

## Understanding

input: 
- Banknote value: int[] values

output: 
- number of collections, which are tolerable, and have total value = value (mod (10^9 + 7))

constraints:
- 

Banknote:
- beauty: int
- value: int

conditions:
- stunning: collection (represented by an array), can't have more uglier bank notes than more beautiful ones.
 - example: 

- tolerable: distribution of types, can become stunning if you can remove 1 or more from 0 or 1 particular types. If 0 i.e. stunning, collection is also tolerable

Example

0, 0, 1, 2, 2, 2, 2, 2, 3, 4,

count
- 0: 2
- 1: 1
- 2: 2
- 3: 1
- 4: 1


Example 2:
count
- 0: 1
- 1: 1
- 2: 2
- 3: 3

## Approach

Subproblems
1. Is this set of banknotes tolerable (which includes stunning)?
2. What is total value of a set of tolerable banks notes?
3. Can we create a tolerable collection with value = total
4. How many tolerable collections can we make value = total



Example 1: 


input: {1, 1}, 7
Expected output: 8

Input: 2 types of notes, both $1
unlimited notes

combinations:
- 7, 0
- 6, 1
- 5, 2
- 4, 3
- 3, 4
- 2, 5
- 1, 6
- 0, 7


input: {10, 20, 30, 40, 50}, 99947
returns: 0


Example 2:
input: {1, 1, 1}, 5
returns 16


A = [27, 34, 23] => Sum (A[i] * v[i]) = 5

Brute force:

- 1, 0, 0
- 0, 1, 0
- 0, 0, 1
- 2, 0, 0
- 1, 1, 0

Solutions, Target value, T
- N * v2, M * v2, ...., 


