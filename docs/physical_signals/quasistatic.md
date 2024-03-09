---
tags:
  - Physical signals
---

# Electrical circuits in the quasistatic approximation

## Quasistatic approximation

In the quasistatic approximation, any variation in the source is immediately reflected to all
the points of the circuit.

<u>Validity scope</u>:

The quasistatic approximation consists of neglecting the
duration of propagation of the signal with respect to the characteristic evolution time
physical quantities.

Thus, in electrokinetics, we consider
that the intensity of the current is the same at every point of a wire, neglecting in the
propagation time.

## Electrical quantities

### Electric current

The electric current is associated with the macroscopic movement of the carriers of
charge, electrons in the case of a metal.

The intensity of the current, denoted i, is a charge rate equal to the electrical charge
which passes through a section of the wire per unit of time:

![\Large\color{Teal} i=\frac{dq}{dt}](https://latex.codecogs.com/svg.latex?\Large\color{Teal}&space;i=\frac{dq}{dt})

with i the intensity in amperes (A), dq the elementary charge in coulombs (C) and dt
the elementary duration in second (s).

    Note: in the case of a steady state, we will note I = Q/T.

<u>Measurement of electric current intensity:</u>

The intensity of the electric current is measured using an ammeter placed in
series on the wire.

![](img/quasistatic/1.png)

- In signal electronics, current intensities are of the order of tens of mA.

- For household appliances (bulb, kettle, etc.), intensities vary from 1 to 10 A.

- In electrical engineering, intensities can reach much higher values high (1000 A for a TGV engine).

### Electrical voltage

Each point of the circuit is characterized by an electrical state: the electric potential.

The electric voltage, denoted u<sub>AB</sub>, is equal to the electric potential difference between A and B.

<span style="color: #008080">u<sub>AB</sub> = V<sub>A</sub> - V<sub>B</sub></span>

with V<sub>A</sub> and V<sub>B</sub> the potentials in A and B. All these quantities are expressed in volts (V).

![](img/quasistatic/2.png)

Note: u<sub>BA</sub> =  V<sub>B</sub> - V<sub>A</sub> = - (V<sub>A</sub> -  V<sub>B</sub>) = - u<sub>AB</sub>

<u>Measurement of electrical voltage</u>:

The electrical voltage is measured using a voltmeter placed in parallel to the
terminals of the dipole.

![](img/quasistatic/3.png)

### Kirchhoff's laws

#### Kirchhoff's Current Law

A node designates an electrical branch, the meeting of at least three wires.

In an electrical node, the sum of the intensities of the currents entering is equal to the sum of the intensities of the outgoing currents.

![](img/quasistatic/4.png)

<u>Proof</u>:

d<sub>q1</sub> + d<sub>q2</sub> = d<sub>q3</sub> + d<sub>q4</sub> + d<sub>q5</sub>

Now divide by dt and you obtain:

<span style="color: #008080">i<sub>1</sub> + i<sub>2</sub> = i<sub>3</sub> + i<sub>4</sub> + i<sub>5</sub></span>

The law of nodes reflects the conservation of the electric charge of an isolated system.

#### Kirchhoff's Voltage Law

A mesh is a loop without branches through which a current flows.

The sum of tensions along an oriented mesh is zero.

<span style="color: #008080">u<sub>AB</sub> + u<sub>BC</sub> + u<sub>CD</sub> + u<sub>DA</sub> = 0</span>

![](img/quasistatic/5.png)

<u>Proof</u>:

u<sub>AB</sub> + u<sub>BC</sub> + u<sub>CD</sub> + u<sub>DA</sub> = (V<sub>A</sub> - V<sub>B</sub>) + (V<sub>B</sub> - V<sub>C</sub>) + (V<sub>C</sub> - V<sub>D</sub>) + (V<sub>D</sub> - V<sub>A</sub>) = 0

By using this, you obtain:

<span style="color: #008080">u<sub>AC</sub> = u<sub>AB</sub> + u<sub>BC</sub></span>

![](img/quasistatic/6.png)

