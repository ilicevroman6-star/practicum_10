import datetime


def correct_date(date: str) -> int | str:
    try:
        date = datetime.datetime.strptime(date, '%m/%d/%Y %H:%M:%S')
        year = date.year

        start_date = datetime.datetime(year, 1, 1, 0, 0, 0)
        delta = date - start_date

        return delta.days * 86400 + delta.seconds
    except ValueError:
        return 'Используйте корректный формат: MM/DD/YYYY HR:MIN:SEC'


if __name__ == '__main__':
    print(correct_date(input()))