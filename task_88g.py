def task_88g():
    str_num = input('Enter your number: ')
    try:
        if not str_num.isdigit():
            raise ValueError
        str_num = f'1{str_num}1'
        print(str_num)
        return int(str_num)
    except ValueError:
        print('Please, enter a number next time')
        return None
