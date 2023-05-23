# Лабораторная работа №4. Выделение контуров в изображениях.
Использовались оператор Шарра и градиентная матрица $`G = |G_x| + |G_y|`$
## Рисунок ручной отрисовки
Исходное изображение:
![](pictures_src/house_semitone.bmp)

Градиент по Х:
![](pictures_results/house_grad_x.bmp)

Градиент по Y:
![](pictures_results/house_grad_y.bmp)

Градиентная матрица G:
![](pictures_results/house_grad_g.bmp)

Бинаризованная градиентная матрица G(Бернсен):
![](pictures_results/house_grad_g_b.bmp)

Бинаризованная градиентная матрица G(Глобальная бинаризация, порог 25):
![](pictures_results/house_bin_25.bmp)

## Фото шахматной доски
Исходное изображение:

![](pictures_src/chess_semitone.bmp)

Градиент по Х:

![](pictures_results/chess_grad_x.bmp)

Градиент по Y:

![](pictures_results/chess_grad_y.bmp)

Градиентная матрица G:

![](pictures_results/chess_grad_g.bmp)

Бинаризованная градиентная матрица G(Бернсен):

![](pictures_results/chess_grad_g_b.bmp)

Бинаризованная градиентная матрица G(Глобальная бинаризация, порог 40):

![](pictures_results/chess_bin_40.bmp)

## Фото человеческого лица
Исходное изображение:

![](pictures_src/face_semitone.bmp)

Градиент по Х:

![](pictures_results/face_grad_x.bmp)

Градиент по Y:

![](pictures_results/face_grad_y.bmp)

Градиентная матрица G:

![](pictures_results/face_grad_g.bmp)

Бинаризованная градиентная матрица G(Бернсен):

![](pictures_results/face_bernsen.bmp)

Бинаризованная градиентная матрица G(Глобальная бинаризация, порог 45):

![](pictures_results/face_bin_45.bmp)


## Кадр из аниме
Исходное изображение:

![](pictures_src/tsukyo_semitone.bmp)

Градиент по Х:

![](pictures_results/tsukyo_grad_x.bmp)

Градиент по Y:

![](pictures_results/tsukyo_grad_y.bmp)

Градиентная матрица G:

![](pictures_results/tsukyo_grad_g.bmp)

Бинаризованная градиентная матрица G(Бернсен):

![](pictures_results/tsukyo_grad_g_b.bmp)

Бинаризованная градиентная матрица G(Глобальная бинаризация, порог 30):

![](pictures_results/tsukyo_bin_30.bmp)

## Выводы
Алгоритм выделения контуров оператором Шарра хорошо себя показывает для векторных и мультяшных изображений, но не очень хорошо работает для фотографий с изображениями людей и рукописным текстом. Однако его не стоит использовать в случае если бинаризованное изображение получено методом Бернсена (для
всех изображений видно, что выделение контуров намного лучше работает при глобальной пороговой бинаризации).
