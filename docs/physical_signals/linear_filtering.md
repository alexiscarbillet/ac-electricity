

# Linear filtering

## Periodic signals

Periodic signals refers to periodic signals, which are signals that repeat their values at regular intervals over time. Let's delve into the requested topics related to periodic signals, including Fourier series decomposition, average value, effective value, and Parseval's equality.

### 1. Fourier Series Decomposition

A periodic signal can be expressed as a sum of sine and cosine functions (or complex exponentials) using Fourier series. For a periodic function \( f(t) \) with period \( T \), the Fourier series is given by:

\[
f(t) = a_0 + \sum_{n=1}^{\infty} \left( a_n \cos\left(\frac{2\pi nt}{T}\right) + b_n \sin\left(\frac{2\pi nt}{T}\right) \right)
\]

where:
- \( a_0 \) is the average (DC component) of the function over one period.
- \( a_n \) and \( b_n \) are the Fourier coefficients defined as:

\[
a_0 = \frac{1}{T} \int_0^T f(t) \, dt
\]

\[
a_n = \frac{2}{T} \int_0^T f(t) \cos\left(\frac{2\pi nt}{T}\right) \, dt
\]

\[
b_n = \frac{2}{T} \int_0^T f(t) \sin\left(\frac{2\pi nt}{T}\right) \, dt
\]

### 2. Average Value and Effective Value

**Average Value**: The average value \( \bar{f} \) of a periodic function over one period \( T \) is given by:

\[
\bar{f} = \frac{1}{T} \int_0^T f(t) \, dt
\]

This represents the mean value of the signal over time.

**Effective Value** (RMS Value): The effective value or root mean square (RMS) value \( f_{\text{rms}} \) of the periodic signal is defined as:

\[
f_{\text{rms}} = \sqrt{\frac{1}{T} \int_0^T (f(t))^2 \, dt}
\]

This value indicates the equivalent direct current (DC) value that would produce the same heating effect in a resistor as the AC signal does.

### 3. Parseval's Equality

Parseval's equality states that the total energy of a periodic signal in the time domain is equal to the total energy in the frequency domain. For a periodic signal \( f(t) \) with Fourier coefficients \( a_n \) and \( b_n \), it is expressed as:

\[
\frac{1}{T} \int_0^T |f(t)|^2 \, dt = \frac{a_0^2}{2} + \sum_{n=1}^{\infty} \left( a_n^2 + b_n^2 \right)
\]

This equation states that the average power (energy per unit time) of the signal in the time domain equals the sum of the squares of its Fourier coefficients, illustrating the conservation of energy between the time and frequency domains.

### Summary

- **Fourier Series Decomposition** allows a periodic function to be represented as a sum of sine and cosine functions.
- **Average Value** gives the mean over one period, while the **Effective Value (RMS)** quantifies the power of the signal.
- **Parseval's Equality** relates the energy in the time domain to that in the frequency domain, ensuring energy conservation.

## Transfer function. Bode diagram

Let’s explore the concept of transfer functions and Bode diagrams, covering the requested points: filter notion and transfer function, main types of filters, gain in decibels with Bode diagrams, and an example of a first-order low-pass filter.

### 1. Notion de Filtre et Fonction de Transfert

**Transfer Function**: The transfer function \( H(s) \) of a linear time-invariant (LTI) system is a mathematical representation that relates the output \( Y(s) \) to the input \( X(s) \) in the Laplace domain. It is defined as:

\[
H(s) = \frac{Y(s)}{X(s)}
\]

where:
- \( s \) is a complex frequency variable \( s = \sigma + j\omega \).
- \( Y(s) \) is the Laplace transform of the output.
- \( X(s) \) is the Laplace transform of the input.

**Filter**: A filter is a system that allows certain frequencies to pass while attenuating others. Filters can be characterized by their transfer functions, which determine how the amplitude and phase of the output signal change in response to different frequencies.

### 2. Principaux Types de Filtre

The main types of filters include:

- **Low-Pass Filter (LPF)**: Allows frequencies below a certain cutoff frequency \( f_c \) to pass while attenuating higher frequencies.
  
- **High-Pass Filter (HPF)**: Allows frequencies above a certain cutoff frequency \( f_c \) to pass while attenuating lower frequencies.
  
- **Band-Pass Filter (BPF)**: Allows frequencies within a certain range (between \( f_1 \) and \( f_2 \)) to pass while attenuating frequencies outside this range.

- **Band-Stop Filter (BSF)**: Attenuates frequencies within a certain range (between \( f_1 \) and \( f_2 \)) while allowing other frequencies to pass.

### 3. Gain en Décibel et Diagramme de Bode

**Gain in Decibels**: The gain of a filter is often expressed in decibels (dB) using the formula:

\[
G(dB) = 20 \log_{10} \left| H(j\omega) \right|
\]

where:
- \( H(j\omega) \) is the transfer function evaluated at \( s = j\omega \) (purely imaginary frequency).

**Bode Diagram**: A Bode diagram consists of two plots:
- The **Magnitude Plot** shows the gain in dB against frequency on a logarithmic scale.
- The **Phase Plot** shows the phase shift (in degrees) against frequency on a logarithmic scale.

Bode diagrams are particularly useful for analyzing the frequency response of LTI systems.

### 4. Exemple : Filtre Passe-Bas du Premier Ordre

A first-order low-pass filter can be represented by the following transfer function:

\[
H(s) = \frac{1}{s + \omega_c}
\]

where \( \omega_c = 2\pi f_c \) is the cutoff angular frequency. In this case, the filter allows frequencies below \( f_c \) to pass while attenuating frequencies above \( f_c \).

**Magnitude Response**: The magnitude of the transfer function at a frequency \( \omega \) is:

\[
|H(j\omega)| = \frac{1}{\sqrt{\omega^2 + \omega_c^2}}
\]

The gain in dB is given by:

\[
G(dB) = 20 \log_{10} \left| H(j\omega) \right| = -20 \log_{10} \sqrt{\omega^2 + \omega_c^2}
\]

**Phase Response**: The phase shift \( \phi \) is given by:

\[
\phi = \tan^{-1}\left(-\frac{\omega}{\omega_c}\right)
\]

#### Bode Diagram for a First-Order Low-Pass Filter

- **Magnitude Plot**: At low frequencies, the gain approaches 0 dB, and at the cutoff frequency \( f_c \), the gain is -3 dB. As frequency increases, the gain decreases, typically at a slope of -20 dB/decade.
  
- **Phase Plot**: The phase starts at 0° for low frequencies and approaches -90° as the frequency increases.

### Summary

- **Transfer Function** describes how input relates to output in the frequency domain.
- **Filters** (LPF, HPF, BPF, BSF) are systems that modify the amplitude of signals at different frequencies.
- **Gain in Decibels** provides a logarithmic measure of signal strength, while **Bode Diagrams** visualize the frequency response.
- The example of a **first-order low-pass filter** illustrates these concepts, showing how it allows low frequencies to pass while attenuating higher frequencies.

## Simple models of passive filters

### 1. Filtre Passe-Haut d’Ordre 1 (First-Order High-Pass Filter)

A first-order high-pass filter can be constructed using a capacitor and a resistor (RC configuration). The basic circuit consists of a capacitor \( C \) in series with a resistor \( R \), with the output taken across the resistor.

#### Transfer Function

The transfer function \( H(s) \) for a first-order high-pass filter is given by:

\[
H(s) = \frac{s}{s + \omega_c}
\]

where \( \omega_c = \frac{1}{RC} \) is the cutoff angular frequency.

#### Magnitude and Phase Response

The magnitude response \( |H(j\omega)| \) and phase response \( \phi \) can be calculated as follows:

\[
|H(j\omega)| = \frac{\omega}{\sqrt{\omega^2 + \omega_c^2}}
\]

\[
G(dB) = 20 \log_{10} \left| H(j\omega) \right| = 20 \log_{10} \left( \frac{\omega}{\sqrt{\omega^2 + \omega_c^2}} \right)
\]

\[
\phi = \tan^{-1}\left(\frac{\omega_c}{\omega}\right)
\]

#### Characteristics

- The filter allows frequencies above the cutoff frequency \( f_c \) (where \( f_c = \frac{\omega_c}{2\pi} \)) to pass and attenuates lower frequencies.
- At the cutoff frequency, the gain is -3 dB.

### 2. Filtre Passe-Bande d’Ordre 2 (Second-Order Band-Pass Filter)

A second-order band-pass filter can be constructed using a combination of resistors, capacitors, and inductors (RLC configuration). A common configuration is to place a resistor \( R \) in series with a parallel combination of an inductor \( L \) and a capacitor \( C \).

#### Transfer Function

The transfer function \( H(s) \) for a second-order band-pass filter is given by:

\[
H(s) = \frac{K \cdot s}{s^2 + \frac{\omega_0}{Q} \cdot s + \omega_0^2}
\]

where:
- \( \omega_0 = \frac{1}{\sqrt{LC}} \) is the resonant angular frequency.
- \( Q = \frac{\omega_0}{\Delta\omega} \) is the quality factor, determining the bandwidth.
- \( K \) is a gain factor.

#### Magnitude and Phase Response

The magnitude response and phase response are given by:

\[
|H(j\omega)| = \frac{K \cdot \omega}{\sqrt{(\omega_0^2 - \omega^2)^2 + \left(\frac{\omega_0}{Q} \cdot \omega\right)^2}}
\]

\[
G(dB) = 20 \log_{10} \left| H(j\omega) \right|
\]

\[
\phi = \tan^{-1}\left(\frac{\frac{\omega_0}{Q} \cdot \omega}{\omega_0^2 - \omega^2}\right)
\]

#### Characteristics

- The filter allows a specific range of frequencies centered around \( f_0 = \frac{\omega_0}{2\pi} \) to pass while attenuating frequencies outside this range.
- The bandwidth of the filter is determined by the quality factor \( Q \).

### 3. Filtre Passe-Bas du Deuxième Ordre (Second-Order Low-Pass Filter)

A second-order low-pass filter can be implemented using an RLC circuit with a resistor \( R \), an inductor \( L \), and a capacitor \( C \) in a configuration where the output is taken across the capacitor.

#### Transfer Function

The transfer function \( H(s) \) for a second-order low-pass filter is given by:

\[
H(s) = \frac{\omega_0^2}{s^2 + \frac{\omega_0}{Q} \cdot s + \omega_0^2}
\]

where:
- \( \omega_0 = \frac{1}{\sqrt{LC}} \) is the cutoff angular frequency.
- \( Q = \frac{\omega_0}{\Delta\omega} \) is the quality factor.

#### Magnitude and Phase Response

The magnitude response and phase response are given by:

\[
|H(j\omega)| = \frac{\omega_0^2}{\sqrt{(\omega_0^2 - \omega^2)^2 + \left(\frac{\omega_0}{Q} \cdot \omega\right)^2}}
\]

\[
G(dB) = 20 \log_{10} \left| H(j\omega) \right|
\]

\[
\phi = \tan^{-1}\left(-\frac{\frac{\omega_0}{Q} \cdot \omega}{\omega_0^2 - \omega^2}\right)
\]

#### Characteristics

- The filter allows frequencies below the cutoff frequency \( f_c \) (where \( f_c = \frac{\omega_0}{2\pi} \)) to pass and attenuates higher frequencies.
- At the cutoff frequency, the gain is -3 dB.

### Summary

- **First-Order High-Pass Filter**: Allows high frequencies to pass; characterized by \( H(s) = \frac{s}{s + \omega_c} \).
- **Second-Order Band-Pass Filter**: Allows a specific range of frequencies to pass; characterized by \( H(s) = \frac{K \cdot s}{s^2 + \frac{\omega_0}{Q} \cdot s + \omega_0^2} \).
- **Second-Order Low-Pass Filter**: Allows low frequencies to pass; characterized by \( H(s) = \frac{\omega_0^2}{s^2 + \frac{\omega_0}{Q} \cdot s + \omega_0^2} \).
