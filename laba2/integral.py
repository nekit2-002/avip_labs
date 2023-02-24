from semitone import np 

def integral_image(img: np.array) -> np.array:
    integral_img = np.empty_like(img)
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

def sum_in_frame(integral_img: np.array, x: int, y: int, frame_size: int):
    len = integral_img.shape[0] - 1
    hight = integral_img.shape[1] - 1

    right = x + frame_size - 1
    low = y + frame_size - 1

    D = integral_img[min(low, hight), min(right, len)]
    if x <= 0 and y <= 0:
        return D
    
    C = integral_img[ min(low, hight), max(x - 1, 0)]
    if min(right, len) == len and y == 0:
        return D - C

    B = integral_img[max(0, y - 1), min(len, right)]
    if min(low, hight) == hight and x == 0:
        return D - B
    
    intersection = integral_img[max(y - 1, 0), max(x - 1, 0)]
    if min(low, hight) == hight and min(len, right) == len:
        print(B, C, D)
        D - C - B

    return D - C - B + intersection

if __name__ == '__main__':
    a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(a)
    print(integral_image(a))
    print(sum_in_frame(integral_image(a), 1, 1, 2))
