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
    plt.axhline(y = 740, color = 'r', linestyle = '-', lw= 0.5)
    plt.axhline(y = 1200, color = 'r', linestyle = '-', lw= 0.5)
    plt.axhline(y = 2600, color = 'r', linestyle = '-', lw= 0.5)
    plt.axhline(y = 3100, color = 'r', linestyle = '-', lw= 0.5)
    
    main_tone_xs = [0.2, 0.4, 0.6, 0.75, 0.9, 1.1, 1.2, 1.3, 1.6, 1.8,  2, 2.25, 2.5]
    main_tone_ys = [253, 253, 253,  253, 253, 253, 253, 260, 280, 300, 410, 490, 520]
    plt.plot(main_tone_xs, main_tone_ys, 'o-b', label = "Основной тон", lw = 0.5, ms=2)
    
    garmonic1_xs = [ 2.25,  2.3,  2.4,  2.5]
    garmonic1_ys = [1000, 1050, 1070, 1200]
    plt.plot(garmonic1_xs,garmonic1_ys, 'o--g', label = "Гармоники", lw = 0.5, ms=2)
    
    garmonic2_xs = [ 2.1,  2.25,  2.35,  2.45,  2.5]
    garmonic2_ys = [1100,  1450, 1570, 1640, 1700]
    plt.plot(garmonic2_xs,garmonic2_ys, 'o--g', lw = 0.5, ms=2)
    
    plt.legend()
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
    
    main_tone_xs = [0.3, 0.5, 0.6, 0.75, 0.9, 1.1, 1.2, 1.3, 1.5, 1.6, 1.7, 1.8, 1.9]
    main_tone_ys = [253, 253, 253,  253, 260, 265, 300, 450, 550, 580, 600, 630, 640]
    plt.plot(main_tone_xs, main_tone_ys, 'o-b', label = "Основной тон", lw = 0.5, ms=2)
    
    garmonic1_xs = [ 1.3,  1.6,  1.7,  1.8,  1.9]
    garmonic1_ys = [1300, 1640, 1670, 1800, 1930]
    plt.plot(garmonic1_xs,garmonic1_ys, 'o--g', label = "Гармоники", lw = 0.5, ms=2)

    garmonic2_xs = [ 1.4,  1.55,  1.7,  1.8,  1.9]
    garmonic2_ys = [2200,  2500, 2650, 2900, 3100]
    plt.plot(garmonic2_xs,garmonic2_ys, 'o--g', lw = 0.5, ms=2)
    
    garmonic3_xs = [ 1.45,  1.51,  1.67, 1.74,  1.9]
    garmonic3_ys = [ 2800,  3000, 3300, 3470, 3750]
    plt.plot(garmonic3_xs,garmonic3_ys, 'o--g', lw = 0.5, ms=2)
    
    plt.legend()
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
    plt.legend()
    plt.savefig('results/denoised/denoised_gav.png', dpi = dpi)
    plt.clf()

    wavfile.write('results/wavs/denoised_voice_gav.wav', sample_rate, to_pcm(denoised))
