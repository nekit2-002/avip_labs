import numpy as np
from scipy.io import wavfile
from scipy import interpolate

def integral_image(img: np.array) -> np.array:
    integral_img = np.zeros(shape=img.shape)
    integral_img[0, 0] = img[0, 0]

    for x in range(1, img.shape[0]):
        integral_img[x, 0] = img[x, 0] + integral_img[x - 1, 0]

    for y in range(1, img.shape[1]):
        integral_img[0, y] = img[0, y] + integral_img[0, y - 1]

    for x in range(1, img.shape[0]):
        for y in range(1, img.shape[1]):
            integral_img[x, y] = img[x, y] \
                                 - integral_img[x - 1, y - 1] \
                                 + integral_img[x - 1, y] \
                                 + integral_img[x, y - 1]

    return integral_img

def sum_in_frame(integral_img: np.array, x: int, y: int, frame_size: int):
    len = integral_img.shape[1] - 1
    hight = integral_img.shape[0] - 1

    half_frame = frame_size // 2
    above = y - half_frame - 1
    low = y + half_frame
    left = x - half_frame - 1
    right = x + half_frame
    
    A = integral_img[max(above, 0), max(left, 0)]
    B = integral_img[max(0, above), min(len, right)]
    C = integral_img[min(hight, low), max(left, 0)]
    D = integral_img[min(hight, low), min(right, len)]
    
    if max(left + 1, 0) == 0 and max(above + 1, 0) == 0:
        return D
    elif max(left + 1, 0) == 0:
        return D - B
    elif max(above + 1, 0) == 0:
        return D - C
    
    return D - C - B + A

def culculate_mean(integral_image: np.array, x: int, y: int, frame_size):
    square = frame_size**2
    s = sum_in_frame(integral_image, x, y, frame_size)
    return s // square

def changeSampleRate(path, NEW_SAMPLERATE = 20000):
    audioPath = "src/" + path
    old_samplerate, old_audio = wavfile.read(audioPath)

    if old_samplerate != NEW_SAMPLERATE:
        duration = old_audio.shape[0] / old_samplerate

        time_old = np.linspace(0, duration, old_audio.shape[0])
        time_new = np.linspace(0, duration, int(old_audio.shape[0] * NEW_SAMPLERATE / old_samplerate))

        interpolator = interpolate.interp1d(time_old, old_audio.T)
        new_audio = interpolator(time_new).T

        wavfile.write("results/wavs/" + path, NEW_SAMPLERATE, np.round(new_audio).astype(old_audio.dtype))
