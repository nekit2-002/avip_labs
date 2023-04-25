import numpy as np
from numpy import mean
from math import pow, log, log2, floor

def contrast(img:np.array):
    flat_img = img.flatten()
    mn = round(mean(flat_img))

    positiveRange = max(2, max(flat_img) - mn)
    negativeRange = max(2, mn - min(flat_img))
    
    positiveAlpha = 2 ** 7/ log(positiveRange)
    negativeAlpha = 2 ** 7/ log(negativeRange)

    res_img = np.zeros_like(img)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            f = img[i, j] - mn
            if f >= 1:
                res_img[i, j] = mn + positiveAlpha * log(f)
            elif f <= -1:
                res_img[i, j] = mn - negativeAlpha * log(abs(f))
            else:
                res_img[i, j] = mn

    return res_img
            
    
    
    

   