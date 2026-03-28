def letters(sentence: str) -> None:
    vowels = 'аеёиоуыэюя'
    consonants = 'бвгджзйклмнпрстфхцчшщ'
    cnt_vowels = 0
    cnt_consonants = 0

    for symbol in sentence:
        if symbol.lower() in vowels:
            cnt_vowels += 1
        elif symbol.lower() in consonants:
            cnt_consonants += 1

    print('Количество гласных:', cnt_vowels)
    print('Количество согласных:', cnt_consonants)


if __name__ == '__main__':
    letters(input())