import numpy as np
import math
import time
import random


def print_state(state):
    if state is None:
        return
    print "\n", state[0:3]
    print state[3:6]
    print state[6:9], "\n"


def up(state):
    # Find position of zero
    pos_zero = np.argmin(state)
    if pos_zero < 6:
        state[pos_zero] = state[pos_zero + 3]
        state[pos_zero + 3] = 0
    else:
        pass
    return state[:]


def down(state):
    # Find position of zero
    pos_zero = np.argmin(state)
    if pos_zero > 2:
        state[pos_zero] = state[pos_zero - 3]
        state[pos_zero - 3] = 0
    else:
        pass
    return state[:]


def right(state):
    # Find position of zero
    pos_zero = np.argmin(state)
    if pos_zero not in [0, 3, 6]:
        state[pos_zero] = state[pos_zero - 1]
        state[pos_zero - 1] = 0
    else:
        pass
    return state[:]


def left(state):
    # Find position of zero
    pos_zero = np.argmin(state)
    if pos_zero not in [2, 5, 8]:
        state[pos_zero] = state[pos_zero + 1]
        state[pos_zero + 1] = 0
    else:
        pass
    return state[:]


def distance_states(s1, s2):
    d = 0
    for i in range(len(s1)):
        d += (s1[i] - s2[i])**2
    return math.sqrt(d)


# state = range(9)
state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
print "Initial state : "
print_state(state)

for i in range(10):
    n = random.randint(1,4)
    if n == 1:
        state = up(state)
    elif n == 2:
        state = down(state)
    elif n == 3:
        state = right(state)
    else:
        state = left(state)
    print "Intermediate state number ", i, " : "
    print_state(state)

print "Final state : "
print_state(state)

