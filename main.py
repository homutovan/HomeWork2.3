valid_symbol = {'+': [2, lambda oper1, oper2: oper1 + oper2], 
                '-': [2, lambda oper1, oper2: oper1 - oper2], 
                '*': [3, lambda oper1, oper2: oper1 * oper2], 
                '/': [3, lambda oper1, oper2: oper1 / oper2]}

str_in = input('Введите арифметическое выражение в форме префиксной нотации:\n').split()

try:
    str_in[2]
    if len(str_in) > 3:
        a = b

    valid_symbol[str_in[0]]

    print(f'Результат вычисления: {valid_symbol[str_in[0]][1](int(str_in[1]), int(str_in[2]))}')

except NameError:
    print('Введенное выражение содержит более 3 символов')

except IndexError:
    print('Введенное выражение содержит менее 3 символов')

except KeyError:
    print('Первая операция отсутствует в списке доступных операций')

except ZeroDivisionError:
    print('Введенное выражение предусматривает деление на 0, проверьте порядок следования операндов')

except ValueError:
    print('В качестве операндов возможно использовать только числа')

finally:
    print('Введите новое выражение:')