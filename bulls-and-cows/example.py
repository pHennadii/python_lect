import random


all_attempts = ['приз', 'стол', 'карп', 'пирс']


def _get_next_attempt():
    next_attempt = random.choice(all_attempts)
    all_attempts.remove(next_attempt)
    return next_attempt


def start(length):  # на вход получаем длину слова
    first_attempt = _get_next_attempt()
    return first_attempt  # первый ход


def next_move(match, exact):  # на вход получаем ответ с прошлого хода
    next_attempt = _get_next_attempt()
    return next_attempt  # следующий ход
