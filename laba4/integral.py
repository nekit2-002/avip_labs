from my_io import np 

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
