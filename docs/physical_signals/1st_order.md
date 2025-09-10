---
tags:
  - physical signals
---

# First order linear circuit

## Response of a series RC circuit to a voltage step

### 1. **Differential Equation for \( u_c(t) \) (Capacitor Voltage)**

In an RC series circuit, the total voltage \( u(t) \) across the circuit is split between the resistor and the capacitor. If a step voltage \( U_0 \) is applied at \( t = 0 \), the circuit can be described by Kirchhoff's Voltage Law (KVL):

u(t) = u_R(t) + u_C(t)

where:

- \( u_R(t) = R \cdot i(t) \) is the voltage across the resistor,

- \( u_C(t) = \frac{1}{C} \int_0^t i(t) \, dt \) is the voltage across the capacitor.

For a series RC circuit, we use the relation \( i(t) = \frac{du_C(t)}{R dt} \), giving us:

\[
U_0 = R \cdot i(t) + u_C(t)
\]

Substitute \( i(t) = C \frac{du_C(t)}{dt} \) into this equation:

\[
U_0 = R C \frac{du_C(t)}{dt} + u_C(t)
\]

This is the **differential equation** governing the behavior of \( u_C(t) \):

\[
R C \frac{du_C(t)}{dt} + u_C(t) = U_0
\]

### 2. **Analysis of the Differential Equation**

This is a first-order linear differential equation. The left side represents the combination of the resistor-capacitor response to the applied step voltage \( U_0 \), while the right side is the constant voltage \( U_0 \).

- The equation suggests that the voltage across the capacitor does not instantaneously reach \( U_0 \) but instead evolves over time.
- The solution will involve an exponential function because of the first-order time derivative.

### 3. **Solution of the Differential Equation**

To solve this, we recognize that this is a standard first-order linear differential equation of the form:

\[
\tau \frac{du_C(t)}{dt} + u_C(t) = U_0
\]

where \( \tau = RC \) is called the **time constant** of the circuit. The general solution to such equations is:

\[
u_C(t) = A e^{-t/\tau} + U_0
\]

We apply the initial condition \( u_C(0) = 0 \) (assuming the capacitor starts with no charge):

\[
0 = A e^{0} + U_0 \implies A = -U_0
\]

Thus, the complete solution is:

\[
u_C(t) = U_0 (1 - e^{-t/\tau})
\]

This shows that \( u_C(t) \) increases exponentially from 0 and asymptotically approaches \( U_0 \).

### 4. **Plot and Time Constant**

The **time constant** \( \tau = RC \) determines how quickly the capacitor charges. After a time equal to \( \tau \), the capacitor reaches approximately 63% of the final voltage \( U_0 \). After \( 5\tau \), the capacitor is considered almost fully charged, as it reaches over 99% of the final voltage.

If we plot \( u_C(t) \), it will show an exponential rise, starting from 0 and approaching \( U_0 \) asymptotically.

### 5. **Current During Charging**

The current \( i(t) \) in the circuit is related to the derivative of the capacitor voltage. Using \( i(t) = C \frac{du_C(t)}{dt} \), we differentiate the capacitor voltage solution:

\[
i(t) = C \cdot \frac{d}{dt} \left( U_0 (1 - e^{-t/\tau}) \right)
\]

This simplifies to:

\[
i(t) = C \cdot U_0 \cdot \frac{1}{\tau} \cdot e^{-t/\tau} = \frac{U_0}{R} e^{-t/\tau}
\]

The current \( i(t) \) starts at a maximum value \( i(0) = \frac{U_0}{R} \) and decreases exponentially to 0 as the capacitor charges.

### 6. **Energy Balance**

The **energy** stored in the capacitor at any time \( t \) is:

\[
E_C(t) = \frac{1}{2} C u_C(t)^2 = \frac{1}{2} C \left( U_0 (1 - e^{-t/\tau}) \right)^2
\]

Initially, the capacitor has no energy, but as it charges, the energy stored increases and asymptotically approaches \( \frac{1}{2} C U_0^2 \), which is the maximum energy the capacitor can store.

The total energy provided by the voltage source is \( U_0 \cdot Q \), where \( Q = CU_0 \). Only half of this energy is stored in the capacitor. The rest is dissipated as heat in the resistor.

The **power dissipated** in the resistor is:

\[
P_R(t) = i(t)^2 R = \left( \frac{U_0}{R} e^{-t/\tau} \right)^2 R = \frac{U_0^2}{R} e^{-2t/\tau}
\]

This shows that the energy lost to heat diminishes over time as the current decreases.

## Discharge of a capacitor

The discharge of a capacitor is a fundamental concept in circuits involving resistors and capacitors (RC circuits). When a charged capacitor is connected to a resistor, the energy stored in the capacitor is gradually dissipated as heat in the resistor.

### 1. **Differential Equation for \( u_C(t) \) (Capacitor Voltage During Discharge)**

In an RC circuit, when a capacitor discharges through a resistor, we can use Kirchhoff's Voltage Law (KVL) to describe the relationship between the voltage across the resistor and the capacitor. When the capacitor discharges, there is no external power source, and the total voltage in the loop must sum to zero. The equation governing the circuit is:

\[
u_R(t) + u_C(t) = 0
\]

where:
- \( u_R(t) = R \cdot i(t) \) is the voltage across the resistor,
- \( u_C(t) = \frac{1}{C} \int_0^t i(t) \, dt \) is the voltage across the capacitor.

Now, since the current in the circuit is related to the rate of change of the charge on the capacitor, we use the relation:

\[
i(t) = -C \frac{du_C(t)}{dt}
\]

This equation indicates that the current flows in the opposite direction to the increasing charge on the capacitor (discharge). Substituting this expression into the voltage drop across the resistor:

\[
u_R(t) = R \cdot \left(-C \frac{du_C(t)}{dt}\right)
\]

Using \( u_R(t) + u_C(t) = 0 \), we now have:

\[
R C \frac{du_C(t)}{dt} + u_C(t) = 0
\]

This is the **differential equation** governing the capacitor voltage during discharge.

### 2. **Solving the Differential Equation**

The differential equation is a first-order linear equation:

\[
R C \frac{du_C(t)}{dt} + u_C(t) = 0
\]

We can rewrite this as:

\[
\frac{du_C(t)}{dt} = -\frac{u_C(t)}{RC}
\]

This is a separable differential equation, and we can solve it by separating variables:

\[
\frac{du_C(t)}{u_C(t)} = -\frac{dt}{RC}
\]

Now integrate both sides:

\[
\int \frac{1}{u_C(t)} \, du_C(t) = -\frac{1}{RC} \int dt
\]

This gives:

\[
\ln(u_C(t)) = -\frac{t}{RC} + \text{constant}
\]

We exponentiate both sides to get rid of the logarithm:

\[
u_C(t) = A e^{-t/RC}
\]

where \( A \) is a constant determined by the initial conditions. If the initial voltage across the capacitor at \( t = 0 \) is \( u_C(0) = U_0 \), we find that:

\[
u_C(0) = A e^{0} = A = U_0
\]

Thus, the solution is:

\[
u_C(t) = U_0 e^{-t/RC}
\]

This equation describes how the voltage across the capacitor decreases exponentially over time as the capacitor discharges through the resistor.

### Summary of Key Results

- The **differential equation** governing the discharge is:

\[
R C \frac{du_C(t)}{dt} + u_C(t) = 0
\]

- The **solution** of the differential equation (voltage across the capacitor during discharge) is:

\[
u_C(t) = U_0 e^{-t/\tau}
\]

  where \( \tau = RC \) is the **time constant** of the circuit.

### Interpretation

- The time constant \( \tau = RC \) controls how quickly the capacitor discharges. After a time \( t = \tau \), the voltage across the capacitor will have dropped to about 37% of its initial value \( U_0 \).
- After \( 5\tau \), the voltage is considered effectively zero (less than 1% of \( U_0 \)).

## Response of a series RL circuit to a voltage step

### 1. **Differential Equation for \( i(t) \)**

For a series RL circuit with a resistor \( R \) and an inductor \( L \), Kirchhoff's Voltage Law (KVL) gives the following relationship:

\[
u(t) = u_R(t) + u_L(t)
\]

where:
- \( u(t) = U_0 \) is the applied step voltage,
- \( u_R(t) = R \cdot i(t) \) is the voltage across the resistor,
- \( u_L(t) = L \frac{di(t)}{dt} \) is the voltage across the inductor.

Substituting these expressions into the KVL equation:

\[
U_0 = R \cdot i(t) + L \frac{di(t)}{dt}
\]

This is the **differential equation** that governs the current \( i(t) \) in the RL circuit.

### 2. **Analysis of the Differential Equation**

The differential equation is:

\[
L \frac{di(t)}{dt} + R \cdot i(t) = U_0
\]

This is a first-order linear differential equation. The two terms on the left side represent:
- \( L \frac{di(t)}{dt} \): the opposition to changes in current caused by the inductor (inductive reactance),
- \( R \cdot i(t) \): the opposition to current caused by the resistor (resistive load).

The right side is the applied step voltage \( U_0 \). This equation shows that when the voltage step is applied, the current does not immediately reach its maximum value due to the inductor's tendency to resist changes in current (known as **inductive kick**). Instead, the current increases gradually over time.

### 3. **Solving the Differential Equation**

We can solve this differential equation for \( i(t) \). First, rewrite it as:

\[
L \frac{di(t)}{dt} = U_0 - R \cdot i(t)
\]

Dividing both sides by \( L \):

\[
\frac{di(t)}{dt} = \frac{U_0}{L} - \frac{R}{L} \cdot i(t)
\]

This is a first-order linear differential equation with a standard form. To solve it, we use an integrating factor approach.

1. **Homogeneous Solution**: First, solve the homogeneous equation \( \frac{di(t)}{dt} + \frac{R}{L} i(t) = 0 \):

\[
\frac{di(t)}{i(t)} = -\frac{R}{L} dt
\]

   Integrating both sides:

\[
\ln(i(t)) = -\frac{R}{L} t + C
\]

   Exponentiating both sides:

\[
i_h(t) = A e^{-t/\tau}
\]

   where \( A \) is a constant and \( \tau = \frac{L}{R} \) is the **time constant** of the RL circuit.

2. **Particular Solution**: For the particular solution, assume \( i_p(t) = I \), a constant current. Substituting into the differential equation:

\[
0 = \frac{U_0}{L} - \frac{R}{L} \cdot I
\]

   Solving for \( I \):

\[
I = \frac{U_0}{R}
\]

   So, the particular solution is \( i_p(t) = \frac{U_0}{R} \).

3. **General Solution**: The general solution is the sum of the homogeneous and particular solutions:

\[
i(t) = A e^{-t/\tau} + \frac{U_0}{R}
\]

4. **Applying Initial Condition**: The initial condition is \( i(0) = 0 \) (since the current through an inductor cannot change instantaneously). Substituting \( t = 0 \) into the general solution:

\[
0 = A e^{0} + \frac{U_0}{R}
\]

   Solving for \( A \):

\[
A = -\frac{U_0}{R}
\]

Thus, the complete solution for the current as a function of time is:

\[
i(t) = \frac{U_0}{R} \left( 1 - e^{-t/\tau} \right)
\]

where \( \tau = \frac{L}{R} \) is the time constant of the circuit.

### 4. **Energy Balance**

Now, let's analyze the energy in the circuit.

- **Energy stored in the inductor**: The inductor stores energy in its magnetic field as current increases. The energy stored in the inductor at any time \( t \) is given by:

\[
E_L(t) = \frac{1}{2} L i(t)^2
\]

  Initially, when \( t = 0 \), the energy is zero because \( i(0) = 0 \). As time progresses and the current builds up, the inductor stores more energy.

- **Energy dissipated in the resistor**: The resistor dissipates energy as heat. The power dissipated in the resistor is:

\[
P_R(t) = R \cdot i(t)^2
\]

  The total energy dissipated by the resistor over time is the integral of the power:

\[
E_R = \int_0^\infty P_R(t) dt
\]

- **Total energy supplied by the voltage source**: The total energy provided by the voltage source is:

\[
E_{\text{total}} = U_0 \cdot Q
\]

  where \( Q = \frac{U_0}{R} \) is the charge delivered.

Initially, all the energy from the voltage source goes into building up the magnetic field of the inductor. Eventually, as the current stabilizes, all the energy is dissipated in the resistor.

### Key Takeaways

- The **differential equation** for the current is:

\[
L \frac{di(t)}{dt} + R i(t) = U_0
\]

- The **solution** is:

\[
i(t) = \frac{U_0}{R} \left( 1 - e^{-t/\tau} \right)
\]

  where \( \tau = \frac{L}{R} \) is the time constant, indicating how fast the current approaches its final steady-state value \( \frac{U_0}{R} \).

- Initially, the inductor resists changes in current, so the current grows gradually. After several time constants, the current reaches a steady-state value of \( \frac{U_0}{R} \).
