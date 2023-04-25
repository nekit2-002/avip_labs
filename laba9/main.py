from scipy.io import wavfile
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np


def spectrogram_plot(samples, sample_rate):
    frequencies, times, my_spectrogram = signal.spectrogram(samples, sample_rate, scaling = 'spectrum', window = ('hann', ))
    plt.pcolormesh(times, frequencies, np.log10(my_spectrogram))
    plt.ylabel('Частота [Гц]')
    plt.xlabel('Время [с]')


def denoise(samples, sample_rate, cutoff_freuency, passes=1):
    z = signal.savgol_filter(samples, 100, 3)
    # Get parameters for filter function
    b, a = signal.butter(3, cutoff_freuency / sample_rate)
    # Lowpass filter
    zi = signal.lfilter_zi(b, a)
    for i in range(passes):
        z, _ = signal.lfilter(b, a, z, zi = zi * z[0])
    return z


def to_pcm(y):
    return np.int16(y / np.max(np.abs(y)) * 30000)

if __name__ == '__main__':
    dpi = 500

    sample_rate, samples = wavfile.read('src/oshinoko.wav')
    plt.figure(dpi=dpi)
  
    spectrogram_plot(samples, sample_rate)
    plt.savefig('results/spectrogram.png', dpi = dpi)
    plt.clf()

    denoised_0 = denoise(samples, sample_rate, cutoff_freuency = 2500, passes = 0)
    spectrogram_plot(denoised_0, sample_rate)
    plt.savefig('results/denoised_spectrogram_savgol.png', dpi = dpi)
    plt.clf()

    denoised = denoise(samples, sample_rate, cutoff_freuency = 2500)
    spectrogram_plot(denoised, sample_rate)
    plt.savefig('results/denoised_spectrogram_once.png', dpi=dpi)
    plt.clf()

    wavfile.write('results/denoised_once.wav', sample_rate, to_pcm(denoised))
    denoised_2 = denoise(samples, sample_rate, cutoff_freuency = 2500, passes = 2)
    spectrogram_plot(denoised_2, sample_rate)
    plt.savefig('results/denoised_spectrogram_twice.png', dpi = dpi)
    plt.clf()

    wavfile.write('results/denoised_twice.wav', sample_rate, to_pcm(denoised))