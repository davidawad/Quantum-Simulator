#!/usr/bin/env python
# encoding: utf-8

from cmath import exp, pi, sqrt
from random import random
import itertools

def vectorflip(bitstring):
    """
        returns flipped bits in a given string
    """
    if not bitstring: raise TypeError("vectorflip passed None")
    return ''.join('1' if x == '0' else '0' for x in bitstring)

def bitflip(bitstring, qubit):
    """
        returns opposite state for a specific qubit
    """
    if not bitstring or not qubit: raise TypeError("bitflip passed None")
    arr = list(bitstring)
    arr[qubit-1] = '1' if qubit is '0' else '0'
    return ''.join(arr)

class System:
    """
        This class represents the wave function describing a
        basic quantum computer consisting of n qubits.
    """
    def __init__(self, num_qubits):
        """
        set up a quantum system with the given number of qubits
        initialized to the "zero" qubit.
        """
        self.num_qubits = num_qubits
        # In this classical simulation,we use 2^n Qubit complex numbers
        # this array of size 2^n will replicate the 2^n states Qubits can have
        self.amplitudes = [0] * (1 << num_qubits)  # use bitshift to realize 2^n
        self.amplitudes[0] = 1  # so that sum of prob.s is 1, starting in 000 state
        self.states = self.generate_states(num_qubits)

    def generate_states(self, num_qubits):
        """
        returns a dictionary of all possible states for n qubits
        in the format { 'state': 'amplitude' } e.g. { 010 : 0j}
        """
        if num_qubits <= 0:
            raise ValueError("simulation requires at least 1 qubit")
        # generate table of states using itertools
        tuples = [''.join(_) for _ in itertools.product(['0', '1'], repeat=num_qubits)]
        data = {}
        map(lambda x: data.update({x:0}), tuples)
        # so that sum of squared amplitudes is 1, assume starting in 000 state
        data['000'] = 1
        return data

    def collapse(self):
        """
        collapse the system (i.e. measure it) and return the state
        based on a random choice from the weighted distribution
        """
        total = 0
        r = random()
        for state in self.states.keys():
            total += abs(self.states[state])**2
            if r <= total: # randomly selected weighted number
                # reset amplitudes after system collapse
                self.states = { x:0 for x in self.states }
                self.states['000'] = 1
                return state

    def amplitude(self, state):
        """
        takes in a possible state of the system such as '010' and returns
        the amplitude of that possible state.
        """
        if len(state) > num_qubits:
            raise ValueError("State doesn't exist")
        # grab binary representation of state, access that array position
        return self.states[state]

    def probability(self, state):
        """
        simply returns the square of the absolute value
        of the amplitude for a given state
        """
        if not state: raise TypeError("state passed as None")
        return abs(self.states[state])**2

    def pi_over_eight(self, qubit):
        """
        applies a π/8 gate to the given qubit
        """
        if qubit > self.num_qubits:
            raise ValueError("Qubit %s not in system" % qubit)
        for state in self.states:
            if state[qubit-1] is '0': # given qubit is 0 in this possible state
                self.states[state] *= exp(-1j * pi / 8)
            else: # given q bit is 1 in this possible state
                self.states[state] *= exp(1j * pi / 8)
        return

    def hadamard(self, qubit):
        """
        applies a Hadamard gate to the given qubit.
        """
        if qubit > self.num_qubits:
            raise ValueError("Qubit %s not in system" % qubit)
        # make complete copy as values update simultaneously
        copy = {k:v for k,v in self.states.items()}
        for state in self.states.keys():
            if state[qubit-1] is '0': # given qubit is 0 in this possible state
                print(state)
                self.states[state] = (copy[state] + copy[bitflip(state, qubit)]) / sqrt(2)
            else: # given qubit is 1 in this possible state
                self.states[state] = (copy[bitflip(state, qubit)] - copy[state]) / sqrt(2)

    def controlled_not(self, control, target):
        """
        applies a controlled-not gate using the first given qubit as the
        control of the permutation of the second.
        """
        # the two qubits have to valid and different
        if control > self.num_qubits or target > self.num_qubits:
            raise ValueError("Qubit %s not in system" % qubit)
        if control == target:
            raise ValueError("controlled not using the same bit for both inputs")

        copy = {k:v for k,v in self.states.items()}
        for state in self.states.keys():
            if state[control-1] is '0': pass
            else: # control is 1, flip amplitude of target
                print(state) # FIXME
                self.states[state] = copy[bitflip(state, target)]
