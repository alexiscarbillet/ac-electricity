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

<u>Note</u>: in the case of a steady state, we will note I = Q/T.

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

### Orientation conventions

Two conventions exist for studying a dipole:

- receiver agreement

![](img/quasistatic/8.png)

- generator convention

![](img/quasistatic/9.png)

A dipole is entirely specified by its characteristic, i.e. the relation
<span style="color: #008080">u<sub>AB</sub> = u<sub>AB</sub>(i)</span> for a given convention.

### Electrical power received

![](img/quasistatic/7.png)

A dipole in receiver convention traversed by a current of intensity i and subjected
at a voltage u receives an electric power:

<span style="color: #008080">P = u x i</span>

Power is expressed in watts (W).

## Electric dipoles

In electricity, a dipole is an element which has two terminals, the current between
through one terminal and exits through the other.

### The ohmic conductor

An ohmic conductor is a dipole for which the applied voltage is proportional
to the intensity of the current passing through it.

![](img/quasistatic/10.png)

<span style="color: #008080">u<sub>AB</sub> = R x i</span>

R is the resistance of the ohmic conductor and is expressed in ohm (Ω).

Power received: <span style="color: #008080">P = R x i<sup>2</sup></span>

Indeed, with <span style="color: #008080">u = R x i</span> in receiver convention, <span style="color: #008080">P = u x i = R x i x i = R x i<sup>2</sup></span>. This power, always positive, is dissipated by the Joule effect.

<u>Note</u>: an electric wire can be compared to an ohmic resistance conductor
zero, consequently the voltage across a wire is zero.

### Ideal voltage generator

The ideal voltage generator maintains a constant voltage at its terminals and
this regardless of the intensity delivered.

![](img/quasistatic/11.png)

<u>Power received</u>: we must return to a receiver convention
<span style="color: #008080">P = u<sub>BA</sub> x i = - u<sub>AB</sub> x i = - U<sub>0</sub> x i </span> < 0 for i > 0

The ideal voltage generator provides power <span style="color: #008080">P<sub>p</sub> = U<sub>0</sub> x i </span>.

### Real voltage generator, Thévenin model

The Thévenin model corresponds to the series association of an ideal generator of
voltage and an ohmic conductor of resistance r, called internal resistance.

![](img/quasistatic/12.png)

<span style="color: #008080">u<sub>AB</sub> = U<sub>0</sub> - r x i </span>

### The capacitor

The capacitor is made up of two metal plates separated by an insulator
electric.

![](img/quasistatic/13.png)

With i the intensity, q the charge of the capacitor in coulomb (C), u<sub>c</sub> the voltage at
terminals of the capacitor, and C the capacitance of the capacitor in farad (F), the laws
electrical are written:

<span style="color: #008080">q = C x u<sub>c</sub></span> 

and
 
![\Large\color{Teal} i=\frac{dq}{dt}](https://latex.codecogs.com/svg.latex?\Large\color{Teal}&space;i=\frac{dq}{dt})

so

![\Large\color{Teal} i=C\frac{du_{c}}{dt}](https://latex.codecogs.com/svg.latex?\Large\color{Teal}&space;i=C\frac{du_{c}}{dt})

The capacitance C of a capacitor represents its ability to store charges
for a given voltage across its terminals.
The farad is a “huge” unit. Commonly used abilities are often
closer to F, 1 mF already being a significant capacity.

<u>Electrostatic energy stored in a capacitor</u>:

![\Large\color{Teal} E_{c}=\frac{1}{2}Cu_{c}^{2}](https://latex.codecogs.com/svg.latex?\Large\color{Teal}&space;E_{c}=\frac{1}{2}Cu_{c}^{2})

<u>Consequence</u>: energy cannot appear or disappear spontaneously,
The voltage across a capacitor is a continuous quantity.

### The electrical coil

A coil is created using a coiled electrical wire. This winding gives
the coil's magnetic properties.

![](img/quasistatic/14.png)

In receiver convention, the voltage across a coil and the intensity of the
current circulating in the coil are connected by the following law:

![\Large\color{Teal} u_{L}=L\frac{di}{dt}](https://latex.codecogs.com/svg.latex?\Large\color{Teal}&space;u_{L}=L\frac{di}{dt})

L, the inductance of the coil, is expressed in henry (H). It represents the ability of the coil to resist current variations.

<u>Real coil</u>: the long winding length gives the coil character
resistive, a real coil is therefore represented by the series association of a
inductance L and a resistance r:

![](img/quasistatic/15.png)

![\Large\color{Teal} u=L\frac{di}{dt}+ri](https://latex.codecogs.com/svg.latex?\Large\color{Teal}&space;u_{L}=L\frac{di}{dt}+ri)

<u>Magnetic energy stored in a coil</u>:

![\Large\color{Teal} E_{L}=\frac{1}{2}Li^{2}](https://latex.codecogs.com/svg.latex?\Large\color{Teal}&space;E_{L}=\frac{1}{2}Li^{2})

<u>Consequence</u>: energy cannot appear or disappear spontaneously,
The current flowing through a coil is a continuous quantity.