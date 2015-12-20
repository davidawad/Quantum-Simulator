#!/usr/bin/env python
# -*- coding: utf-8 -*-
import quantum

if __name__ == "__main__":

    # set up a system with 3 qubits
    psi = quantum.Psi(3)

    # apply Hadamard gate to qubit 1 (second qubit)
    psi.hadamard(1)

    # apply Hadamard gate to qubit 2 (third qubit)
    psi.hadamard(2)

    # apply π/8 gate to qubit 1
    psi.pi_over_eight(1)

    # apply controlled-not gate with qubit 1 controlling qubit 0
    psi.controlled_not(1, 0)

    # collapse and print the result (a tuple of 3 classical bits)
    print(psi.collapse())
