def final_price(cost: int, discount_card=False, holiday=False) -> str:
    '''
    calculates the final discount
    '''
    discount = 1.0

    if discount_card:
        discount *= 0.95

    if holiday:
        discount *= 0.97

    if 5000 <= cost < 15000:
        discount *= 0.97
    elif 15000 <= cost < 20000:
        discount *= 0.95
    elif 20000 <= cost < 30000:
        discount *= 0.93
    elif cost >= 30000:
        if holiday and discount_card:
            discount *= 0.85
        else:
            discount *= 0.9

    final_cost = cost * discount
    return f'{final_cost:.2f}'


if __name__ == '__main__':
    print(final_price(int(input())))
