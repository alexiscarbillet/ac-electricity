---
tags:
  - Electronic
---

# Linear system

## Linear Time-Invariant System

A **Linear Time-Invariant System (LTI system)** is a fundamental concept in electronics and control theory, describing systems whose behavior can be predicted using linear equations and whose properties do not change over time.

### 1. Definitions

#### **Operator**
In the context of LTI systems, an operator refers to a mathematical entity that defines how a system transforms an input signal to produce an output. The most common operator in electronics is the **differential operator** \( \mathcal{D} \), which operates on a function to describe its derivatives:
\[
\mathcal{D}x(t) = \frac{dx(t)}{dt}
\]
This operator is critical in systems governed by differential equations, such as electrical circuits or mechanical systems.

#### **Linearity**
A system is **linear** if it satisfies two key properties:
1. **Superposition (Additivity)**: If an input signal \( x_1(t) \) produces an output \( y_1(t) \), and an input \( x_2(t) \) produces \( y_2(t) \), then for any two scalars \( \alpha \) and \( \beta \), the system’s response to \( \alpha x_1(t) + \beta x_2(t) \) is:
\[
\alpha y_1(t) + \beta y_2(t)
\]
2. **Homogeneity (Scaling)**: If an input \( x(t) \) produces an output \( y(t) \), then for any scalar \( k \), the response to \( kx(t) \) is \( ky(t) \).

Thus, the system’s response to a combination of inputs is simply the combination of the individual responses.

#### **Time-Invariance**
A system is **time-invariant** if its behavior does not change over time. This means that if a system responds to an input \( x(t) \) with output \( y(t) \), then if the input is delayed by some time \( t_0 \), the output will also be delayed by the same amount:
\[
x(t - t_0) \rightarrow y(t - t_0)
\]
This property ensures that the system’s characteristics remain the same regardless of when the input is applied.

### 2. **Systems Governed by Differential Equations**

Many LTI systems, especially in electronics, are governed by **linear differential equations**. These equations describe the relationship between the input and output of the system, often involving derivatives of the input and/or output signals.

A general form of a linear differential equation for an LTI system is:
\[
a_n \frac{d^n y(t)}{dt^n} + a_{n-1} \frac{d^{n-1} y(t)}{dt^{n-1}} + \dots + a_1 \frac{dy(t)}{dt} + a_0 y(t) = b_m \frac{d^m x(t)}{dt^m} + b_{m-1} \frac{d^{m-1} x(t)}{dt^{m-1}} + \dots + b_1 \frac{dx(t)}{dt} + b_0 x(t)
\]
Here:
- \( y(t) \) is the output signal (response of the system),
- \( x(t) \) is the input signal,
- \( a_0, a_1, \dots, a_n \) are constants defining the system's response,
- \( b_0, b_1, \dots, b_m \) are constants related to the input signal.

This equation reflects the **causal relationship** between the input and output of the system. For example, in an electrical circuit consisting of resistors, capacitors, and inductors, the system might be described by a second-order differential equation, as in the case of an RLC circuit:
\[
L \frac{d^2 i(t)}{dt^2} + R \frac{di(t)}{dt} + \frac{i(t)}{C} = v(t)
\]
Where:
- \( L \) is the inductance,
- \( R \) is the resistance,
- \( C \) is the capacitance,
- \( i(t) \) is the current, and
- \( v(t) \) is the input voltage.

This is a second-order linear differential equation, and its solution will describe how the current in the circuit evolves over time in response to the applied voltage.

### Conclusion

In summary:
- **Operator** defines how inputs are transformed into outputs, often via differential equations.
- **Linearity** ensures that the system’s response to combined inputs is the sum of the individual responses.
- **Time-invariance** guarantees that the system's behavior is consistent over time.

## Frequency response and transfer function

The **frequency response** and **transfer function** are key concepts in the analysis of Linear Time-Invariant (LTI) systems, providing insight into how these systems respond to sinusoidal inputs and how their behavior can be characterized mathematically.

### 1. **Sinusoidal Steady-State Response (Régime sinusoïdal forcé)**

When an LTI system is subjected to a sinusoidal input in steady state (also called the **forced sinusoidal regime**), its output is also sinusoidal, but it may have a different amplitude and phase. This property is crucial because sinusoidal signals are fundamental in many practical applications, such as AC power systems, communications, and signal processing.

For an LTI system with input:
\[
x(t) = X_0 \cos(\omega t + \phi)
\]
where:
- \( X_0 \) is the amplitude,
- \( \omega \) is the angular frequency,
- \( \phi \) is the phase,

the system's output will have the form:
\[
y(t) = Y_0 \cos(\omega t + \phi + \theta)
\]
where:
- \( Y_0 \) is the output amplitude,
- \( \theta \) is the phase shift introduced by the system.

The input and output have the same frequency, \( \omega \), but the output may be scaled (in amplitude) and delayed (in phase) depending on the system’s properties.

This behavior can be analyzed using **complex notation**, which simplifies the math. The input can be written as:
\[
x(t) = \Re\{ X e^{j\omega t} \}
\]
where \( X = X_0 e^{j\phi} \) is the complex amplitude. The output will similarly be:
\[
y(t) = \Re\{ Y e^{j\omega t} \}
\]
where \( Y = Y_0 e^{j(\phi + \theta)} \).

### 2. **Transfer Function (Fonction de transfert)**

The **transfer function**, denoted \( H(s) \), is a fundamental concept in the analysis of LTI systems. It is defined as the ratio of the Laplace transform of the output to the Laplace transform of the input, assuming zero initial conditions. In the **frequency domain**, the transfer function relates the system's input and output as:
\[
H(s) = \frac{Y(s)}{X(s)}
\]
where:
- \( Y(s) \) is the Laplace transform of the output \( y(t) \),
- \( X(s) \) is the Laplace transform of the input \( x(t) \),
- \( s = \sigma + j\omega \) is the complex frequency variable in the Laplace domain.

For sinusoidal steady-state analysis, we are particularly interested in the **frequency response** of the system, which is obtained by evaluating the transfer function along the imaginary axis of the \( s \)-plane, i.e., \( s = j\omega \). The frequency response is then given by:
\[
H(j\omega) = \frac{Y(j\omega)}{X(j\omega)}
\]
This complex function describes how the system affects the amplitude and phase of sinusoidal inputs at different frequencies.

- The **magnitude** \( |H(j\omega)| \) tells us how the system amplifies or attenuates signals at frequency \( \omega \).
- The **phase** \( \arg(H(j\omega)) \) tells us how the system shifts the phase of signals at frequency \( \omega \).

For example, for a simple RC circuit with transfer function:
\[
H(j\omega) = \frac{1}{1 + j\omega RC}
\]
- At low frequencies (\( \omega \ll \frac{1}{RC} \)), \( |H(j\omega)| \approx 1 \), so the system passes low-frequency signals with little attenuation.
- At high frequencies (\( \omega \gg \frac{1}{RC} \)), \( |H(j\omega)| \approx 0 \), so the system attenuates high-frequency signals (acting as a low-pass filter).

### 3. **Equivalence: Differential Equation and Transfer Function**

There is a direct equivalence between the **differential equation** governing an LTI system and its **transfer function** in the frequency (Laplace) domain.

Consider an LTI system described by a linear differential equation:
\[
a_n \frac{d^n y(t)}{dt^n} + a_{n-1} \frac{d^{n-1} y(t)}{dt^{n-1}} + \dots + a_1 \frac{dy(t)}{dt} + a_0 y(t) = b_m \frac{d^m x(t)}{dt^m} + b_{m-1} \frac{d^{m-1} x(t)}{dt^{m-1}} + \dots + b_0 x(t)
\]
Taking the Laplace transform of both sides (with zero initial conditions), we can transform the time-domain differential equation into an algebraic equation in the Laplace domain:
\[
a_n s^n Y(s) + a_{n-1} s^{n-1} Y(s) + \dots + a_1 s Y(s) + a_0 Y(s) = b_m s^m X(s) + b_{m-1} s^{m-1} X(s) + \dots + b_0 X(s)
\]
This simplifies to:
\[
\left( a_n s^n + a_{n-1} s^{n-1} + \dots + a_1 s + a_0 \right) Y(s) = \left( b_m s^m + b_{m-1} s^{m-1} + \dots + b_0 \right) X(s)
\]
Thus, the transfer function is:
\[
H(s) = \frac{Y(s)}{X(s)} = \frac{b_m s^m + b_{m-1} s^{m-1} + \dots + b_0}{a_n s^n + a_{n-1} s^{n-1} + \dots + a_0}
\]
This shows that the transfer function can be directly derived from the differential equation by expressing it in terms of \( s \), with coefficients of the input and output's derivatives becoming the numerator and denominator polynomials.

### Conclusion

The **frequency response** describes how an LTI system responds to different input frequencies, while the **transfer function** provides a powerful tool for analyzing the system in the frequency domain. There is a clear equivalence between the time-domain description of a system via differential equations and its frequency-domain representation through the transfer function.

## Stability

**Stability** is a fundamental property in the analysis and design of electrical circuits and control systems, especially in systems governed by differential equations and transfer functions. A system is considered stable if its response to any bounded input remains bounded over time, meaning it does not oscillate or diverge uncontrollably.

### 1. **Stability Criterion**

The stability of an LTI system can be analyzed using its **transfer function** \( H(s) \) or its differential equation. Several criteria are used to determine stability, but all are based on the behavior of the system’s poles, which are the values of \( s \) that cause the denominator of the transfer function to be zero.

#### **Poles and Stability**
The general form of the transfer function is:
\[
H(s) = \frac{N(s)}{D(s)}
\]
Where:
- \( N(s) \) is the numerator polynomial, 
- \( D(s) \) is the denominator polynomial.

The poles of the system are the roots of \( D(s) = 0 \). The stability of the system depends on the location of these poles in the **complex plane**:
- **Stable system**: All poles have negative real parts (i.e., they are in the **left half-plane** of the complex plane). In this case, the system’s natural response will decay over time.
- **Unstable system**: If any pole has a positive real part (i.e., it is in the **right half-plane**), the system is unstable, and its response will grow without bound.
- **Marginally stable system**: Poles on the **imaginary axis** (i.e., with zero real part) indicate a marginally stable system, where the system may oscillate indefinitely without growing or decaying.

#### **Routh-Hurwitz Criterion**
A popular method for checking the stability of a system without solving for the poles explicitly is the **Routh-Hurwitz criterion**. It applies to the characteristic equation (the denominator of the transfer function) and provides a systematic way to determine whether any poles have positive real parts.

Given the characteristic equation:
\[
a_n s^n + a_{n-1} s^{n-1} + \dots + a_1 s + a_0 = 0
\]
The Routh-Hurwitz criterion creates a **Routh array** from the coefficients \( a_n \), \( a_{n-1} \), etc., and examines the signs of the first column in the array. If all entries in this column are positive, the system is stable. Any sign changes indicate the presence of poles in the right half-plane, meaning the system is unstable.

#### **Nyquist Criterion**
Another powerful tool for determining stability, particularly in frequency-domain analysis, is the **Nyquist criterion**. This method is based on plotting the **Nyquist diagram**, which is a plot of the transfer function \( H(j\omega) \) in the complex plane as \( \omega \) varies from \( -\infty \) to \( \infty \). By analyzing how the plot encircles the critical point \(-1 + j0\), one can determine the stability of a closed-loop system.

### 2. **Application: Negative Resistance Oscillator**

An interesting application of the stability criterion is the design and analysis of an **oscillator with negative resistance**. Oscillators are circuits that generate periodic signals without any external periodic input. They achieve this by operating at the edge of stability, where the system has poles on the imaginary axis, indicating **sustained oscillations**.

#### **Principle of Negative Resistance**
An **oscillator** relies on positive feedback and requires a circuit component that compensates for energy losses, often modeled as a negative resistance. In such circuits, energy is provided by active components (e.g., transistors or tunnel diodes) that introduce negative resistance, which cancels out the natural losses of the circuit, allowing it to oscillate.

For instance, consider a simple LC circuit, which has an inductance \( L \) and capacitance \( C \). In a stable system, this circuit would oscillate briefly and then decay due to losses (resistance). If a negative resistance \( -R \) is introduced, the total resistance \( R_{\text{total}} = R - R_{\text{neg}} \) can be reduced to zero, preventing the oscillations from decaying.

#### **Negative Resistance Oscillator Design**
A typical **negative resistance oscillator** is designed using a device like a **tunnel diode**, which exhibits a region of negative differential resistance in its current-voltage characteristics. In this region, an increase in voltage causes a decrease in current, effectively providing the negative resistance required for oscillation.

The **transfer function** of such an oscillator can be analyzed as follows:
\[
H(s) = \frac{1}{LC s^2 + \left(\frac{R_{\text{total}}}{L}\right) s + 1}
\]
If \( R_{\text{total}} = 0 \), the characteristic equation becomes:
\[
s^2 + \frac{1}{LC} = 0
\]
The poles of this system are purely imaginary:
\[
s = \pm j \sqrt{\frac{1}{LC}}
\]
This indicates that the system is **marginally stable** and will oscillate indefinitely with a natural frequency of:
\[
\omega_0 = \frac{1}{\sqrt{LC}}
\]
This is the resonant frequency of the LC circuit, and the oscillator will produce a sinusoidal signal at this frequency.

If \( R_{\text{total}} \) becomes slightly negative (i.e., the negative resistance dominates), the system becomes unstable, and the oscillations grow until non-linear effects limit the amplitude, resulting in a stable oscillating waveform at \( \omega_0 \).

#### **Stability Considerations in Oscillator Design**
The key challenge in designing such oscillators is to maintain the system on the boundary of stability. If the negative resistance is too large, the system becomes unstable, leading to uncontrolled oscillations. If it is too small, the oscillations decay, and the circuit stops functioning as an oscillator. Proper tuning of the feedback network and the negative resistance is crucial to ensure sustained, stable oscillations.

### Conclusion

Stability analysis is crucial in determining whether a system will behave predictably over time. The **stability criterion** can be applied using various methods, such as pole location, the Routh-Hurwitz criterion, or Nyquist plots. The **negative resistance oscillator** is a practical example where stability principles are used to create controlled oscillations. In such circuits, negative resistance compensates for natural losses, leading to sustained oscillations at a defined frequency.