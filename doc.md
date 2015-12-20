## Documentation

## Quantum Gates

#### Remember, with quantum gates the amplitudes are all being changed at once. When this loop happens, we're editing the amplitudes of all of the qubits in the system at any given time.


```python
num_qubits = 3


"""
It's like a lookup table that looks like this for 3 qubits

    1 2 3
    0 0 0 - position 1
    0 0 1 - position 2
    0 1 0 - position 3
    0 1 1 - position 4
    1 0 0 - position 5
    1 0 1 - position 6
    1 1 0 - position 7
    1 1 1 - position 8  <- position 2^n
"""
# the pi over 8 gate's implementation
def pi_over_eight(qubit):
    # go through each amplitude
    for i in range(1 << self.num_qubits):
        if (i >> qubit) % 2 == 0:  # if zero
            self.amplitudes[i] *= exp(-1j * pi / 8)
        else:  # if one
            self.amplitudes[i] *= exp(1j * pi / 8)

```

What we're seeing here is that every computation on a single bit, has an effect on all 2^n bits of the system.

## Summary of the model

`n` Qubits, described by 2^n amplitudes. With 1 amplitude for each possible n bit string. You can't measure the amplitudes directly.

They start in the all 0 state initially;

So Psi().amplitudes[0] = 1, as in Psi_000 has an amplitude and probability of 1.

And a computation is just a series of gates being applied to the different Qubits in the system.

Probability of (010) = |Psi()|^2  

Where 010 is just one of the possible states you're interested in. So to find 010 you'd have to inspect Psi.aplitudes[3]. And then square that to find the probability of the state of the system being that.


And it's measured at the end in order to find the actual output of the computation.
