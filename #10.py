def numbers_range(start: int, stop: int) -> None:
    digits = ['1', '3', '4', '8', '9']
    result = []

    if start <= stop:
        for number in range(start, stop+1):
            for i in range(len(str(number))):
                if str(number)[i] not in digits:
                    break

                if i == len(str(number)) - 1:
                    result.append(int(number))
        print(result)

    else:
        start, stop = stop, start
        numbers_range(start, stop)


if __name__ == '__main__':
    try:
        start_number = int(input())
        stop_number = int(input())
        numbers_range(start_number, stop_number)
    except ValueError:
        print('Введите числа')