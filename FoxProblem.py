class FoxProblem:
    def __init__(self, start_state=(3, 3, 1)):
        self.start_state = start_state
        self.goal_state = (0, 0, 0)
        self.total_chickens = start_state[0]
        self.total_fox = start_state[1]

    # get successor states for the given state
    def get_successors(self, state):
        # Create a successors list to add to
        successors = []
        # Create and validate states if the boat is on the left
        if state[2] == 1:
            s = (state[0] - 1, state[1], 0)             # One Chicken Leaves
            if self.validate_state(s):
                successors.append(s)
            s = (state[0] - 2, state[1], 0)             # Two Chickens Leave
            if self.validate_state(s):
                successors.append(s)
            s = (state[0], state[1] - 1, 0)             # One Fox Leaves
            if self.validate_state(s):
                successors.append(s)
            s = (state[0], state[1] - 2, 0)             # Two Foxes Leave
            if self.validate_state(s):
                successors.append(s)
            s = (state[0] - 1, state[1] - 1, 0)         # One Fox and One Chicken Leave
            if self.validate_state(s):
                successors.append(s)
        # Create and validate states if the boat is on the right
        else:
            s = (state[0] + 1, state[1], 1)             # One Chicken Returns
            if self.validate_state(s):
                successors.append(s)
            s = (state[0] + 2, state[1], 1)             # Two Chickens Return
            if self.validate_state(s):
                successors.append(s)
            s = (state[0], state[1] + 1, 1)             # One Fox Returns
            if self.validate_state(s):
                successors.append(s)
            s = (state[0], state[1] + 2, 1)             # Two Foxes Return
            if self.validate_state(s):
                successors.append(s)
            s = (state[0] + 1, state[1] + 1, 1)         # One Fox and One Chicken Return
            if self.validate_state(s):
                successors.append(s)
        return successors

    # Validates whether a particular state is allowable or not
    def validate_state(self, state):
        # We check to make sure the number of chickens and foxes is within an allowable range.
        # (ex. Total Chickens >= Current Number of Chickens >= 0)
        # Then, we check to make sure chickens aren't outnumbered on either side of the river
        # (if at least one chicken is present)
        if state[0] > self.total_chickens or state[1] > self.total_fox or state[0] < 0 or state[1] < 0 \
                or state[1] > state[0] > 0 or self.total_fox - state[1] > self.total_chickens - state[0] > 0:
            return False
        return True

    # tests is we've reached the goal state or not
    def goal_test(self, state):
        if state == self.goal_state:
            return True
        return False

    def __str__(self):
        string = "Chickens and foxes problem: " + str(self.start_state)
        return string


# A bit of test code
if __name__ == "__main__":
    test_cp = FoxProblem((5, 5, 1))
    print(test_cp.get_successors((5, 5, 1)))
    print(test_cp)
