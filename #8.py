import datetime


def correct_date(date: str) -> None:
    try:
        date = datetime.datetime.strptime(date, '%m/%d/%Y %H:%M:%S')
        date = date.strftime('%d.%m.%y %I:%M:%S %p')

        print(date)
    except ValueError:
        print('Используйте корректный формат: MM/DD/YYYY HR:MIN:SEC')


if __name__ == '__main__':
    correct_date(input())