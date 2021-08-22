def task_88v():
    str_num = input('Enter your number: ')
    try:
        if len(str_num) == 1:
            print(str_num)
            return int(str_num)
        else:
            str_swapped = str_num[-1] + str_num[1:-1] + str_num[0]
            print(str_swapped)
            return int(str_swapped)
    except ValueError:
        print('Please, enter a number next time')
        return None
