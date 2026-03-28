def common_multiples(a: int, b: int, n: int) -> None:
    result = []

    if a > 0 and b > 0 and n > 0:
        for number in range(1, n+1):
            if number % a == 0 and number % b == 0:
                result.append(number)
        print(result)

    else:
        print('Числа не соответствуют условию')


if __name__ == '__main__':
    try:
        number_1 = int(input())
        number_2 = int(input())
        limit = int(input())

        common_multiples(number_1, number_2, limit)
    except ValueError:
        print('Введите ЧИСЛА')