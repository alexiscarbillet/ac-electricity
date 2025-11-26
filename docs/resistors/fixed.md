---
tags:
  - resistors
---

# 🔩 Fixed Resistors

**Fixed resistors** are fundamental, passive electrical components designed to provide a specific, **predetermined level of electrical resistance** (R) to the flow of current (I) in a circuit. This resistance is constant under normal operating conditions.

---

## ⚡ Fundamental Operation

A fixed resistor functions by **converting electrical energy into heat** as current flows through it. This process is governed by **Ohm's Law** and the **Joule heating effect**.

### Ohm's Law
The relationship between voltage, current, and resistance in a circuit is defined by Ohm's Law:

$$V = I \cdot R$$

* **V** (Voltage) is the potential difference across the resistor (measured in Volts).
* **I** (Current) is the electrical current flowing through the resistor (measured in Amperes).
* **R** (Resistance) is the fixed value of the resistor (measured in Ohms, $\Omega$).

### Key Applications
Fixed resistors are essential in electronic design for:
* **Current Limiting:** Protecting sensitive components by reducing the flow of current.
* **Voltage Division:** Creating a reference voltage or setting signal levels (e.g., using a **voltage divider** circuit).
* **Signal Conditioning:** Adjusting signal characteristics in amplifier stages or filters.
* **Power Dissipation:** Safely converting unwanted electrical energy into heat.

---

## 🏗️ Common Types of Fixed Resistors

The physical construction and material composition determine a fixed resistor's characteristics, stability, and precision.

| Type | Construction | Key Characteristics | Typical Tolerance |
| :--- | :--- | :--- | :--- |
| **Carbon Composition (CCR)** | Solid slug of carbon powder and binder. | Excellent pulse handling, high noise, low precision. | $\pm 5\%$ to $\pm 20\%$ |
| **Carbon Film (CFR)** | Thin carbon film deposited on a ceramic core, cut with a helix. | Good general-purpose stability, cost-effective. | $\pm 2\%$ to $\pm 5\%$ |
| **Metal Film (MFR)** | Thin metal film (e.g., nickel-chromium) deposited on a ceramic core, cut with a helix. | High precision, low noise, excellent stability. | $\pm 0.1\%$ to $\pm 1\%$ |
| **Wirewound** | Resistive wire (e.g., Nichrome) wound around a core. | Highest power handling, very low resistance values. | $\pm 0.005\%$ to $\pm 1\%$ |

---

## 📜 Historical Development

The evolution of fixed resistors closely tracks the history of electronics, driven by the need for better stability and precision.

* **19th Century Foundations:** The concept of resistance was formalized by **Georg Simon Ohm**. Early resistors used simple lengths of metal wire or carbon material.
* **Mid-20th Century Dominance:** **Carbon Composition Resistors** became the standard for consumer electronics (radios, early TVs) due to their **low cost** and **reliability**.
* **Late 20th Century Transition:** **Film Resistors** (Carbon and Metal) replaced CCRs in most applications, offering superior **precision** and **temperature stability**.
* **Modern Era (SMT):** The advent of **Surface Mount Technology (SMT)** made tiny, rectangular **Surface Mount Devices (SMD) resistors** the standard for virtually all modern, compact electronic devices (smartphones, computers).

---

## 🌈 Resistor Color Code

In through-hole resistors, the resistance value and tolerance are indicated by a series of colored bands printed on the body.

### 4-Band Color Code Example

The most common code uses four bands: **Digit 1 | Digit 2 | Multiplier | Tolerance**.

| Color | Digit Value (1st & 2nd Band) | Multiplier (3rd Band) | Tolerance (4th Band) |
| :--- | :--- | :--- | :--- |
| **Black** | 0 | $\times 1$ | — |
| **Brown** | 1 | $\times 10$ | $\pm 1\%$ |
| **Red** | 2 | $\times 100$ | $\pm 2\%$ |
| **Orange** | 3 | $\times 1\text{k}$ | — |
| **Yellow** | 4 | $\times 10\text{k}$ | — |
| **Green** | 5 | $\times 100\text{k}$ | $\pm 0.5\%$ |
| **Blue** | 6 | $\times 1\text{M}$ | $\pm 0.25\%$ |
| **Violet** | 7 | $\times 10\text{M}$ | $\pm 0.1\%$ |
| **Gray** | 8 | $\times 100\text{M}$ | $\pm 0.05\%$ |
| **White** | 9 | $\times 1\text{G}$ | — |
| **Gold** | — | $\times 0.1$ | $\pm 5\%$ |
| **Silver** | — | $\times 0.01$ | $\pm 10\%$ |

**Example:** A resistor with **Red (2)**, **Green (5)**, **Brown ($\times 10$)**, **Gold ($\pm 5\%$)** has a value of:

$$25 \times 10 = 250\ \Omega \pm 5\%$$
