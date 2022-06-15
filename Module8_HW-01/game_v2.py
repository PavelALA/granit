"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
 # создаем функцию для поиска заданного числа по принципу "больше-меньше"
    limit_a = 1 #задаем нижнюю границу поиска
    count = 0 #создаем счетчик попыток
    limit_b = 101 #задаем верхнюю границу поиска
    predict = 0 # для первого входа в цикл задаем значение заведомо не равное number
    
    while number != predict:  
    # создем цикл поиска заданного числа по принципу "больше-меньше"
        count += 1
        predict = np.random.randint(limit_a, limit_b)
        if predict > number:
            limit_b = predict
                       
        elif predict < number:
            limit_a = predict
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
