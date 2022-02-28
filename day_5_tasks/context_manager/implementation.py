from contextlib import contextmanager


@contextmanager
def count_lines(path, mode='r', encoding='utf-8'):
    if mode == 'r' or mode == 'r+':
        """
        Если файл открыт только для чтения или для чтения и записи, печатается количество строк в этом файле. 
        """
        f = open(path, mode)
        all_file = [i.rstrip() for i in f.readlines()]
        print(len(all_file))
        yield f
        f.close()
    else:
        """
        При ином режиме доступа контекстный менеджер отрабатывает без изменений
        """
        f = open(path, mode)
        yield f
        f.close()


'''Test'''
with count_lines('../generators/task2/log.txt') as f:
    pass
