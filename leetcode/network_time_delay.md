# Leetcode 743 Network Delay Time
You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

Constraints
- 1 <= k <= n <= 100
- 1 <= times.length <= 6000 
- times[i].length == 3
- 1 <= ui, vi <= n
- ui != vi
- 0 <= wi <= 100
- All the pairs (ui, vi) are unique. (i.e., no multiple edges.)

## Understanding

Input: A grid representing edges of a network. 
Output: An integer representing the time it takes for the valid portion of a graph to receive the signal

- Our input is an array of edges (ui, vi, wi). wi = time(ui -> vi) 
- The edges connect nodes ui or vi in the graph.
- nodes are just marked by an integer id. 
- Not all nodes are connected. It can be a disconnected graph
- No node is connected to itself
- All edges are unique.
- minimum time is not = sum (wi) but the maximum steps required to reach all nodes 

Clarifying
1. Can edges be directional? Is it possible to have an edge ui -> vi and edge vi -> ui which have different wi? Yes
edges are directional. So if we only have an edge ui -> vi and k = vi, then total time = -1 because no edge vi -> ui or
to another node.
2. Can there be cycles in the graph? Yes it can be

Problems we have to solve:

1. Identify which nodes are reachable from a given source node
2. Identify the minimum time it takes to visit a node from a given source node
3. Determine when we have reached all reachable nodes 
4. Determine if all reachable nodes is equivalent to all nodes in the graph
5. Determine when we have finished propagating the light

## Approach

We need to find out what is the minimum time it takes to get to a node. What is the largest time needed to visit all? Have we visited all?

Because we have to visit all nodes and we should test multiple paths to get to a node, it strikes me that DFS could be a good solution. We want
to explore all possible paths and then record the minimum time it takes to reach the furthest terminating node. I will also need to record
every node I have visited along all paths and determine if that is the entire set of nodes.

First approach. DFS

1. Given a starting point, figure out which nodes are connected and can visit next. 
2. Record the nodes we visit and time it takes us to get there
3. If we have visited a node and the time it took to get there is less than current path then stop
4. If we have no more adjacent nodes to visit stop. Return time to get to the node
5. Stop when we have explored all paths from the starting point
6. Count if number of nodes visited = all nodes. If no return -1
7. If yes, loop through and find the max time. Which should be the least amount of time to visit all nodes


### Data Structures
edge map: We should be able to quickly look up which nodes are connected and their weight. I think a data structure like
{source: [(target, weight), ...]} is appropriate

visited: this is a cache which records which nodes we have visited in our exploration and the time it takes to get there.




