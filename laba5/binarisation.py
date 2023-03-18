# 1 + (6 - 1)%10 == 6 --> Bernsen adaptive algorithm (modified)
import numpy as np

def simple_bin(img: np.array, thres: int = 40):
    res_img = np.empty_like(img)
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            res_img[x, y] = 255 if img[x, y] > thres else 0
    return res_img
