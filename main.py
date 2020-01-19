valid_symbol = {'(': [1],
                ')': [0], 
                '+': [2, lambda oper1, oper2: oper1 + oper2], 
                '-': [2, lambda oper1, oper2: oper1 - oper2], 
                '*': [3, lambda oper1, oper2: oper1 * oper2], 
                '/': [3, lambda oper1, oper2: oper1 / oper2]}

def two_operands():

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

    return None

def multiple_operands():

    #notation = input('Введите арифметическое выражение в форме префиксной нотации:\n').split()

    in_string = '- * / 15 - 7 + 1 1 3 + 2 + 1 1' #Пример из Википедии

    notation = in_string.split()

    while len(notation) > 1:
        out_string = []
        digit = 0


        for symbol in notation:
          
            out_string.append(symbol)

            if symbol.isdigit():
                digit += 1
            else:
                digit = 0

            if digit == 2:
                operand2 = out_string.pop()
                operand1 = out_string.pop()
                operator = out_string.pop()

                new_symbol = int(valid_symbol[operator][1](int(operand1), int(operand2)))
                out_string.append(str(new_symbol))
                notation = out_string + notation[(len(out_string) + 2):]

                break
    
    print(f'Результат вычисления: {notation[0]}')  

    return None

def symbolic_solution():

    #notation = input('Введите арифметическое выражение в форме префиксной нотации:\n').split()

    in_string = '- * / 15 - 7 + 1 1 3 + 2 + 1 1' #Пример из Википедии

    #15 / (7 - (1 + 1)) * 3 - (2 + (1 + 1))

    notation = in_string.split()

    while len(notation) > 1:

        out_string = []
        operand2 = []
        operand1 = []
        digit = 0

        for symbol in notation:
          
            out_string.append(symbol)

            if symbol[0].isdigit():
                digit += 1
            else:
                digit = 0

            if digit == 2:
                operand2 = out_string.pop()
                operand1 = out_string.pop()
                operator = out_string.pop()

                try:
                    math_symbol = operand1 + operator + operand2
                
                except (IndexError, TypeError):
                    try:
                        math_symbol = operand1 + operator + operand2[1]
                    
                    except (IndexError, TypeError):
                        try:
                            math_symbol = operand1[1] + operator + operand2
                            
                        except (IndexError, TypeError):
                            math_symbol = operand1[1] + operator + operand2[1]
                
                if (valid_symbol[operator][0] < 3) and (len(notation)) != 3:
                    
                    math_symbol = '(' + math_symbol + ')'

                try:
                    new_symbol = int(valid_symbol[operator][1](int(operand1), int(operand2)))
                
                except (IndexError, TypeError):
                    try:
                        new_symbol = int(valid_symbol[operator][1](int(operand1[0]), int(operand2)))
                    
                    except (IndexError, TypeError):
                        try:
                            new_symbol = int(valid_symbol[operator][1](int(operand1), int(operand2[0])))
                            
                        except (IndexError, TypeError):
                            new_symbol = int(valid_symbol[operator][1](int(operand1[0]), int(operand2[0])))

                out_string.append([str(new_symbol), math_symbol])
                notation = out_string + notation[(len(out_string) + 2):]

                break

    print(f'Результат вычисления:{notation[0][1]} = {notation[0][0]}')

    return None

#two_operands()
#multiple_operands()
symbolic_solution()

