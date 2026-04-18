def correct_message(message: str) -> str:
    '''
    message is the original text
    '''
    return message[:160]


if __name__ == '__main__':
    print(correct_message(input('Введите сообщение: ')))
