import random

NUMB_OF_DIGITS = 4
random_list = []
result = {}


def make_number():
    global random_list
    random_list = random.sample('0123456789', NUMB_OF_DIGITS)
    if random_list[0] == '0':
        random_list.append(random_list.pop(0))
    return random_list


def check_number(user_number):
    global result
    result = {'bulls': 0, 'cows': 0}
    for index, num in enumerate(user_number):
        if random_list[index] == num:
            result['bulls'] += 1
        elif num in random_list:
            result['cows'] += 1
    return result


def is_game_over():
    return result['bulls'] == NUMB_OF_DIGITS
