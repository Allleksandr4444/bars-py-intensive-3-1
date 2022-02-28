def return_error(file):
    """
    Функция для возврата всех строк файла, которые содержат слово: error.
    """
    with open(file, 'r', encoding='utf-8') as f:
        all_file = [i.rstrip() for i in f.readlines()]
        for i in all_file:
            if 'ERROR' in i.upper():
                print(i)


# Test
print(return_error('log.txt'))
