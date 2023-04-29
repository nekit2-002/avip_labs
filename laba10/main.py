from scipy.io import wavfile
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

def spectrogram_plot(samples, sample_rate,t = 10000):
    frequencies, times, my_spectrogram = signal.spectrogram(samples, sample_rate, scaling = 'spectrum', window = ('hann'))
    spec = np.log10(my_spectrogram)
    plt.pcolormesh(times, frequencies, spec, shading='gouraud', vmin=spec.min(), vmax=spec.max())

    plt.ylim(top=t)
    plt.ylabel('Частота [Гц]')
    plt.xlabel('Время [с]')

def denoise(samples, sample_rate, cutoff_freuency, passes=1):
    z = signal.savgol_filter(samples, 100, 3)
    # Get parameters for filter function
    b, a = signal.butter(3, cutoff_freuency / sample_rate)
    # Lowpass filter
    zi = signal.lfilter_zi(b, a)
    for _ in range(passes):
        z, _ = signal.lfilter(b, a, z, zi = zi * z[0])
    return z

def to_pcm(y):
    return np.int16(y / np.max(np.abs(y)) * 32767)

if __name__ == '__main__':
    dpi = 500

    sample_rate, samples = wavfile.read('src/voice_a.wav')
    plt.figure(dpi = dpi)

    spectrogram_plot(samples, sample_rate)
    plt.savefig('results/spectrogram_a.png', dpi = dpi)
    plt.clf()

    denoised = denoise(samples, sample_rate, cutoff_freuency = 4000)
    spectrogram_plot(denoised, sample_rate, 6000)
    plt.axhline(y = 300, color = 'r', linestyle = '-', lw= 0.5, label = "Форманты")
    plt.axhline(y = 750, color = 'r', linestyle = '-', lw= 0.5)
    plt.axhline(y = 1200, color = 'r', linestyle = '-', lw= 0.5)
    plt.axhline(y = 2600, color = 'r', linestyle = '-', lw= 0.5)
    plt.axhline(y = 3100, color = 'r', linestyle = '-', lw= 0.5)
    plt.legend(bbox_to_anchor = (1.0, 1), loc = 'upper right')
    plt.savefig('results/denoised/denoised_a.png', dpi = dpi)
    plt.clf()

    wavfile.write('results/wavs/denoised_voice_a.wav', sample_rate, to_pcm(denoised))



    sample_rate, samples = wavfile.read('src/voice_i.wav')
    plt.figure(dpi = dpi)

    spectrogram_plot(samples, sample_rate)
    plt.savefig('results/spectrogram_i.png', dpi = dpi)
    plt.clf()

    denoised = denoise(samples, sample_rate, cutoff_freuency = 4000)
    spectrogram_plot(denoised, sample_rate, 6000)
    plt.axhline(y = 250, color = 'r', linestyle = '-', lw= 0.5, label = "Форманты")
    plt.axhline(y = 2000, color = 'r', linestyle = '-', lw= 0.5)
    plt.axhline(y = 2800, color = 'r', linestyle = '-', lw= 0.5)
    plt.axhline(y = 3300, color = 'r', linestyle = '-', lw= 0.5)
    plt.legend(bbox_to_anchor = (1.0, 1), loc = 'upper right')
    plt.savefig('results/denoised/denoised_i.png', dpi = dpi)
    plt.clf()

    wavfile.write('results/wavs/denoised_voice_i.wav', sample_rate, to_pcm(denoised))


    sample_rate, samples = wavfile.read('src/voice_gav.wav')
    plt.figure(dpi = dpi)

    spectrogram_plot(samples, sample_rate)
    plt.savefig('results/spectrogram_gav.png', dpi = dpi)
    plt.clf()

    denoised = denoise(samples, sample_rate, cutoff_freuency = 4000, passes = 2)
    spectrogram_plot(denoised, sample_rate, 6000)
    plt.axhline(y = 300, color = 'r', linestyle = '-', lw= 0.5, label = "Форманты")
    plt.axhline(y = 600, color = 'r', linestyle = '-', lw= 0.5)
    plt.axhline(y = 1000, color = 'r', linestyle = '-', lw= 0.5)
    plt.axhline(y = 2300, color = 'r', linestyle = '-', lw= 0.5)
    plt.legend(bbox_to_anchor = (1.0, 1), loc = 'upper right')
    plt.savefig('results/denoised/denoised_gav.png', dpi = dpi)
    plt.clf()

    wavfile.write('results/wavs/denoised_voice_gav.wav', sample_rate, to_pcm(denoised))
