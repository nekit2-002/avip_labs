from PIL import Image
import numpy as np


def __rank_filter_helper(img, new_image, x, y, size, threshold):
    aperture = img[max(y - size // 2, 0) : min(y + size // 2 + 1, img.shape[0]),
                   max(x - size // 2, 0) : min(x + size // 2 + 1, img.shape[1])]
    
    if x == 5 and y == 5:
        print(aperture)

    ones = (aperture == 255).sum()

    if ones >= threshold:
        new_image[y, x] = 255


def rank_filter(img, size, threshold):
    if size % 2 == 0:
        raise Exception("Only even size of aperture is supported")

    new_img = np.zeros(shape=img.shape)

    x, y = 0, 0
    while y + size <= img.shape[0]:
        if y % 2 == 0:
            while x + 1 < img.shape[1]:
                __rank_filter_helper(img, new_img, x, y, size, threshold)
                x += 1
        else:
            while x - 1 > 0:
                __rank_filter_helper(img, new_img, x, y, size, threshold)
                x -= 1

        y += 1

    return new_img.astype(np.uint8)


if __name__ == '__main__':
    pass