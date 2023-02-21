from resampling import *


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


def safe_number_input(number_type: type, lower_bound=None, upper_bound=None):
    input_correct = False
    user_input = 0

    while not input_correct:
        try:
            user_input = number_type(input('> '))
            if lower_bound is not None and user_input < lower_bound:
                raise ValueError
            if upper_bound is not None and user_input > upper_bound:
                raise ValueError
            input_correct = True
        except ValueError:
            print("Введите корректное значение")
    return user_input


def execute(img, f1, f2, number_type=int):
    data_type = np.uint8
    color_model = 'RGB'

    factor = safe_number_input(number_type, 0.5)
    result = Image.fromarray(one_step_resampling(
        img, factor, f1, f2).astype(data_type), color_model)

    return result


images = {
   'Uzumaki': 'uzumaki.png',
   'Figures':'sample.png'
}


operation_classes = {
    'Интерполяция': 'int',
    'Децимация': 'dec',
    'Двухпроходная передискретизация': 'two',
    'Однопроходная передискретизация': 'one'
}

if __name__ == '__main__':
    print('Выберите изображение:')
    selected_image = prompt(images)
    img = image_to_np_array(selected_image)

    print('Выберите операцию:')
    selected_operation = prompt(operation_classes)

    match selected_operation:
        case 'int':
            print('Введите целый коэффициент растяжения')
            result = execute(img, mul, lambda a, b: int(round(a / b)))

        case 'dec':
            print('Введите целый коэффициент сжатия')
            result = execute(img, lambda a, b: int(round(a / b)), mul)

        case 'two':
            print('Введите целый коэффициент растяжения')
            numerator = safe_number_input(int, 1)

            print('Введите целый коэффициент сжатия')
            denominator = safe_number_input(int, 1)

            args = [numerator, denominator]
            result = Image.fromarray(
                two_step_resampling(img, *args).astype(np.uint8),
                'RGB')

        case 'one':
            print('Введите дробный коэффициент растяжения/сжатия')
            result = execute(img, lambda a, b: int(round(a * b)),
                             lambda a, b: int(round(a / b)), float)

        case _:
            exit()

    print('Введите название сохраненного изображения (оставьте пустым, чтобы \
не сохранять)')
    selected_path = input()
    if selected_path:
        result.save(path + '\\pictures_results\\' + selected_path)
