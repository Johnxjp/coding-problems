# Topcoder: Candybowlgame
The candy game is played with N bowls of candies. The bowls are arranged in a row and numbered from 0 to N-1 sequentially.

The game is played by two players who take alternating turns. The player unable to take a valid turn loses the game. Each turn, the current player has two options:

    Select a bowl that currently contains at least two candies. Eat exactly two of those candies.
    Select an odd number k. Select a bowl x &gt;= k that currently contains at least k candies. Take exactly k candies from bowl x and place them into bowl (x-k).

(For example, suppose you select the odd number k = 3. If bowl 10 contains 100 candies, you may select x = 10. You will then take the k = 3 candies from bowl x = 10, leaving 97 candies there, and you will add those three candies to whatever is in bowl x-k = 7.)

You are given the initial distribution of some candies: the int[] C with N elements such that for each i, bowl i contains C[i] candies.

You are also given E extra candies that have to be added to the bowls. (You must add each of the E candies to one of the bowls.)

A distribution of candies is winning if the player who starts the game has a winning strategy - i.e., a strategy such that the starting player following that strategy is guaranteed to win the game, regardless of what their opponent does.

Consider all different candy distributions that can be obtained by starting with the distribution C and then adding the E extra candies. Among them, count all winning ones. Return their count modulo 10^9 + 7. 

## Understanding
input:
- n bowls of candy, each bowl contians a different amount of candies
- extra candies, E, to be added to the bowl.

output:
- Number of 'winning' candy distributions % (10^9 + 7)

constraints:
- All candies E must be added to a bowl
- 1 <= C <= 100
- 0 <= C[i] <= 10^9
- 0 <= E <= 10^6

A player wins when:
- The other player cannot take a valid turn


Valid turn
1. a player must eat exactly 2 candies from a bowl that contains at least candies
2. choose an odd number k, and select a bowl X >= k that contains at least k candies. Take k candies from X and place them into X-k

Condition 2. k has to be a number that is < max(all Bowls), otherwise cannot take exactly k candies.

clarifications:
- Candies are indistinguishable, which means (1, 1) is unique.
- 'winning' strategy is only considered for the player who starts the game. Therefore can have winning strategies >= 0. 


## Approach
Think about the state of the game at a point in time. There are 2 players alternating.

We know the board state is defined by the current distribution of C and E and player turn (P). Each player wants to win so 
we consider them to take optimal turns. Therefore important to track both states.

state = (C, E, P)
At a given state, we will have many possible options of what we can do. Therefore we have to solve the sub-problem of 
what our choice is:

1. eat 2 candies from a bowl >= 2 candies
2. choose X and choose k. (here is interesting)


E gets added to the bowl at the beginning of the game. Therefore a game distribution is really C. So we say
from a given C can player 1 win? You're asking, how many ways can I distirbute E across C so that player 1 can win and you need
to use all E.

We must also calculate winning every turn, by considering if there are any moves. If there are then we return that and store
it in the state that we have 1 winning move. This could go on for a very long time in the case of large numbers.

There's probably an way to avoid calculating all the distributions because at some point the pattern will remain the same. 


What's the brute force way of solving this and what are the subproblems?

1. How do we distribute E across C so that player 1 will win?
- How to distribute E? In theory 1 candy can go in each bowl. But certain states are the same. 
- How many different unique states are there? How do I produce them in sequence without double counting?
2. run the game
- decide if will eat 2 or choose k
 - choose k
 - choose x


 How do I produce all the states in sequence without double counting?
 


 