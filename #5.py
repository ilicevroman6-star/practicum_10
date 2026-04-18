def card_cost(cost: int) -> int | str:
    '''
    calculates the cost
    '''
    
    if cost == 5 or cost == 10:
        return cost
    elif cost == 25:
        return cost + 3
    elif cost == 50:
        return cost + 8
    elif cost == 100:
        return cost + 20
    else:
        return 'Таких карт нет'


if __name__ == '__main__':
    try:
        print(card_cost(int(input())))
    except ValueError:
        print('Запишите стоимость числом')
