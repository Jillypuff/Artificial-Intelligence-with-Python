---
id: ktznfgycrtusv057xnmsbl3
title: Search
desc: ''
updated: 1742056997958
created: 1741905766994
---
# Search
Search problems are defined as problems with a clear start and goal. Examples could be to solve a maze, to sort a list or to move from point A to point B.

# Agent
An entity that perceives its envioronment and acts upon that environment

# State
A configuration of the agent and its environment

# Initial state
The state in which the agent begins

# Actions
Choices that can be made in a state<br>
**ACTIONS(s)** returns the set of actions that can be executed in state **s**

# Transition model
A description of what state results from performing any applicable action in any state<br>
**RESULT(_s_, _a_)** return the state resulting from performing action _a_ in state _s_

![](\pics\transitionmodel.png)

# Goal test
A way to determine if a given state is a goal state.

# Path cost
Numerical cost associated with a given path

![](\pics\pathcost.png)

# Search Problems
- Initial state
- Actions
- Transition model
- Goal test
- Path cost function

# Solution
A set of *actions* that gets to the goal state

# Optimal solution
A set of *actions* that gets to the goal state in the lowest path cost possible

# Node
A data structure that keep track of:
- A State
- A Parent *(The node that generated this node)*
- An action *(What action was made to get to this node)*
- A path cost *(From initial state to the node state)*

# Approach to solve search problem
- Start with a frontier that contains the initial state
- Repeat:
    - <span style="color: red;">If the frontier is empty, then no solution</span>
    - Remove a node from the frontier
    - <span style="color: green;">If node contains goal state, return the solution</span>
    - Expand node, add resulting nodes to the frontier *(Add all possible states based on actions available to frontier)*

# Repeating patterns
If a action takes you back to a previous state it can create an infinite loop of going back and forth.

# Revised Approach to solve search problem
- Start with a frontier that contains the initial state.
- Start with an empty explored set.
- Repeat:
    - <span style="color: red;">If the frontier is empty, then no solution</span>
    - Remove a node from the frontier
    - <span style="color: green;">If node contains goal state, return the solution</span>
    - **Add the node to the explored set**
    - Expand node, add resulting nodes to the frontier **if they aren't already in the frontier or the explored set**

# DFS and BFS
**Stack, FILO**: First in last out, means that the latest node added to the frontier will be the first one selected for next loop<br>
**Queue, FIFO**: First in first out, means that the next node will be the first one in the frontier<br>
By using a stack we will create a _DFS, a depth first search_, that will go to the bottom of the tree primarly<br>
By using a queue we will create a _BFS, a breadth first search_, that will explore the most shallow node of the trees first<br>


# Implemention of the node and frontier in python
```python
import sys

class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action

class Frontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)
    
    def empty(self):
        return len(self.frontier) == 0
        
class StackFrontier(Frontier):
    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1] # -1 grabs last element in list
            self.frontier = self.frontier[:-1]
            return node
        
class QueueFrontier(StackFrontier):
    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0] # 0 grabs first element in list
            self.frontier = self.frontier[1:]
            return node
```

# Uninformed search vs informed search
**Uninformed search** is when the search strategy uses no problem-specific knowledge<br>
**Informed search** is when the search strategy uses problem-specific knowledge to find solution more efficiently

# GBFS Greedy best-first search
Search algorithm that expands the node that is closest to the goal, as estimated by a heuristic function _h(n)_

# Manhattan distance
One type of **GBFS** that ignores obstacles and calculates how many squares the state is from the goal
![alt text](\pics\manhattandistance.png)

# A* Search
Search algorithm that expands node with lowest value of _g(n)_ + _h(n)

_g(n)_ = cost to reach node<br>
_h(n)_ = estimated cost to goal

![alt text](\pics\astarsearch.png)

**A* search** is optimal if:
- _h(n)_ is admissible (never overestimates the true cost)
- _h(n)_ is consistent (for ever node _n_ and successor _n'_ with step cost _c, $h(n)  \leq h(n') + c$_)

# adversarial  search
When you have some force trying to stop you from reaching the goal, like a game

# Minmax
Is an algorithm to solve the adversarial search, to make the computer understand the goal of the game we can save outcomes as numbers
![alt text](\pics\minmaxtictactoe.png)
* **MAX (X)** aims to maximize score
* **MIN (O)** aims to minimize score

# Game
* **S0:** Initial state
* **Player_(s)_**: returns which player to move in state _s_
* **Actions_(s)_**: return legal moves in state _s_
* **Result_(s, a)_**: returns state after action _a_ taken in state _s_
* **Terminal_(s)_**: checks if state _s_ is a terminal state _(a state where no actions can be taken, aka game is finished)_
* **Utility_(s)_**: Final numerical value for terminal state _s_

