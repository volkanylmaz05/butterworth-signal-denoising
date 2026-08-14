import matplotlib.pyplot as plt #for graph 
import numpy as np #for linspace etc.
from scipy import signal #for signal functions

fs = 500  # Sampling frequency

t = np.linspace(0, 1, fs) # len(t) = 500

clear_signal = np.sin(2 * np.pi *5*t)

np.random.seed(0) #for similarity in noise generation
noise = 0.5 * np.random.randn(len(t))
noisy_signal = clear_signal + noise

b, a = signal.butter(4, 40, fs=fs, btype="low")
filtered_signal = signal.filtfilt(b, a, noisy_signal)

plt.figure(figsize=(12, 8))
plt.subplot(3, 1, 1)
plt.plot(t, clear_signal)
plt.title("Clear Signal")
plt.ylabel("Amplitude")

plt.subplot(3, 1, 2)
plt.plot(t, noisy_signal)
plt.title("Noisy Signal")
plt.ylabel("Amplitude")

plt.subplot(3, 1, 3)
plt.plot(t, filtered_signal)
plt.title("Filtered Signal")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()