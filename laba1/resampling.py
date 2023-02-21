from PIL import Image
import numpy as np
from sys import path
from math import floor
from operator import mul

path = path[0]

def image_to_np_array(image_name: str) -> np.array:
    img_src = Image.open(path + '\\pictures_src\\' + image_name).convert('RGB')
    return np.array(img_src)


def two_step_resampling(img: np.array, numerator: int,
                        denominator: int) -> np.array:
    tmp = one_step_resampling(img, numerator, mul,
                              lambda a, b: floor(a / b))
    return one_step_resampling(tmp, denominator,
                               lambda a, b: int(round(a / b)),
                               mul)


def one_step_resampling(img: np.array, factor: float, f1, f2):
    dimensions = img.shape[0:2]
    new_dimensions = tuple(f1(dimension, factor) for dimension in
                           dimensions)
    new_shape = (*new_dimensions, img.shape[2])
    new_img = np.empty(new_shape)

    for x in range(new_dimensions[0] - 1): # столбец
        for y in range(new_dimensions[1] - 1): # строка
            new_img[x, y] = img[
                f2(x, factor), 
                f2(y, factor)
            ]
    return new_img


if __name__ == '__main__':
    print(path)