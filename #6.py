def correct_message(message: str) -> str:
    return message[:160]


if __name__ == '__main__':
    print(correct_message(input('Введите сообщение: ')))