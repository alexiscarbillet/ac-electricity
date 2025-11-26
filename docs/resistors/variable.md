---
tags:
  - resistors
---

# 🕹️ Variable Resistors

**Variable resistors** are electro-mechanical components whose resistance can be manually or electronically adjusted. They are primarily used to **tune, control, and regulate** electrical parameters in a circuit. The two main device types are **Potentiometers** and **Rheostats**.

---

## ⚙️ Construction and Principle

All variable resistors share a common fundamental structure involving a resistive element and a movable contact.

### The Mechanism
1.  **Resistive Element:** This is a track or strip made of a resistive material (carbon composition, wirewound, or cermet).
2.  **Wiper (Sliding Contact):** A movable conductive contact that slides along the resistive element.
3.  **Adjustment:** By physically moving the wiper, the electrical path length through the resistive element changes, thereby altering the total resistance between the terminals connected to the element and the wiper.

### Rheostat Mode (2-Terminal)
A **rheostat** is used to control the **current** in a circuit.
* **Connection:** Uses only two terminals: one end of the resistive element and the wiper terminal.
* **Function:** By varying the resistance, the rheostat directly limits the current flowing through the circuit it is connected to (e.g., controlling motor speed or light brightness).

### Potentiometer Mode (3-Terminal)
A **potentiometer** ("pot") is used primarily as a **voltage divider** to produce a variable output voltage proportional to the input voltage.
* **Connection:** Uses all three terminals: both ends of the resistive element (across the input voltage, $V_{in}$) and the wiper terminal (for the output voltage, $V_{out}$).
* **Function:** $V_{out}$ is a fraction of $V_{in}$, determined by the wiper's position. This is the mechanism for most **volume controls** and analog signal adjustments.

---

## 📐 Types and Tapors

Variable resistors are classified by their physical form and their resistive profile.

### Physical Types
| Type | Description | Primary Use |
| :--- | :--- | :--- |
| **Rotary Potentiometer** | Resistance track is circular; adjusted by turning a shaft. | Volume control, tuning, continuous adjustment. |
| **Slide Potentiometer** | Resistance track is linear; adjusted by sliding a knob. | Audio mixing consoles (faders). |
| **Trimmer Potentiometer (Trimpot)** | Small, often screwdriver-adjusted, intended for infrequent internal calibration. | Setting circuit bias or reference levels. |
| **Digital Potentiometer** (Digipot) | Semiconductor IC that uses digital signals (e.g., SPI) to set the resistance ratio electronically. | Modern systems requiring micro-controller control. |

### Taper (Resistance Profile)
* **Linear Taper (Type B):** Resistance changes proportionally to the angle of rotation or distance of travel. Used for controls like balance or trimming.
* **Logarithmic Taper (Type A):** Resistance changes exponentially. Used for controls like **audio volume**, as human hearing perceives loudness logarithmically.

---

## 📜 History and Applications

The fundamental idea of variable resistance dates back to the **19th century**.

* **1841:** Sir Charles Wheatstone coined the term **"rheostat"** for a device controlling current, originally using wrapped wire.
* **Early 20th Century:** Potentiometers became essential in **radio receivers** for tuning and volume control.
* **Mid-20th Century:** The shift from wirewound to **carbon composition** and later **cermet** elements improved stability, reduced noise, and lowered cost, making them ubiquitous in consumer electronics.

Variable resistors continue to be used wherever a mechanical analog adjustment is needed, spanning **audio systems**, **lighting dimmers**, **motor speed controls**, and precise **sensor calibration**.