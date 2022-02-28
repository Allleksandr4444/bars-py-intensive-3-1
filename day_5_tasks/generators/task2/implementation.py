def return_error(file):
    """
    Функция для возврата всех строк файла, которые содержат слово: error.
    """

    with open(file, 'r', encoding='utf-8') as file_open:
        all_file = (i.rstrip() for i in file_open.readlines())
        for i in all_file:
            if 'ERROR' in i.upper():
                yield i


# Test
file = return_error('log.txt')

for line in file:
    print(line)
