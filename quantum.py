#!/usr/bin/env python
# encoding: utf-8

from cmath import exp, pi, sqrt
from random import random


class Psi:
    def __init__(self, num_qubits):
        """
        set up a quantum system with the given number of qubits
        initialized to the "zero" qubit.
        """
        self.num_qubits = num_qubits
        # In this classical simulation,we use 2^n Qubit complex numbers
        # this array of size 2^n will replicate the 2^n states Qubits can have
        self.amplitudes = [0] * (1 << num_qubits)  # use bitshift to realize 2^n
        self.amplitudes[0] = 1  # so that sum of squared prob. is 1, starting in 000 state

    def collapse(self):
        """
        collapse the system (i.e. measure it) and return a tuple
        of the bits.
        """
        weights = [abs(amp) ** 2 for amp in self.amplitudes]
        choice = random() * sum(weights)
        for i, w in enumerate(weights):
            choice -= w
            if choice < 0:
                self.amplitudes = [0] * (1 << self.num_qubits)
                self.amplitudes[i] = 1
                return tuple((i >> bit) % 2 for bit in range(self.num_qubits))

    def amplitude(self, state):
        """
        takes in a possible state of the system such as '010' and returns
        the amplitude of that possible state.
        """
        if len(state) > (1 << self.num_qubits):
            raise ValueError("State doesn't exist")
        # grab binary representation of state, access that array position
        return self.amplitudes[int(state, 2)]

    def probability(self, state):
        """
        simply returns the square of the absolute value
        of the amplitude for a given state
        """
        return abs(self.amplitude(state))**2

    def pi_over_eight(self, qubit):
        """
        applies a π/8 gate to the given qubit
        """
        if qubit > self.num_qubits:
            raise ValueError("Qubit %s not in system" % qubit)
        # go through each amplitude
        for i in range(1 << self.num_qubits):
            # find out whether that amplitude corresponds to the qubit being
            # zero or one
            # for example psi_010 would be i bit shifted for the 2nd bit
            # in this case, bit two has a 1, so let's multiply it's amplitude
            if (i >> qubit) % 2 == 0:  # if zero
                self.amplitudes[i] *= exp(-1j * pi / 8)
            else:  # if one
                self.amplitudes[i] *= exp(1j * pi / 8)

    def hadamard(self, qubit):
        """
        applies a Hadamard gate to the given qubit.
        """
        if qubit > self.num_qubits:
            raise ValueError("Qubit %s not in system" % qubit)
        # make a copy of amplitudes as they update simultaneously
        old_amplitudes = self.amplitudes[:]
        # go through each amplitude
        for i in range(1 << self.num_qubits):
            # find out whether that amplitude corresponds to the qubit being
            if (i >> qubit) % 2 == 0:  # if zero
                self.amplitudes[i] = (old_amplitudes[i] - old_amplitudes[i + (1 << qubit)]) / sqrt(2)
            else:  # if one
                self.amplitudes[i] = (old_amplitudes[i - (1 << qubit)] - old_amplitudes[i]) / sqrt(2)

    def controlled_not(self, qubit1, qubit2):
        """
        applies a controlled-not gate using the first given qubit as the
        control of the permutation of the second.
        """
        # the two quibits have to valid and different
        if qubit1 > self.num_qubits or qubit2 > self.num_qubits or qubit1 == qubit2:
            raise ValueError("Qubit %s not in system" % qubit)
        # make a copy of amplitudes as they update simultaneously
        old_amplitudes = self.amplitudes[:]
        # go through each amplitude
        for i in range(1 << self.num_qubits):
            # permutate qubit2 based on value of qubit1
            self.amplitudes[i ^ (((i >> qubit1) % 2) << qubit2)] = old_amplitudes[i]
