import math
import numpy as np


class State():

    def __init__(self):
        table_of_states = {}
        goal_state = '123456780'
        initial_state = '013526478'

    def get_tag(self, state):
        tag = ''
        for i in state:
            tag += str(i)
        return tag

    def get_state(self, tag):
        state = []
        for i in range(9):
            state.append(int(tag[i]))
        return state[:]

    def find_minimum_cost_in_list(self):
        max1 = max([x[1] for x in dic.values()])
        max2 = [x for x in dic.values() if x[1] == maxx1]
        key = [x for x,y in dic.items() if y == maxx2[0]]
        return key

    def distance_states(s1, s2):
        d = 0
        for i in range(len(s1)):
            d += (s1[i] - s2[i])**2
        return math.sqrt(d)

    def compute_h(self, state):


    def up(self, state):
        # Find position of zero
        pos_zero = np.argmin(state)
        if pos_zero < 6:
            state[pos_zero] = state[pos_zero + 3]
            state[pos_zero + 3] = 0
        else:
            pass
        return state[:]

    def down(self, state):
        # Find position of zero
        pos_zero = np.argmin(state)
        if pos_zero > 2:
            state[pos_zero] = state[pos_zero - 3]
            state[pos_zero - 3] = 0
        else:
            pass
        return state[:]

    def right(self, state):
        # Find position of zero
        pos_zero = np.argmin(state)
        if pos_zero not in [0, 3, 6]:
            state[pos_zero] = state[pos_zero - 1]
            state[pos_zero - 1] = 0
        else:
            pass
        return state[:]

    def left(self, state):
        # Find position of zero
        pos_zero = np.argmin(state)
        if pos_zero not in [2, 5, 8]:
            state[pos_zero] = state[pos_zero + 1]
            state[pos_zero + 1] = 0
        else:
            pass
        return state[:]

    def actions(self,state):
        possible_states = [up(state), down(state), left(state), right(state)]
        possible_unique_states = []
        for i in possible_states:
            if i not in possible_unique_states:
                possible_unique_states.append(i)
        return possible_unique_states[:]


