# 1 + (6 - 1)%10 == 6 --> Bernsen adaptive algorithm (modified)
from semitone import semitone
from semitone import np
from integral import integral_image

def sum_in_frame(integral_img: np.array, x: int, y: int, frame_size: int):
    # print(integral_img.shape)
    len = integral_img.shape[1] - 1
    hight = integral_img.shape[0] - 1

    half_frame = frame_size // 2
    above = y - half_frame - 1
    low = y + half_frame
    left = x - half_frame - 1
    right = x + half_frame
    
    A = integral_img[max(above, 0), max(left, 0)]
    B = integral_img[max(0, above), min(len, right)]
    C = integral_img[min(hight, low), max(left, 0)]
    D = integral_img[min(hight, low), min(right, len)]
    
    # print("Half frame", half_frame, "above", above, "low", low,"hight =", hight, "left", left, "right", right, "x =", x,"y =", y)
    if max(left + 1, 0) == 0 and max(above + 1, 0) == 0:
        return D
    elif max(left + 1, 0) == 0:
        return D - B
    elif max(above + 1, 0) == 0:
        return D - C
    
    return D - C - B + A

def culculate_mean(integral_image: np.array, x: int, y: int, frame_size):
    square = frame_size**2
    s = sum_in_frame(integral_image, x, y, frame_size)
    return s // square
 

def bernsen_threshold(image:np.array, frame_size: int, thres: int) -> np.array:
    if len(image.shape) == 3:
        image = semitone(image)

    res_img = np.empty_like(image)
    integral_img = integral_image(image)

    for x in range(image.shape[0]): # СТРОКА
        for y in range(image.shape[1]): # СТОЛБЕЦ
            # print("Строка --", x, "из ",image.shape[0],  "Столбец --", y, "из ",image.shape[1])
            mean = culculate_mean(integral_img, y, x, frame_size)
            if mean == 0:
                res_img[x, y] = 0
                continue

            # print(mean)
            res_img[x, y] = 0 if mean < thres else 255
    return res_img

if __name__ == '__main__':
    a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12],])
    print(a)
    # print(a[1, 2])
    # print(a.shape)
    print(integral_image(a))
    print(sum_in_frame(integral_image(a), 1, 0, 3))
    # print(culculate_mean(integral_image(a), 1, 0, 3))
