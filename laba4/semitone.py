from my_io import np


# Fhotoshop semitone.
def semitone(img):
    return (0.3 * img[:, :, 0] + 0.59 * img[:, :, 1] + 0.11 *
            img[:, :, 2]).astype(np.uint8)


if __name__ == '__main__':
    pass
