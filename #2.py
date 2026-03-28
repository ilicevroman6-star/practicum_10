def fibonacci(number: int) -> list:
    fibonacci_numbers = []

    for nmb in range(1, number+1):
        if nmb == 1 or nmb == 2:
            fibonacci_numbers.append(1)
        else:
            result = (fibonacci_numbers[nmb - 2] +
                      fibonacci_numbers[nmb - 3])
            fibonacci_numbers.append(result)

    return fibonacci_numbers


if __name__ == '__main__':
    print(fibonacci(int(input())))