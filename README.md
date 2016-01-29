# Quantum-Simulator
Quantum Computing Simulation Software for experimentation with quantum logic gates.

I noticed there wasn't a lot of work happening in the field of simulating quantum computation on classical machines.
This project aims to simply simulate quantum gates so you might determine the usefulness of using a quantum computer or quantum algorithms.


## Usage
```python
import quantum

# set up a system with 3 Qubits, 1 indexed for simplicity
psi = quantum.System(3)

# apply Hadamard gate to Qubit 1
psi.hadamard(1)

# apply Hadamard gate to Qubit 2
psi.hadamard(2)

# apply π/8 gate to Qubit 1
psi.pi_over_eight(1)

# apply controlled-not gate with Qubit 1 controlling Qubit 2
psi.controlled_not(1, 2)

# collapse and print the result (a tuple of 3 classical bits)
print(psi.collapse())

001
```


## Requirements
- Python 2.7+



## Available Gates
It currently realizes a π/8 gate, a controlled-not gate and the Hadamard gate. With more to come soon hopefully.



#### NOTE: this is a classical simulation of a quantum system and so n Qubits requires 2^n complex amplitudes with each operation affecting every one of those amplitudes. 


## Contributors and Accreditation

Based on the concepts portrayed by Michael Nielsen's fantastic talk at the [2009 singularity summit](https://www.youtube.com/watch?v=vykoKInjuPY).

Inspired by code samples from [jatuber](https://github.com/jtauber/quantumpy) and [limitedmage](https://gist.github.com/limitedmage/945473)


## Resources:
[The Qubit Wiki Page](https://en.wikipedia.org/wiki/Qubit)

[Quantum Gates](https://en.wikipedia.org/wiki/Quantum_gate)

[The basics of Ion Trap Quantum Computing](https://www2.physics.ox.ac.uk/research/ion-trap-quantum-computing-group/intro-to-ion-trap-qc)
