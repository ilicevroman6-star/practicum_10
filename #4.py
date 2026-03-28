def make_payment(payment: int) -> None:
    if 20 <= payment <= 1000:
        print('Успех')
    else:
        print('Повторите попытку')


if __name__ == '__main__':
    try:
        make_payment(int(input()))
    except ValueError:
        print('Повторите попытку')