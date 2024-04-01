---
tags:
  - Physical signals
---

# First order linear circuit

## Response of a series RC circuit to a voltage step

We will consider the response of a series association {ohmic conductor, capacitor}
which is “suddenly” subjected to a constant voltage E.
The capacitor is initially discharged, and the switch is closed at t = 0.

### Electrical assembly

![](img/1st_order/1.png)

### Experimental results

We carry out a first experiment with R = 1.0 kΩ, C = 100 μF and E = 6.0V.

We simulate the results using a python script:

```
import numpy as np
import matplotlib.pyplot as plt

# Define the functions
def U(x):
    return np.where(x < 0, 0, 6)

def UC(x):
    return np.where(x < 0, 0, 6*(1-np.exp(-x/0.1)))

def i(x):
    return np.where(x < 0, 0, 6*np.exp(-x/0.1))

# Generate x values
t = np.linspace(-0.1, 0.6, 500)

# Generate y values for each function
y_U = U(t)
y_UC = UC(t)
y_i = i(t)

# Create subplots
fig, axes = plt.subplots(3, 1, figsize=(8, 10))

# Plot U(x)
axes[0].plot(t, y_U, label='U(t)', color='blue')
axes[0].set_title('Plot of U(t)')
axes[0].grid(True)
axes[0].legend()

# Plot UC(x)
axes[1].plot(t, y_UC, label='UC(t)', color='red')
axes[1].set_title('Plot of UC(t)')
axes[1].grid(True)
axes[1].legend()

# Plot i(x)
axes[2].plot(t, y_i, label='i(t)', color='green')
axes[2].set_title('Plot of i(t)')
axes[2].grid(True)
axes[2].legend()

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()
```

![](img/1st_order/2.png)

The voltage u<sub>c</sub> is continuous at t = 0, the capacitor charges, the voltage
increases until reaching a constant value equal to E.

The intensity of the current i is discontinuous at t = 0; starting from a maximum value
at t = 0<sup>+</sup>, the intensity decreases to zero once the capacitor is charged.

We distinguish the steady state, once the quantities do not depend
plus time (here for t > 0.5 s) and the transient regime between the initial instant
and the steady state.

### Differential equation verified by uc(t)

We are interested in the evolution of the circuit, once the switch is closed, ∀t > 0.

- Law of additivity of tensions : <span style="color: #008080">u = E = u<sub>R</sub> + u<sub>c</sub></span>

- Characteristics of dipoles : <span style="color: #008080">u<sub>R</sub> = Ri</span>

and 

![\Large\color{Teal} i=C\frac{du_{c}}{dt}](https://latex.codecogs.com/svg.latex?\Large\color{Teal}&space;i=C\frac{du_{c}}{dt})

So, ∀t > 0, 

![\Large\color{Teal} E=RC\frac{du_{c}}{dt}+u_{c}](https://latex.codecogs.com/svg.latex?\Large\color{Teal}&space; E=RC\frac{du_{c}}{dt}+u_{c})

### Analysis of the differential equation

The differential equation shows 𝜏 = RC, the time constant of the
circuit.

Once the steady state is reached : 

![\Large\color{Teal} \frac{du_{c}}{dt}=0](https://latex.codecogs.com/svg.latex?\Large\color{Teal}&space;\frac{du_{c}}{dt}=0)

we conclude that <span style="color: #008080">u<sub>c</sub> = E</span> in regime permanent.

The law of additivity of tensions leads to:

∀t > 0, 

![\Large\color{Teal} i(t)=\frac{E-u_{c}(t)}{R}](https://latex.codecogs.com/svg.latex?\Large\color{Teal}&space; i(t)=\frac{E-u_{c}(t)}{R})

In particular for t = 0<sup>+</sup>, the capacitor is discharged, i is maximum and is worth
i(0<sup>+</sup>) = E/R; once the steady state is reached, the intensity is canceled.

### Solving the differential equation

The capacitor is initially discharged u<sub>c</sub>(0<sup>—</sup>) = 0, the continuity of the voltage
across a capacitor ensures that: u<sub>c</sub>(0<sup>+</sup>) = u<sub>c</sub>(0<sup>—</sup>) = 0.

The problem to solve is therefore the following: we are looking for u<sub>c</sub> which verifies:

∀t > 0, 

![\Large\color{Teal} E=\tau\frac{du_{c}}{dt}+u_{c}](https://latex.codecogs.com/svg.latex?\Large\color{Teal}&space; E=\tau\frac{du_{c}}{dt}+u_{c})

and u<sub>c</sub>(0<sup>+</sup>) = 0

The general solution is of the form:

∀t > 0,

![\Large\color{Teal} u_{c}(t)=Ae^\frac{-dt}{\tau}+E](https://latex.codecogs.com/svg.latex?\Large\color{Teal}&space; u_{c}(t)=Ae^\frac{-dt}{\tau}+E)

The initial condition imposes: u<sub>c</sub>(0<sup>+</sup>) = 0 = E+A  => A = -E, we deduce:

∀t > 0,

![\Large\color{Teal} u_{c}(t)=E(1 - e^\frac{-dt}{\tau})](https://latex.codecogs.com/svg.latex?\Large\color{Teal}&space; u_{c}(t)=E(1 - e^\frac{-dt}{\tau}))
