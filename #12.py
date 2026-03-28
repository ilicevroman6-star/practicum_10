from math import degrees, acos
import turtle


def triangle(x: int, y: int, a: int, b: int, col_1: str, col_2: str) \
    -> None:
    """
    Draws an isosceles triangle from the left corner at the base

    :param x: the abscissa coordinate of the left corner at the base
    :param y: coordinate of the ordinate of the left angle at the base
    :param a: length of the side rib
    :param b: base length
    :param col_1: shape color
    :param col_2: outline color
    :return: None
    """

    if a <= 0 or b <= 0:
        raise ValueError(f"⚠️ Стороны должны быть положительными: a={a}, b={b}")


    if b >= 2 * a:
        raise ValueError(f"⚠️ Основание (b={b}) должно быть меньше 2a={2 * a} "
                         f"для построения треугольника")

    turtle.fillcolor(col_1)
    turtle.pencolor(col_2)
    turtle.begin_fill()

    turtle.up()
    turtle.goto(x, y)
    turtle.down()

    try:
        t1 = degrees(acos(b / (2 * a)))
        t2 = degrees(acos(1 - (b ** 2 / (2 * a ** 2))))
        turtle.forward(b)
        turtle.left(180 - t1)
        turtle.forward(a)
        turtle.left(180 - t2)
        turtle.forward(a)

    except Exception as f:
        print(f"❌ Ошибка при рисовании треугольника: {f}")

    finally:
        turtle.end_fill()
        turtle.up()
        turtle.home()

def parallelogram(x: int, y: int, a: int, b: int, col_1: str, col_2: str) \
    -> None:
    """
    Draws a parallelogram with 60° and 120° angles.

    :param x: x-coordinate of the starting point (bottom-left corner)
    :param y: y-coordinate of the starting point (bottom-left corner)
    :param a: length of the first side (horizontal side)
    :param b: length of the second side (slanted side)
    :param col_1: fill color
    :param col_2: outline color
    :return: None
    """

    if a <= 0 or b <= 0:
        raise ValueError("⚠️ Параллелограмм не нарисован: стороны должны быть "
              f"положительными (a={a}, b={b})")

    turtle.fillcolor(col_1)
    turtle.pencolor(col_2)
    turtle.begin_fill()

    turtle.up()
    turtle.goto(x, y)
    turtle.down()

    try:
        turtle.forward(a)
        turtle.left(60)
        turtle.forward(b)
        turtle.left(120)
        turtle.forward(a)
        turtle.left(60)
        turtle.forward(b)

    except Exception as r:
        print(f"❌ Ошибка при рисовании параллелограмма: {r}")

    finally:
        turtle.end_fill()
        turtle.up()
        turtle.home()

def square(x: int, y: int, a: int, col_1: str, col_2: str) -> None:
    """
    Draws a square.

    :param x: x-coordinate of the bottom-left corner
    :param y: y-coordinate of the bottom-left corner
    :param a: side length
    :param col_1: outline color
    :param col_2: fill color
    :return: None
    """

    if a <= 0:
        raise ValueError(f"⚠️ Сторона квадрата должна быть положительной: "
                         f"a={a}")

    turtle.up()
    turtle.setposition(x, y)
    turtle.down()

    turtle.pencolor(col_1)
    turtle.fillcolor(col_2)
    turtle.begin_fill()

    try:
        for i in range(4):
            turtle.forward(a)
            turtle.left(90)

    except Exception as j:
        print(f"❌ Ошибка при рисовании квадрата: {j}")

    finally:
        turtle.end_fill()
        turtle.up()
        turtle.home()

def ornament() -> None:
    for _ in range(12):
        parallelogram(-300 + 50 * _, -200, 30, 30,
                      'LightSeaGreen', 'DimGray')
    for _ in range(12):
        triangle(-285 + 50 * _, -170, 38, 30,
                 'CornflowerBlue', 'DarkSlateGray')

    for _ in range(12):
        parallelogram(-300 + 50 * _, 200, 30, 30,
                      'LightSeaGreen', 'DimGray')

    for _ in range(12):
        turtle.left(180)
        triangle(-270 + 50 * _, 195, 38, 30,
                 'CornflowerBlue', 'DarkSlateGray')

    for _ in range(3):
        square(-300 + 202 * _, -100, 200, 'Black', 'Indigo')

    turtle.fillcolor('Yellow')
    turtle.pencolor('Red')
    turtle.begin_fill()

    turtle.up()
    turtle.goto(0, -100)
    turtle.down()
    turtle.circle(100)

    turtle.end_fill()


if __name__ == '__main__':
    try:
        turtle.hideturtle()
        turtle.tracer(False)

        ornament()

        turtle.update()
        turtle.done()

    except ValueError as e:
        print(e)