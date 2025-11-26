---
tags:
  - resistors
---

# 💡 Photoresistor (LDR)

A **Photoresistor**, also known as a **Light-Dependent Resistor (LDR)** or **photocell**, is a passive component whose electrical **resistance decreases as the intensity of incident light increases**. They are essential for simple, cost-effective light-sensing and control circuits.

---

## ⚡ Principle of Photoconductivity

Photoresistors operate based on the phenomenon of **photoconductivity**, which describes how a semiconductor material's ability to conduct electricity changes when it absorbs light.

### 1. Structure and Material
* **Material:** LDRs are typically made from semiconductor materials, historically **Cadmium Sulfide ($\text{CdS}$)** or **Cadmium Selenide ($\text{CdSe}$)**.
* **Design:** The material is deposited as a zigzag track between two electrodes on a ceramic substrate, maximizing the surface area exposed to light.
    

### 2. The Mechanism
1.  **Dark State (High Resistance):** In the dark, the semiconductor has very few mobile charge carriers (electrons), resulting in a high electrical resistance, often in the $\text{M}\Omega$ range.
2.  **Light State (Low Resistance):** When **photons** (light particles) strike the material, their energy is absorbed, causing bound electrons to jump into the conduction band.
3.  **Carrier Generation:** This process generates **electron-hole pairs**, increasing the number of mobile charge carriers.
4.  **Resistance Change:** The increased mobile charge carriers increase the material's **conductivity** and thus **decrease the resistance**.

### Inverse Relationship
The relationship between illumination ($\mathcal{E}$) and resistance ($R$) is **inverse and non-linear**:
* **High Illumination $\rightarrow$ Low Resistance** (e.g., $100\ \Omega$ to $1\ \text{k}\Omega$)
* **Low Illumination $\rightarrow$ High Resistance** (e.g., $1\ \text{M}\Omega$ to $10\ \text{M}\Omega$)

---

## ⏳ History and Applications

### Historical Milestones
* **19th Century:** The underlying principle of photoconductivity was first observed.
* **Mid-20th Century:** Commercial LDRs (primarily $\text{CdS}$) became widely adopted in consumer and military electronics due to their low cost and simplicity.
* **Post-War Applications:** Found widespread use in early **light meters for photography**, automatic **streetlights**, and simple **security and alarm systems**.

### Modern Usage and Considerations
While modern optoelectronic sensors (like photodiodes and phototransistors) offer better speed and spectral response, LDRs remain popular in applications where **simplicity, cost, and a large resistance change** are prioritized over speed.

* **Automatic Lighting:** Turning garden or pathway lights on at dusk.
* **Novelty and Toys:** Simple light-sensitive circuits.

***
**⚠️ Regulatory Note on Cadmium Sulfide ($\text{CdS}$):**
Many traditional LDRs utilize Cadmium Sulfide, which is subject to restrictions (e.g., **RoHS/WEEE** directives in the EU) due to the toxicity of Cadmium. For new designs, engineers increasingly opt for **Cadmium-free** alternatives (like lead sulfide ($\text{PbS}$)) or alternative sensors entirely.
***