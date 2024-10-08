---
tags:
  - Physical signals
---

# Damped oscillators

A damped oscillator is a system in which an oscillating motion decreases in amplitude over time due to energy loss, typically from friction or resistance.

## Presentation

### 1. Electric Oscillator: RLC Series Circuit

An RLC series circuit consists of a resistor (R), an inductor (L), and a capacitor (C) connected in series. The behavior of this circuit can be described by the following differential equation:

\[
L \frac{d^2i(t)}{dt^2} + R \frac{di(t)}{dt} + \frac{1}{C} i(t) = 0
\]

Where:
- \(i(t)\) is the current as a function of time.
- \(R\) is the resistance (in ohms).
- \(L\) is the inductance (in henries).
- \(C\) is the capacitance (in farads).

#### Solution to the Differential Equation

The solution to this equation depends on the damping condition, which can be classified as:
- **Underdamped** (\(R < 2\sqrt{\frac{L}{C}}\)): The system oscillates with a gradually decreasing amplitude.
- **Critically damped** (\(R = 2\sqrt{\frac{L}{C}}\)): The system returns to equilibrium as quickly as possible without oscillating.
- **Overdamped** (\(R > 2\sqrt{\frac{L}{C}}\)): The system returns to equilibrium slowly without oscillating.

For an underdamped oscillator, the solution can be expressed as:

\[
i(t) = I_0 e^{-\frac{R}{2L}t} \cos(\omega_d t + \phi)
\]

Where:
- \(I_0\) is the initial amplitude.
- \(\omega_d = \sqrt{\frac{1}{LC} - \left(\frac{R}{2L}\right)^2}\) is the damped angular frequency.
- \(\phi\) is the phase constant.

### 2. Energy Analysis

The total energy \(E\) in an RLC circuit consists of:
- **Electrical energy** stored in the capacitor (\(E_C = \frac{1}{2} C V^2\)).
- **Magnetic energy** stored in the inductor (\(E_L = \frac{1}{2} L I^2\)).

As the system oscillates, energy is transferred between the capacitor and the inductor. In a damped oscillator, some energy is lost as heat in the resistor, which can be described as follows:

\[
E(t) = E_0 e^{-\frac{R}{L} t}
\]

Where \(E_0\) is the initial total energy. The energy decreases exponentially over time due to damping.

### 3. Phase Portraits

A phase portrait represents the trajectory of a system in a state space (typically with position on one axis and momentum or velocity on the other). For a damped oscillator:

- **Under-damped:** The trajectories are spirals that move inward towards the equilibrium point. The system oscillates while losing energy.

- **Critically damped:** The trajectory approaches the equilibrium point without oscillating, exhibiting a smooth return to rest.

- **Overdamped:** The trajectory approaches equilibrium slowly, and there are no oscillations.

In a phase portrait, we can illustrate the behavior of the system based on the damping condition:

#### Phase Portrait Example

- **Underdamped:** ![Underdamped Phase Portrait](https://upload.wikimedia.org/wikipedia/commons/thumb/7/76/Damped_oscillator.svg/500px-Damped_oscillator.svg.png)
- **Critically damped:** Approaches the origin directly without oscillation.
- **Overdamped:** Slower approach to the origin, no oscillation.

### Summary

A damped oscillator, such as an RLC series circuit, showcases how oscillations decrease in amplitude due to energy loss. Understanding its energy dynamics and visualizing its behavior through phase portraits provides valuable insights into the system's response to disturbances. 

## Theoretical study of the damped electric oscillator

### 1. Differential Equation for the Damped Oscillator

In an RLC series circuit, which consists of a resistor (R), an inductor (L), and a capacitor (C), we can describe the behavior of the voltage across the capacitor (\(u_C\)) as it oscillates with damping. The governing differential equation for the charge (\(q\)) on the capacitor can be written as:

\[
L \frac{d^2q(t)}{dt^2} + R \frac{dq(t)}{dt} + \frac{1}{C} q(t) = 0
\]

This equation represents a second-order linear homogeneous differential equation. The voltage across the capacitor (\(u_C\)) can be expressed in terms of charge \(q(t)\) as follows:

\[
u_C(t) = \frac{q(t)}{C}
\]

### 2. Solving the Differential Equation

To solve the differential equation, we first assume a solution of the form:

\[
q(t) = e^{\lambda t}
\]

where \(\lambda\) is a constant to be determined. Substituting this into the differential equation yields:

\[
L \lambda^2 e^{\lambda t} + R \lambda e^{\lambda t} + \frac{1}{C} e^{\lambda t} = 0
\]

Factoring out \(e^{\lambda t}\) (which is never zero), we get:

\[
L \lambda^2 + R \lambda + \frac{1}{C} = 0
\]

This is a quadratic equation in \(\lambda\). We can solve it using the quadratic formula:

\[
\lambda = \frac{-R \pm \sqrt{R^2 - 4L\cdot\frac{1}{C}}}{2L}
\]

The term \(D = R^2 - 4L\cdot\frac{1}{C}\) is called the discriminant and determines the nature of the solutions:

1. **Under-damped (\(R^2 < 4L/C\))**: Two complex conjugate roots.
2. **Critically damped (\(R^2 = 4L/C\))**: A repeated real root.
3. **Overdamped (\(R^2 > 4L/C\))**: Two distinct real roots.

#### Case 1: Under-damped Oscillator

For the under-damped case, the roots are complex:

\[
\lambda = -\frac{R}{2L} \pm j\sqrt{\frac{1}{LC} - \left(\frac{R}{2L}\right)^2}
\]

Let's denote:

- \(\alpha = -\frac{R}{2L}\)
- \(\omega_d = \sqrt{\frac{1}{LC} - \left(\frac{R}{2L}\right)^2}\)

The general solution for \(q(t)\) is:

\[
q(t) = e^{\alpha t} \left( A \cos(\omega_d t) + B \sin(\omega_d t) \right)
\]

Where \(A\) and \(B\) are constants determined by initial conditions.

Substituting back to find \(u_C(t)\):

\[
u_C(t) = \frac{q(t)}{C} = \frac{1}{C} e^{\alpha t} \left( A \cos(\omega_d t) + B \sin(\omega_d t) \right)
\]

#### Case 2: Critically Damped Oscillator

For the critically damped case, the roots are real and repeated:

\[
\lambda = -\frac{R}{2L}
\]

The general solution is:

\[
q(t) = \left( A + Bt \right) e^{-\frac{R}{2L} t}
\]

And for the voltage across the capacitor:

\[
u_C(t) = \frac{1}{C} \left( A + Bt \right) e^{-\frac{R}{2L} t}
\]

#### Case 3: Overdamped Oscillator

For the overdamped case, the roots are real and distinct:

\[
\lambda_1, \lambda_2 = \frac{-R \pm \sqrt{R^2 - 4L\cdot\frac{1}{C}}}{2L}
\]

The general solution is:

\[
q(t) = A e^{\lambda_1 t} + B e^{\lambda_2 t}
\]

And for the capacitor voltage:

\[
u_C(t) = \frac{1}{C} \left( A e^{\lambda_1 t} + B e^{\lambda_2 t} \right)
\]

## Forced sinusoidal regime

The "forced sinusoidal regime" refers to a situation in electrical circuits where an external sinusoidal voltage or current source drives the system. This is particularly relevant for RLC circuits, where resistors, inductors, and capacitors interact with the alternating current (AC) source.

### 1. Example: RLC Series Circuit

In a series RLC circuit, we have a resistor \(R\), an inductor \(L\), and a capacitor \(C\) connected in series with a sinusoidal voltage source \(V_s(t) = V_0 \cos(\omega t + \phi)\), where:
- \(V_0\) is the amplitude of the voltage.
- \(\omega\) is the angular frequency of the source.
- \(\phi\) is the phase angle.

The differential equation governing the current \(i(t)\) in the circuit can be derived from Kirchhoff’s voltage law:

\[
V_s(t) = V_R(t) + V_L(t) + V_C(t)
\]

Where:
- \(V_R(t) = Ri(t)\) is the voltage across the resistor.
- \(V_L(t) = L \frac{di(t)}{dt}\) is the voltage across the inductor.
- \(V_C(t) = \frac{1}{C} \int i(t) dt\) is the voltage across the capacitor.

### 2. Complex Representation of Sinusoidal Quantities

To analyze sinusoidal signals more conveniently, we use complex numbers and phasors. A sinusoidal function can be represented in its complex form:

\[
X(t) = X_0 e^{j(\omega t + \phi)}
\]

Where:
- \(X_0\) is the amplitude.
- \(j\) is the imaginary unit.
- \(\phi\) is the phase angle.

Using this representation, we can simplify calculations involving the addition and subtraction of sinusoidal quantities.

### 3. Complex Impedances

**Impedance** (\(Z\)) is a measure of how much a circuit resists the flow of alternating current. It is a complex quantity defined as:

\[
Z = R + jX
\]

Where:
- \(R\) is the resistance.
- \(X\) is the reactance.

#### Impedance of an Ohmic Resistor

For a pure resistor:

\[
Z_R = R
\]

#### Impedance of an Inductor

For a pure inductor, the reactance is given by:

\[
Z_L = j\omega L
\]

Where:
- \(\omega = 2\pi f\) (with \(f\) being the frequency in hertz).

#### Impedance of a Capacitor

For a pure capacitor, the reactance is:

\[
Z_C = -\frac{j}{\omega C}
\]

### 4. Electrokinetic Laws in Sinusoidal Forced Regime

In a sinusoidal regime, Ohm's law can be extended to AC circuits using complex impedances:

\[
V = IZ
\]

Where:
- \(V\) is the voltage across the component (complex).
- \(I\) is the current through the component (complex).
- \(Z\) is the impedance of the component (complex).

Using this, we can analyze the entire circuit by combining the impedances of each component. The total impedance \(Z_{total}\) for a series RLC circuit is:

\[
Z_{total} = Z_R + Z_L + Z_C = R + j\left(\omega L - \frac{1}{\omega C}\right)
\]

### 5. Example: Complex Impedance of a Real Inductor

For a real inductor, the impedance is modified to account for resistance in the inductor itself. The impedance can be expressed as:

\[
Z_L = R_L + j\omega L
\]

Where:
- \(R_L\) is the equivalent series resistance (ESR) of the inductor.
- \(\omega L\) is the inductive reactance.

This means the overall impedance of a real inductor is a combination of its resistive and reactive components, represented as:

\[
Z_L = R_L + j\omega L
\]

### Summary

In summary, the forced sinusoidal regime in an RLC series circuit involves the interaction of resistors, inductors, and capacitors under the influence of a sinusoidal voltage source. By representing sinusoidal quantities as complex numbers and using the concept of impedance, we can efficiently analyze and solve the circuit's behavior.

## Oscillator subjected to sinusoidal excitation

An "oscillator subjected to sinusoidal excitation" refers to a system, such as an RLC circuit, where an external sinusoidal voltage or current source causes oscillations.

### 1. Voltage Resonance Across the Capacitor

In an RLC series circuit driven by a sinusoidal voltage source \(V_s(t) = V_0 \cos(\omega t + \phi)\), we can analyze the voltage resonance that occurs across the capacitor.

#### Impedance in the RLC Circuit

The total impedance \(Z_{total}\) of the circuit is given by:

\[
Z_{total} = R + j\left(\omega L - \frac{1}{\omega C}\right)
\]

Where:
- \(R\) is the resistance.
- \(\omega L\) is the inductive reactance.
- \(-\frac{1}{\omega C}\) is the capacitive reactance.

At resonance, the condition is such that the inductive and capacitive reactances cancel each other out:

\[
\omega L = \frac{1}{\omega C} \quad \Rightarrow \quad \omega^2 = \frac{1}{LC} \quad \Rightarrow \quad \omega = \frac{1}{\sqrt{LC}}
\]

This frequency is known as the **resonant frequency** (\(\omega_0\)) of the circuit.

#### Voltage Across the Capacitor

The voltage across the capacitor (\(V_C\)) can be expressed using Ohm's law as:

\[
V_C = I \cdot Z_C
\]

Where \(I\) is the current through the circuit and \(Z_C = -\frac{j}{\omega C}\) is the impedance of the capacitor. The current \(I\) can be expressed in terms of the source voltage and the total impedance:

\[
I = \frac{V_s}{Z_{total}}
\]

Thus, substituting for \(V_C\):

\[
V_C = \frac{V_s}{Z_{total}} \cdot Z_C
\]

The maximum voltage across the capacitor occurs at resonance due to the fact that the impedance of the circuit is minimized, leading to maximum current:

\[
V_{C,max} = I_{max} \cdot Z_C
\]

At resonance, the impedance \(Z_{total}\) becomes purely resistive:

\[
Z_{total, res} = R
\]

### 2. Study of Resonance in Current

**Current Resonance** refers to the maximum current that flows through the circuit at the resonant frequency. As previously noted, at resonance, the impedance is minimized, allowing maximum current to flow.

#### Current in the Circuit

Using the expression for current from the voltage source, we can analyze the current at the resonant frequency:

\[
I_{max} = \frac{V_0}{R}
\]

Where:
- \(V_0\) is the amplitude of the source voltage.
- \(R\) is the resistance in the circuit.

At resonance, the total current through the circuit reaches its peak value, which can be much higher than at other frequencies due to the resonance effect. This is especially important in applications like radio transmission and signal processing, where selective amplification of specific frequencies is desired.

#### Quality Factor (Q)

The **Quality Factor** (\(Q\)) is a dimensionless parameter that describes how underdamped an oscillator is, and it is defined as:

\[
Q = \frac{\omega_0 L}{R}
\]

A higher \(Q\) indicates a sharper resonance peak, meaning that the circuit will respond more strongly at the resonant frequency compared to other frequencies.

### Summary

In summary, when an RLC circuit is subjected to sinusoidal excitation, resonance occurs at a specific frequency where the impedance of the circuit is minimized. This results in maximum voltage across the capacitor and maximum current in the circuit. Understanding resonance is crucial for designing circuits that effectively utilize sinusoidal signals.
