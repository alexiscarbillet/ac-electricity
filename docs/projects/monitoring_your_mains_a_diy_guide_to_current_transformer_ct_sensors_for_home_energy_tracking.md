# Monitoring Your Mains A DIY Guide to Current Transformer (CT) Sensors for Home Energy Tracking

For many DIY enthusiasts, the ultimate goal of a smart home is transparency—knowing exactly how many watts your workshop, HVAC system, or crypto-miner is pulling at any given second. While smart plugs are great for individual appliances, monitoring an entire electrical panel requires a more specialized component: the Current Transformer (CT) sensor.

CT sensors allow you to measure AC current non-invasively, meaning you can monitor high-voltage lines without actually cutting or splicing into the copper. This makes them the gold standard for DIY energy monitoring projects using platforms like ESP32, Arduino, or Raspberry Pi.

## How CT Sensors Work

A Current Transformer works on the principle of electromagnetic induction. When an alternating current (AC) flows through a primary wire (like the "Hot" wire in your breaker box), it generates a magnetic field around that wire. 

The CT sensor consists of a magnetic core wrapped in many turns of fine wire (the secondary winding). When you clamp the sensor around the primary wire, the magnetic field induces a much smaller, proportional current in the secondary winding. For example, a "100A:50mA" sensor will output 50 milliamps of current for every 100 amps flowing through the main line.

## Split-Core vs. Solid-Core Sensors

When choosing a sensor for a DIY project, you will encounter two primary form factors. For retrofitting an existing breaker panel, the choice is almost always split-core.

| Feature | Solid-Core CT | Split-Core CT | Rogowski Coil |
| :--- | :--- | :--- | :--- |
| **Installation** | Requires disconnecting wire | Clamps around wire | Flexible loop, wraps around |
| **Accuracy** | High | Moderate to High | High (excellent for high current) |
| **Cost** | Low | Moderate | High |
| **Best For** | New builds / OEM equipment | DIY Retrofitting / Panels | High-amperage industrial use |
| **Safety** | High | High (if burden is internal) | High |

## The Critical Component: The Burden Resistor

CT sensors output current, but microcontrollers (like an Arduino) measure voltage. To bridge this gap, you need a **burden resistor**. 

By placing a resistor across the output leads of the CT sensor, the output current is forced through the resistor, creating a small, measurable voltage drop (Ohm’s Law: $V = I \times R$). 

**Warning:** Never "open-circuit" a CT sensor while it is clamped around a live wire. Without a burden resistor to dissipate the energy, the voltage on the secondary leads can spike to thousands of volts, potentially destroying the sensor or causing an electrical arc. Many popular DIY sensors, like the **SCT-013-000**, require an external burden resistor, while others (like the **SCT-013-030**) have one built-in to output a safe 0-1V signal.

## DIY Implementation Steps

If you are building a monitoring system using an ESP32 or similar 3.3V microcontroller, follow these technical guidelines:

### 1. Signal Offsetting
Microcontroller Analog-to-Digital Converters (ADCs) can only measure positive voltages (e.g., 0V to 3.3V). Since AC current is a sine wave that swings positive and negative, you must use a voltage divider (two identical resistors) to "lift" the CT signal to a midpoint (1.65V). This allows the ADC to read the full wave.

### 2. Sizing the Sensor
Don't use a 100A sensor to monitor a 10A circuit. You will lose "resolution." The ADC has a finite number of steps (e.g., 1024 steps for a 10-bit ADC). If your sensor is oversized, the signal will be too small to distinguish from background electronic noise.

### 3. Calculating Real Power
A CT sensor only measures current (Amps). To calculate true Power (Watts), you also need to know the Voltage. While you can assume a constant 120V or 230V, household voltage fluctuates. For a truly accurate DIY build, use an AC-to-AC transformer to safely sample the voltage waveform alongside the current waveform. This allows you to calculate the "Power Factor"—the efficiency of your electrical system.

## Safety and Ethics

Working inside a breaker panel is inherently dangerous. While CT sensors are non-invasive, you are still working near exposed busbars. 
- **Always** turn off the main breaker before opening the panel.
- **Never** clamp a CT sensor around both the Hot and Neutral wires simultaneously; the fields will cancel each other out, resulting in a zero reading.
- **Ensure** your DIY enclosure is non-conductive and your low-voltage wires are properly routed away from high-voltage components.

By mastering the CT sensor, you move beyond "guessing" your energy usage and gain the data needed to optimize your home's efficiency, one milliamp at a time.