from my_io import *
from contoir import sharr_operator
from my_io import Image

operations = {
    'Градиентная матрица Gx': 'x',
    'Градиентная матрица Gy': 'y',
    'Градиентная матрица G': 'g',
    'Бинаризованная градиентная матрица G': 'b',
}

images = {
    'Chess': 'chess_semitone.bmp',
    'Anime face': 'tsukyo_semitone.bmp'
}

if __name__ == '__main__':
    print('Выберите изображение:')
    selected_image = prompt(images)
    img = image_to_np_array(selected_image)

    print('Выберите вид обработки:')
    op = prompt(operations)

    result = Image.fromarray(sharr_operator(img, op), 'L')
    print('Введите название сохраненного изображения (оставьте пустым, чтобы \
не сохранять)')

    selected_path = input()
    if selected_path:
        result.save(path.join('pictures_results', selected_path))
