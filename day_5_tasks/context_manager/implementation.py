from contextlib import contextmanager


@contextmanager
def count_lines(path, mode='r', encoding='utf-8'):
    if mode == 'r' or mode == 'r+':
        """
        Если файл открыт только для чтения или для чтения и записи, печатается количество строк в этом файле. 
        """
        file_open = open(path, mode)
        print('Количество строк в файле:', len(file_open.readlines()))
        yield file_open
        file_open.close()
    else:
        """
        При ином режиме доступа контекстный менеджер отрабатывает без изменений
        """
        file_open = open(path, mode)
        yield file_open
        file_open.close()


# Test
with count_lines('../generators/task2/log.txt') as f:
    pass
