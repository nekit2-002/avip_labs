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


images = {
    'debian': 'debian.png',
    'figures': 'figures.png'
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
    args = []
    color_model = 'RGB'
    data_type = np.uint8

    print('Выберите операцию:')
    selected_operation = prompt(operation_classes)

    match selected_operation:
        case 'int':
            print('Введите целый коэффициент растяжения')
            factor = safe_number_input(int, 1)
            args = [factor]
            result = Image.fromarray(one_iteration_discretization(
                img, factor, lambda a, b: a * b, lambda a, b: int(round(a / b))).astype(data_type), color_model)

        case 'dec':
            print('Введите целый коэффициент сжатия')
            factor = safe_number_input(int, 1)
            args = [factor]
            result = Image.fromarray(one_iteration_discretization(img, factor, lambda a, b: int(
                round(a / b)), lambda a, b: a * b).astype(data_type), color_model)

        case 'two':
            print('Введите целый коэффициент растяжения')
            numerator = safe_number_input(int, 1)

            print('Введите целый коэффициент сжатия')
            denominator = safe_number_input(int, 1)

            args = [numerator, denominator]
            result = Image.fromarray(
                two_iteration_discretization(img, *args).astype(data_type))
        case 'one':
            print('Введите дробный коэффициент растяжения/сжатия')
            factor = safe_number_input(float, 0)
            args = [factor]

            result = Image.fromarray(one_iteration_discretization(
                img, factor, lambda a, b: int(round(a * b)), lambda a, b: int(round(a / b))).astype(data_type), color_model)
        case _:
            result = Image.fromarray(one_iteration_discretization(
                img, [2], lambda a, b: a * b, lambda a, b: int(round(a / b))).astype(data_type), color_model)

    print('Введите название сохраненного изображения (оставьте пустым, чтобы \
          не сохранять)')
    selected_path = input()
    if selected_path:
        result.save(path.join('pictures_results', selected_path))
