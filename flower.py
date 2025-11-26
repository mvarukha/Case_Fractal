from turtle import *

import local_RU as RU


def draw_fractal_flower():
    FLOWER_PETAL_ANGLE = 60
    FLOWER_PETAL_COUNT = 12
    FLOWER_SIZE_FACTOR = 2.5
    INITIAL_X = 0
    INITIAL_Y = 0
    FLOWER_TURN_ANGLE = 360 / FLOWER_PETAL_COUNT

    def flower_rec(order: int, size: float) -> None:
        '''
        Draws a fractal flower with specified recursion depth and size.
        Args:
            order: Recursion depth for the fractal.
            size: Size of the flower components.
        Returns:
            None
        '''
        if order == 0:
            circle(size)
        else:
            for _ in range(FLOWER_PETAL_COUNT):
                circle(size)
                left(FLOWER_TURN_ANGLE)
                flower_rec(order - 1, size / FLOWER_SIZE_FACTOR)

    def setup_screen() -> None:
        speed(0)
        tracer(0, 0)

    try:
        print('=' * 40)
        recursion_depth = int(input(RU.CHOOSE_DEPTH_VARYA))
        if recursion_depth < 0:
            print(RU.INVALID_DEPTH)
            return
        print('=' * 40)
        flower_size = float(input(RU.CHOOSE_LEN))
        print('=' * 40)
        if flower_size <= 0:
            print(RU.INVALID_LEN)
            return
    except ValueError:
        print(RU.INVALID_ENTER)
        return
    print(RU.CREATING)

    setup_screen()
    up()
    goto(INITIAL_X, INITIAL_Y)
    down()
    flower_rec(recursion_depth, flower_size)
    update()
    done()
    exitonclick()

if __name__ == '__main__':

    draw_fractal_flower()
