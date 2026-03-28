import turtle as t


def triangle(x1: int, y1: int, x2: int, y2: int, x3: int, y3: int, col: str) \
    -> None:
    t.fillcolor(col)
    t.begin_fill()

    t.up()
    t.setpos(x1, y1)
    t.down()

    t.setpos(x2, y2)
    t.setpos(x3, y3)
    t.setpos(x1, y1)

    t.end_fill()
    t.up()
    t.home()

def square(x1: int, y1: int, x2: int, y2: int, x3: int, y3: int,
           col_1: str, col_2: str, reverse=False) -> None:
    triangle(x1, y1, x2, y2, x3, y3, col_1)
    triangle(x2, y2, x2, y3, x3, y3, col_2)

    if reverse:
        triangle(x1, y1, x2, y2, x3, y3, col_1)
        triangle(x1, y1, x1, y3, x3, y3, col_2)

def design() -> None:
    colors = ['LightCyan', 'MediumTurquoise', 'SteelBlue']

    t.setpos(-150, 150)
    for row in range(6):
        t.setpos(-150, 150 - row * 50)
        for column in range(6):
            if row == column and row < 3:
                square(
                       -150 + 50 * column, 100 - 50 * column,
                       -100 + 50 * column, 100 - 50 * column,
                       -150 + 50 * column, 150 - 50 * column,
                       colors[1], colors[2]
                      )
            elif row == column and row >= 3:
                square(
                       -150 + 50 * column, 100 - 50 * column,
                       -100 + 50 * column, 100 - 50 * column,
                       -150 + 50 * column, 150 - 50 * column,
                       colors[2], colors[1]
                      )
            elif column == 5 - row and row >= 3:
                square(
                     100 - 50 * column, 100 - 50 * column,
                     150 - 50 * column, 100 - 50 * column,
                     150 - 50 * column, 150 - 50 * column,
                     colors[1], colors[2], reverse=True
                      )
            elif column == 5 - row and row < 3:
                square(
                     100 - 50 * column, 100 - 50 * column,
                     150 - 50 * column, 100 - 50 * column,
                     150 - 50 * column, 150 - 50 * column,
                     colors[2], colors[1], reverse=True
                      )
            elif (row == 1 and column == 0) or (row == 2 and column == 1):
                square(
                    -150 + 50 * column, 50 - 50 * column,
                    -100 + 50 * column, 50 - 50 * column,
                    -150 + 50 * column, 100 - 50 * column,
                    colors[0], colors[1]
                      )
            elif (row == 3 and column == 1) or (row == 4 and column == 0):
                square(
                    -150 + 50 * column, -100 + 50 * column,
                    -100 + 50 * column, -100 + 50 * column,
                    -100 + 50 * column, -50 + 50 * column,
                    colors[1], colors[0], reverse=True
                      )
            elif row == 2 and column == 0:
                square(
                    -150 + 50 * column, 50 * column,
                    -100 + 50 * column, 50 * column,
                    -150 + 50 * column, 50 + 50 * column,
                    colors[1], colors[0]
                     )
            elif row == 3 and column == 0:
                square(
                    -150 + 50 * column, -50 + 50 * column,
                    -100 + 50 * column, -50 + 50 * column,
                    -100 + 50 * column, 50 * column,
                    colors[0], colors[1], reverse=True
                     )
            elif row == 1 and column == 5:
                square(
                     50 + 50, 50,
                     100 + 50, 50,
                     100 + 50, 50 + 50,
                    colors[0], colors[1], reverse=True
                      )
            elif row == 2 and column == 4:
                square(
                     50, 0,
                     100, 0,
                     100, 50,
                    colors[0], colors[1], reverse=True
                      )
            elif row == 3 and column == 4:
                square(
                     50, -50,
                     100, -50,
                     50, 0,
                    colors[1], colors[0]
                      )
            elif row == 4 and column == 5:
                square(
                     100, -100,
                     150, -100,
                     100, -50,
                    colors[1], colors[0]
                      )
            elif row == 2 and column == 5:
                square(
                     100, 0,
                     150, 0,
                     150, 50,
                    colors[1], colors[0], reverse=True
                      )
            elif row == 3 and column == 5:
                square(
                     100, -50,
                     150, -50,
                     100, 0,
                    colors[0], colors[1]
                      )
            elif (row == 0 and column == 1) or (row == 1 and column == 2):
                square(
                    -100 + 50 * row, 100 - 50 * row,
                    -50 + 50 * row, 100 - 50 * row,
                    -100 + 50 * row, 150 - 50 * row,
                    colors[2], colors[1]
                      )
            elif (row == 0 and column == 4) or (row == 1 and column == 3):
                square(
                     50 * row, 50 + 50 * row,
                     50 + 50 * row, 50 + 50 * row,
                     50 + 50 * row, 100 + 50 * row,
                    colors[2], colors[1], reverse=True
                      )
            elif row == 0 and column == 2:
                square(
                     -50, 100,
                     0, 100,
                     -50, 150,
                    colors[1], colors[0]
                      )
            elif row == 0 and column == 3:
                square(
                     0, 100,
                     50, 100,
                     50, 150,
                    colors[1], colors[0], reverse=True
                      )
            elif row == 4 and column == 2:
                square(
                     -50, -100,
                     0, -100,
                     0, -50,
                    colors[1], colors[2], reverse=True
                      )
            elif row == 4 and column == 3:
                square(
                     0, -100,
                     50, -100,
                     0, -50,
                    colors[1], colors[2]
                      )
            elif row == 5 and column == 1:
                square(
                     -100, -150,
                     -50, -150,
                     -50, -100,
                    colors[1], colors[2], reverse=True
                      )
            elif row == 5 and column == 2:
                square(
                     -50, -150,
                     0, -150,
                     0, -100,
                    colors[0], colors[1], reverse=True
                      )
            elif row == 5 and column == 3:
                square(
                     0, -150,
                     50, -150,
                     0, -100,
                    colors[0], colors[1]
                      )
            elif row == 5 and column == 4:
                square(
                     50, -150,
                     100, -150,
                     50, -100,
                    colors[1], colors[2]
                      )


if __name__ == '__main__':
    t.hideturtle()
    t.tracer(False)

    design()

    t.update()
    t.done()