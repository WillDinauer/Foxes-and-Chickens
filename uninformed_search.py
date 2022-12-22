from collections import deque
from SearchSolution import SearchSolution


class SearchNode:
    # each search node except the root has a parent node
    # and all search nodes wrap a state object

    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent


# Breadth-first search
def bfs_search(search_problem):
    search_solution = SearchSolution(search_problem, "BFS")

    # Set up the 'frontier' queue and 'seen' set
    start_node = SearchNode(search_problem.start_state)
    frontier = deque()
    frontier.append(start_node)
    seen = set()
    seen.add(search_problem.start_state)

    # While there are still unvisited nodes
    while len(frontier) > 0:
        # Get the next node/state
        search_solution.nodes_visited += 1
        current_node = frontier.pop()
        current_state = current_node.state

        # Check if this state is the goal state
        if search_problem.goal_test(current_state):
            # Perform a backtrace to create the solution path
            while current_node is not None:
                search_solution.path.insert(0, current_node.state)
                current_node = current_node.parent
            break

        # Wrap unseen successor states in a node and add them to the frontier
        for child in search_problem.get_successors(current_state):
            if child not in seen:
                seen.add(child)
                child_node = SearchNode(child, current_node)
                frontier.append(child_node)

    return search_solution


# We pass the solution along to each new recursive call to dfs_search
#  so that statistics like number of nodes visited or recursion depth
#  might be recorded
def dfs_search(search_problem, depth_limit=100, node=None, solution=None):
    # if no node object given, create a new search from starting state
    if node is None:
        node = SearchNode(search_problem.start_state)
        solution = SearchSolution(search_problem, "DFS")

    # Add the current node to the path
    solution.path.append(node.state)
    solution.nodes_visited += 1

    # BASE CASE: current node's state is the goal state
    if search_problem.goal_test(node.state):
        return True
    # Base case for maximum depth reached
    if len(solution.path) > depth_limit:
        solution.path.remove(node.state)
        # Return the empty solution if we are at the root.
        # Otherwise, return False to prevent further recursion
        if node.parent is None:
            return solution
        return False

    # Recurse over all children
    for child in search_problem.get_successors(node.state):
        if child not in solution.path:
            # Package child state as a node
            child_node = SearchNode(child, node)
            # Recursive call - returns True if goal was found at or below this node
            if dfs_search(search_problem, depth_limit, child_node, solution):
                if node.parent is None:
                    return solution
                else:
                    return True

    # Dead end - remove the current node from the search path
    solution.path.remove(node.state)
    if node.parent is None:
        return solution
    return False


# Iterative Deepening Search
def ids_search(search_problem, depth_limit=100):
    solution = SearchSolution(search_problem, "IDS")
    for depth in range(0, depth_limit):
        dfs = dfs_search(search_problem, depth)
        # Revisiting nodes counts towards nodes visited. Sum them up for every DFS call.
        solution.nodes_visited += dfs.nodes_visited
        # Found a valid solution! Save the path and break out
        if len(dfs.path) > 0:
            solution.path = dfs.path
            break
    return solution
