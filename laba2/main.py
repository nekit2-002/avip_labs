from bernsen import bernsen_threshold
from semitone import to_semitone, image_to_np_array, path
from semitone import Image, np

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


def run_bernsen(img_name):
    print("Введите размер окна:")
    frame_size = safe_number_input(3, 20)
    print("Введите порог t:")
    t = safe_number_input(0, 255)

    return Image.fromarray(bernsen_threshold(img_name, frame_size, t).astype(np.uint8), "L")


images = {
    "House": 'house.png',
    "Anime face": 'tsukyo.png',
    "Face": 'nando.png',
    "Chess": 'chess.png',
    "Book": 'text.png'
}

operations = {
        'Полутон': 'semitone',
        'Бинаризация': 'thresholding'
}


if __name__ == '__main__':
    print('Выберите изображение:')
    selected_image = prompt(images)
    img = image_to_np_array(selected_image)

    print("Выберите обработку изображения:")
    selected_handle = prompt(operations)

    match selected_handle:
        case 'semitone':
            result = to_semitone(selected_image)
        case 'thresholding':
            result = run_bernsen(img)
        case _:
            exit()

    print('Введите название сохраненного изображения (оставьте пустым, чтобы \
не сохранять)')
    selected_path = input()
    if selected_path:
        result.save(path + '\\pictures_results\\' + selected_path)
