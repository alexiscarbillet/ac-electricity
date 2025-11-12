---
tags:
  - inductors
---

# Coupled Inductors

## Overview

A **coupled inductor** is a pair (or more) of inductors that share a common magnetic field, enabling **energy transfer** via **mutual inductance**. They can behave like transformers or be configured to support filtering, isolation, impedance matching, and power conversion while sharing a magnetic core or magnetic path.

---

## History

Coupled inductors evolved alongside major revolutions in power and communication systems:

- **1830s – Foundations:**  
  Michael Faraday and Joseph Henry independently discovered electromagnetic induction, laying the theoretical groundwork for coupled coils.

- **1880s–1890s – The Transformer Era:**  
  With the rise of AC power, engineers such as *William Stanley* and *Nikola Tesla* developed practical transformers using magnetically coupled coils, enabling long-distance power delivery.

- **1900–1930 – Telecommunications Boom:**  
  Coupled inductors were essential in:
  - Telephone hybrid coils
  - Telegraph isolation circuits
  - Early RF transmitters and receivers
  - Tuning and resonance networks

- **1940–1970 – RF and Radar Systems:**  
  Radar, military radio, and early television drove innovation in high-frequency coupled coils for filters, baluns, and impedance transformation.

- **1980–2000 – Power Electronics Expansion:**  
  Adoption in switch-mode power supplies (SMPS), flyback and forward converters, and motor drivers.

- **2000–Present – Integration & Miniaturization:**  
  Coupled inductors are now found in:
  - On-chip DC-DC converters
  - Wireless charging pads
  - Automotive power systems
  - IoT energy modules
  - 5G RF front-end filtering

- **Emerging Research Areas:**  
  - Resonant wireless power transfer
  - Magnetic isolation for high-voltage safety
  - Nanocrystalline and ferrite core optimization
  - Planar coupled inductors in PCBs

---

## Physical Principle

### Mutual Inductance

When two inductors share a magnetic field:

\[
v_2 = M \cdot \frac{di_1}{dt}
\]

Where:

- \( M \) = Mutual inductance (H)
- \( v_2 \) = Induced voltage on the secondary
- \( di_1/dt \) = Rate of current change in the primary coil

### Coupling Coefficient

\[
k = \frac{M}{\sqrt{L_1 L_2}}, \quad 0 \le k \le 1
\]

| k Value | Interpretation |
|--------|----------------|
| **1.0** | Perfect coupling (no leakage) |
| **0.6–0.99** | Typical for transformers |
| **0.2–0.6** | Loosely coupled resonant coils (e.g., wireless charging) |
| **< 0.2** | Weak coupling (minimal energy transfer) |

### Ideal transformer relationship:

\[
\frac{V_s}{V_p} = \frac{N_s}{N_p}
\]

---

## How Coupled Inductors Work

### 1. Energy Transfer
- A changing current in the primary coil creates a magnetic field.
- This changing field induces voltage in the secondary coil **without electrical contact**.

### 2. Voltage Transformation
- Controlled by the **turns ratio** between coils.
- Enables step-up or step-down behavior (like transformers).

### 3. Isolation
- There is no direct conductive connection → useful for safety isolation and noise rejection.

### 4. Filtering & EMI Control
- Can form common-mode or differential-mode filters.
- Used in LC networks, resonators, and signal conditioning.

### 5. Power Conversion & Storage
- Stores magnetic energy that is cycled during SMPS operation.
- Core component in flyback, forward, SEPIC, and Ćuk converters.

---

## Types of Coupled Inductors

| Type | Description | Common Use |
|---|---|---|
| **Transformer-style** | Tightly coupled coils on shared core | AC voltage conversion, isolation |
| **Common-mode choke** | Opposite winding orientation cancels differential noise | EMI filtering on power/data lines |
| **Flyback coupled inductor** | Stores energy in air-gap core | Flyback DC–DC converters |
| **Resonant coupled coils** | Loosely coupled, tuned to same frequency | Wireless power transfer |
| **Planar coupled inductors** | Lithographed windings on PCB layers | Compact MHz power converters |
| **Center-tapped coupled coil** | Shared winding tap point | Push-pull power supplies |

---

## Key Characteristics

| Parameter | Significance |
|---|---|
| **Mutual Inductance (M)** | Determines energy transfer strength |
| **Coupling Coefficient (k)** | Indicates magnetic linking efficiency |
| **Turns Ratio (N₁:N₂)** | Sets voltage/current transformation |
| **Leakage Inductance** | Uncoupled field energy → can cause voltage spikes |
| **Core Material** | Ferrite, nanocrystalline, iron powder affect efficiency & bandwidth |
| **Saturation Current** | Max current before core field collapses |

---

## Advantages & Limitations

### ✅ Advantages
- Efficient magnetic energy transfer
- Electrical isolation
- Enables voltage/current transformation
- Supports filtering and impedance matching
- Useful for both signals and power
- Can reduce common-mode noise

### ⚠ Limitations
- Core saturation limits performance
- Leakage inductance can cause switching spikes
- Efficiency depends on core material and frequency
- Parasitic capacitance can limit high-frequency use

---

## Common Applications

### 🔹 Power Electronics  
- Flyback, forward, SEPIC, Ćuk, isolated buck/boost converters
- High-voltage DC supplies
- Battery charging circuits

### 🔹 EMI & Signal Integrity  
- Common-mode chokes on USB, Ethernet, CAN, HDMI
- Differential signal filtering
- Ground noise suppression

### 🔹 RF & Communications  
- Baluns (balanced ↔ unbalanced conversion)
- Impedance matching networks
- Duplexer and transceiver circuits

### 🔹 Isolation & Safety  
- Medical equipment
- Industrial power
- High-voltage sensor isolation

---

## Coupled Inductors vs Transformers

| Feature | Coupled Inductor | Transformer |
|---|---|---|
| Primary role | Filtering, storage, conversion, isolation | AC voltage transformation |
| Air gap | Sometimes (for energy storage) | Rare (avoids, lowers efficiency) |
| Leakage inductance | Often intentionally used | Minimized |
| DC tolerance | Often designed for DC bias | Typically not |
| Energy storage | Yes | Minimal |

---

## Design Considerations

| Challenge | Solution |
|---|---|
| Core saturation | Use gapped cores, larger core, better material |
| Leakage inductance spikes | Snubbers, clamp circuits, RC damping |
| EMI noise | Shielding, choke configuration, filtering |
| AC losses | Litz wire, ferrite at HF, planar coils |
| Size reduction | Planar magnetics, high-µ materials |

---

## Summary

Coupled inductors enable:

- **Magnetic energy transfer**
- **Isolation and impedance transformation**
- **Efficient power conversion**
- **Noise suppression and signal conditioning**

They are fundamental in **power electronics, RF, communications, and EMI control**, bridging the gap between inductors and transformers depending on how they are applied.
