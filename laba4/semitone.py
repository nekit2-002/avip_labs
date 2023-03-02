from my_io import image_to_np_array,image_from_np_array, np

# Fhotoshop semitone.
def semitone(img):
    return (0.3 * img[:, :, 0] + 0.59 * img[:, :, 1] + 0.11 *
            img[:, :, 2]).astype(np.uint8)


def to_semitone(img_name):
    img = image_to_np_array(img_name)
    return image_from_np_array(img, semitone)


if __name__ == '__main__':
    pass