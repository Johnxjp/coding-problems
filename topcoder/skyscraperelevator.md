## Problem Statement

There is a skyscraper with floors numbered from 0 (the lobby) to N, inclusive.

The skyscraper has a single elevator. Initially, the elevator is in the lobby, i.e., its initial floor is 0.

In the lobby, the elevator has a display showing its current floor.

The elevator needs 1 second to move one floor up or down. A person needs 20 seconds to move one floor up when using stairs.

Everything else in this problem (e.g., pushing buttons, getting onto and off the elevator, etc.) happens instantly. E.g., if the elevator is on floor 7 and a new person arrives to the lobby, calls the elevator, waits for it, enters the elevator, pushes the "10" button, rides the elevator to floor 10 and then gets off the elevator, the whole process takes exactly 7 + 10 = 17 seconds.

A sequence of people will enter the lobby of the building, one person at a time. Each person is going to a specific floor. These floors are given in the int[] people, in the order in which the people will arrive.

Whenever a person enters the lobby, they look at the elevator's display and determine the fastest way to get to their desired floor:

    If taking the stairs is strictly faster, they take the stairs.
    Otherwise (if taking the elevator is equally fast or faster than taking the stairs) they take the elevator.

(The people know both their own speed and the elevator's speed so they always correctly determine which option is better for them.)

Each person will follow the rule given above when deciding whether to take the elevator. Each person will complete their journey before the next person enters the building.

For each person, calculate the number of seconds in which they will reach their destination. Return the sum of those times. 


## Understanding

Input: 
- floors, number of floors in the skyscraper
- integer array, represents people and floors they are travelling to
Output: 
- integer, sum of time taken for a person to reach their destination the fastest

clarifications:
- Each person will follow the rule given above when deciding whether to take the elevator. Each person will complete their journey before the next person enters the building. 
- elevator does not need to come to lobby at end
- Each element of people will be between 1 and N, inclusive.

## Approach

Example
N = 47000, P = {19, 1, 1000}
Returns: 1040

Elevator always on the lobby, floor zero.

1 person, takes elevator, 19 seconds
2 person, takes elevator, 20 seconds (19 down, 1 up)
3 person, takes elevator, 1001 seconds (1 down, 1000 up)
= 1040

Time to take elevator = sum(current floor to lobby + floor the person wants to get to)
Time to take the stairs = 20 * floor they want to get to

Subproblem
- tracking where the elevator is
