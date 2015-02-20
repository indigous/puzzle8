#!/usr/bin/python

import numpy as np
import sys


class Puzzle8():

    def __init__(self, start, goal):
        # List = {'tag' : [G, H, F, Parent, Explored]}
        self.table_of_states = {}
        self.goal_state = self.get_state(goal)
        self.initial_state = self.get_state(start)
        self.current_state = []
        self.reachable_states = []
        self.counter = 0
        self.table_coord = {0: (0, 0), 1: (0, 1), 2: (0, 2), 3: (1, 0), 4: (1, 1), 5: (1, 2), 6: (2, 0),
                            7: (2, 1), 8: (2, 2)}

    def get_tag(self, state):
        tag = ''
        for i in state:
            tag += str(i)
        return tag

    def add_state_to_list(self, tag, g, h, parent, explored):
        self.table_of_states[tag] = [g, h, g + h, parent, explored]
        return

    def print_state(self, state):
        print "\n", state[0:3]
        print state[3:6]
        print state[6:9], "\n"
        return

    def get_state(self, tag):
        state = []
        for i in range(9):
            state.append(int(tag[i]))
        return state[:]

    def find_state_minimum_cost(self):
        my_list = [x for x in self.table_of_states.values() if x[-1] == 0]
        min1 = min([x[2] for x in my_list])
        min2 = [x for x in my_list if x[2] == min1]
        key = [x for x, y in self.table_of_states.items() if y == min2[0]]
        # min1 = min([x[2] for x in self.table_of_states.values()])
        # min2 = [x for x in self.table_of_states.values() if x[1] == min1]
        # key = [x for x,y in self.table_of_states.items() if y == min2[0]]
        if type(key) == list:
            return key[0]
        return key

    def distance_states(self, s1, s2):
        d = 0
        for i in range(len(s1)):
            ind1 = self.table_coord[s1.index(i)]
            ind2 = self.table_coord[s2.index(i)]
            d += abs(ind1[0] - ind2[0]) + abs(ind1[1] - ind2[1])
        return d

    def compute_h(self, state):
        return self.distance_states(state, self.goal_state)

    def mark_as_explored(self, state):
        self.table_of_states[self.get_tag(state)][-1] = 1
        return

    def print_sequence(self, state):
        list_sequence = [self.get_tag(state)]
        i = self.table_of_states[self.get_tag(state)][3]
        while i != 0:
            list_sequence.append(i)
            i = self.table_of_states[self.get_tag(i)][3]
        count = 1
        for j in reversed(list_sequence):
            if count == 1:
                print "\nInitial state :"
                self.print_state(self.get_state(j))
            elif count == self.counter + 1:
                print "Goal state :"
                self.print_state(self.get_state(j))
            else:
                print "Step ", count-1
                self.print_state(self.get_state(j))
            count += 1

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

    def get_possible_states(self, state):
        possible_states = [self.up(state[:]), self.down(state[:]), self.right(state[:]), self.left(state[:])]
        possible_unique_states = []
        for i in possible_states:
            if i not in possible_unique_states and i != state:
                possible_unique_states.append(i)
        return possible_unique_states[:]

    def find_by_a_star(self):
        # Mark initial state as current state
        self.current_state = self.initial_state[:]
        # Put the initial state in the list as open (not explored)
        self.add_state_to_list(self.get_tag(self.initial_state), 0, self.compute_h(self.initial_state), 0, 0)
        # Reset the counter
        self.counter = 0

        # Loop until reaching goal state
        while self.current_state != self.goal_state and self.counter < 300000:
            self.mark_as_explored(self.current_state)
            # print "current state : "
            # self.print_state(self.current_state)
            self.reachable_states = self.get_possible_states(self.current_state)
            # print "reachable states : "
            # for i in self.reachable_states:
            #     self.print_state(i)

            for state in self.reachable_states:
                tag = self.get_tag(state)
                g = self.table_of_states[self.get_tag(self.current_state)][0] + 1
                if tag not in self.table_of_states:
                    self.add_state_to_list(tag, g, self.compute_h(state), self.get_tag(self.current_state), 0)
                elif self.table_of_states[tag][0] > g:
                    self.table_of_states[tag][0] = g
                    self.table_of_states[tag][2] = g + self.table_of_states[tag][1]
                    self.table_of_states[tag][3] = self.get_tag(self.current_state)
                    self.table_of_states[tag][-1] = 0

            self.current_state = self.get_state(self.find_state_minimum_cost())
            # print "selected state : "
            # self.print_state(self.current_state)
            self.counter += 1

        print "\nNumber of steps = ", self.counter
        self.print_sequence(self.current_state)



if __name__ == "__main__":
    puzzle = Puzzle8(sys.argv[1], sys.argv[2])
    # puzzle = Puzzle8('013425786', '123456780')
    puzzle.find_by_a_star()
