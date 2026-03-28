from math import sqrt


def simple_number(number: int) -> bool:
    dividers = []

    if number == 1:
        return False

    else:
        for numeral in range(2, round(sqrt(number)) + 1):
            if number % numeral == 0:
                dividers.append(numeral)

        if len(dividers) == 0:
            return True

        else:
            return False


if __name__ == '__main__':
    try:
        n = int(input('Простые числа до '))

        for _ in range(1, n + 1):
            if simple_number(_):
                print(_)
    except ValueError:
        print('Введите натуральное число n')