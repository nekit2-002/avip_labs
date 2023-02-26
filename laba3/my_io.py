from PIL import Image
from filter import np
from sys import path

path = path[0]

def safe_number_input(lower_bound=None, upper_bound=None):
    input_correct = False
    user_input = 0
    while not input_correct:
        try:
            user_input = int(input('> '))
            if lower_bound is not None and user_input < lower_bound:
                raise ValueError
            if upper_bound is not None and user_input > upper_bound:
                raise ValueError
            input_correct = True
        except ValueError:
            print("Введите корректное значение")
    return user_input


def prompt(variants: dict):
    for number, variant in enumerate(variants.keys(), 1):
        print(f'{number} - {variant}')
    input_correct = False
    user_input = 0
    while not input_correct:
        try:
            user_input = int(input('> '))
            if user_input <= 0 or user_input > len(variants):
                raise ValueError
            input_correct = True
        except ValueError:
            print("Введите корректное значение")
    return dict(enumerate(variants.values(), 1))[user_input]


def image_to_np_array(image_name: str) -> np.array:
    img_src = Image.open(path + '\\pictures_src\\' + image_name).convert('L')
    return np.array(img_src)
