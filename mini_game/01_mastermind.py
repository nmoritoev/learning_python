# Игра «Быки и коровы»
# https://goo.gl/Go2mb9
#
# Правила:
# Компьютер загадывает четырехзначное число, все цифры которого различны
# (первая цифра числа отлична от нуля). Игроку необходимо разгадать задуманное число.
# Игрок вводит четырехзначное число c неповторяющимися цифрами,
# компьютер сообщают о количестве «быков» и «коров» в названном числе
# «бык» — цифра есть в записи задуманного числа и стоит в той же позиции,
#       что и в задуманном числе
# «корова» — цифра есть в записи задуманного числа, но не стоит в той же позиции,
#       что и в задуманном числе
#
# Например, если задумано число 3275 и названо число 1234,
# получаем в названном числе одного «быка» и одну «корову».
# Очевидно, что число отгадано в том случае, если имеем 4 «быка».


import mastermind_engine as me
from termcolor import cprint, colored

number_attempts = 0
me.make_number()
while True:
    user_number = input(colored('Введите свой вариант:', color='yellow'))
    if not user_number.isdigit():
        cprint('Вы ввели не число. Введите еще раз', color='red')
        continue

    if int(user_number[0]) == 0:
        cprint('Первая цифра числа должна быть отлична от нуля. Введите еще раз', color='red')
        continue

    if me.NUMB_OF_DIGITS != len(user_number):
        cprint('Вы ввели не корректное число. Введите еще раз', color='red')
        continue

    if len(set(user_number)) != len(user_number):
        cprint('вы ввели повторяющиеся цифры. Введите еще раз', color='red')
        continue

    me.check_number(user_number)
    cprint(me.result, color='blue')
    number_attempts += 1
    if me.is_game_over():
        cprint(f'Поздравляем вы выиграли!!! Колличество ходов - {number_attempts} ', color='cyan')
        replay_game = input(colored(f'Хотите сыграть еще раз? \n да/нет -', color='magenta'))
        if replay_game == 'да':
            me.make_number()
            number_attempts = 0
            continue
        else:
            cprint('Спасибо за игру! До свидания!)', color='cyan')
            break

