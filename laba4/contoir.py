# # 1 + (6 - 1)%10 == 6 --> Sharr operator
from bernsen import np
from bernsen import bernsen_threshold
from typing import Literal


operators = {
    'x': np.array(
        [[3, 0, -3],
         [10, 0, -10],
         [3, 0, -3]]
    ),
    'y': np.array(
        [[3, 10, 3],
         [0, 0, 0],
         [-3, -10, -3]]
    )
}


if __name__ == '__main__':
    pass
