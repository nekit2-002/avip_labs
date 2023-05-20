from scipy.io import wavfile
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
from helpers import *

def spectrogram_plot(samples, sample_rate,t = 10000):
    frequencies, times, my_spectrogram = signal.spectrogram(samples, sample_rate, scaling = 'spectrum', window = ('hann'))
    spec = np.log10(my_spectrogram)
    plt.pcolormesh(times, frequencies, spec, shading='gouraud', vmin=spec.min(), vmax=spec.max())

    plt.ylim(top=t)
    plt.ylabel('Частота [Гц]')
    plt.xlabel('Время [с]')
    return my_spectrogram, frequencies

if __name__ == '__main__':
   changeSampleRate("voice_a.wav")
   sample_rate_a , samples_a = wavfile.read("results/wavs/voice_a.wav")

   dpi = 500
   spectogram_a, frequencies_a = spectrogram_plot(samples_a, sample_rate_a)
   plt.savefig('results/spectrogram_a.png', dpi = dpi)
   plt.clf()

   changeSampleRate("voice_i.wav")
   sample_rate_i , samples_i = wavfile.read("results/wavs/voice_i.wav")
   spectogram_i, frequencies_i = spectrogram_plot(samples_i, sample_rate_i)
   plt.savefig('results/spectrogram_i.png', dpi = dpi)
   plt.clf()

   changeSampleRate("voice_gav.wav")
   sample_rate_i , samples_i = wavfile.read("results/wavs/voice_gav.wav")
   spectogram_i, frequencies_i = spectrogram_plot(samples_i, sample_rate_i)
   plt.savefig('results/spectrogram_gav.png', dpi = dpi)
   plt.clf()
