module_name = 'example'
word = 'приз'


def get_answer(word, attempt):
    matched, exact = 0, 0
    for i, letter in enumerate(attempt):
        if letter in word:
            matched += 1
        if letter == word[i]:
            exact += 1
    return matched, exact


def main(module_name, word):
    print(f'[sys]: Загадано слово "{word}"')

    bot = __import__(module_name)
    print(f'[sys]: Загружен модуль "{module_name}" '
          f'(имя должно быть транслитом фамилии)\n')

    length = len(word)
    attempt = bot.start(length)
    print(f'[run]: >> Вызвана функция `start({length})`, '
          f'где {length} - длина загаданного слова')
    print(f'[bot]: << Бот ответил первой попыткой: "{attempt}"\n')

    attempts_count = 1
    while attempt != word:
        print(f'[sys]: Бот ещё не отгадал слово, считаем для него ответ.')

        match, exact = get_answer(word, attempt)
        print(f'[sys]: Получили `match = {match}` и `exact = {exact}`\n')

        attempt = bot.next_move(match, exact)
        print(f'[run]: >> Вызвана функция `next_move({match}, {exact})`')
        print(f'[bot]: << Бот ответил следующей попыткой: "{attempt}"\n')

        attempts_count += 1
        print(f'[sys]: Нарастили счётчик попыток, теперь их {attempts_count}')

    return attempts_count


if __name__ == '__main__':
    attempts_count = main(module_name, word)
    print(f'[sys]: Бот отгадал слово "{word}" за {attempts_count} ход(а) :)')
