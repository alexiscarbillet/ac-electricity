

# Oscillators

## Quasi-Sinusoidal Oscillator

### Principle

A quasi-sinusoidal oscillator is an electronic circuit designed to generate an alternating voltage (AC) that closely resembles a sine wave. Unlike square or triangular wave oscillators, quasi-sinusoidal oscillators produce a smoother waveform, making them suitable for applications like signal generators and communication systems.

Oscillation is typically achieved through positive feedback, where a portion of the output signal is fed back to the input. This process requires amplification, often provided by an operational amplifier or a transistor.

### Conditions for Oscillation (Barkhausen Conditions)

For an oscillator to establish stable oscillations, it must meet the Barkhausen conditions:

**Gain Condition**: The product of the open-loop gain \(A\) and the feedback factor \(\beta\) must equal 1:

\[
A \cdot \beta = 1
\]
   
**Phase Condition**: The total phase shift around the loop must be an integer multiple of \(2\pi\) (or 360°):

\[
\text{Total Phase} = 2k\pi \quad (k \in \mathbb{Z})
\]

These conditions ensure that the oscillation is sustained without attenuation or excessive amplification.

### Example: Wien Bridge Oscillator
The Wien bridge oscillator is a type of quasi-sinusoidal oscillator that uses a Wien bridge circuit, which is a filter configuration. Here’s how it works:

**Circuit Configuration**: A Wien bridge consists of two resistors and two capacitors arranged in series and parallel. A voltage is applied to an operational amplifier.

**Operating Conditions**:

- For oscillation to occur, the gain of the amplifier must be set to satisfy the Barkhausen conditions. The required gain is typically:

\[
A = 3
\]

This means that the amplifier’s gain must be adjusted to 3 for the circuit to oscillate.

**Frequency of Oscillation**: The oscillation frequency is determined by the values of the resistors \(R_1\), \(R_2\) and capacitors \(C_1\), \(C_2\) used in the circuit:

\[
f = \frac{1}{2\pi R \cdot C}
\]

For a standard Wien bridge, the oscillation frequency can be expressed as:

\[
f = \frac{1}{2\pi R_1 C_1}
\]

assuming \(R_1 = R_2\) and \(C_1 = C_2\).

## Relaxation Oscillators

### Principle
Relaxation oscillators are a type of electronic oscillator that generate a non-sinusoidal waveform, typically triangular or sawtooth shapes. These oscillators work by charging and discharging a capacitor through a resistor, creating a cycle of rapid voltage changes.

Relaxation oscillators are often simpler than other types of oscillators and can be built using basic components such as resistors, capacitors, and comparators or transistors.

### Operating Sequences
The operation of a relaxation oscillator generally involves the following sequences:

**Charging Phase**:

   - A capacitor \(C\) is charged through a resistor \(R\). The voltage across the capacitor increases exponentially according to the equation:

\[
V_C(t) = V_{max} \left(1 - e^{-\frac{t}{RC}}\right)
\]

   - Here, \(V_{max}\) is the supply voltage, \(R\) is the resistance, \(C\) is the capacitance, and \(t\) is time.

**Threshold Detection**:

   - When the voltage across the capacitor reaches a predetermined threshold (typically set by a comparator or a transistor), a triggering event occurs.
   - For example, in a Schmitt trigger oscillator, this threshold can change based on hysteresis, providing a stable switching point.

**Discharging Phase**:

   - Once the threshold is reached, the capacitor rapidly discharges. This can occur through a different path or resistor, causing the voltage to drop quickly.
   - The discharge can be linear or exponential, depending on the circuit configuration.

**Resetting**:

   - After discharging, the circuit resets to the initial state, and the charging phase begins again. This cycle continues, creating a periodic output.

### Example: Astable Multivibrator
A common example of a relaxation oscillator is the astable multivibrator, which uses two transistors, resistors, and a capacitor. Here’s how it operates:

1. **Charging**: When powered, one transistor turns on, allowing current to flow through the capacitor, charging it until it reaches a certain voltage.

2. **Switching**: Once the capacitor voltage reaches the threshold of the other transistor, it turns on, causing the first transistor to turn off. The capacitor then begins to discharge through the circuit.

3. **Cycle Repeat**: The process repeats, resulting in a square wave output at the transistor's collector terminals.

