# вариант запроса Д
# вариант предметной области 17 : дирижёр - оркестр
from operator import itemgetter


class Dir:
    # дирижёр
    def __init__(self, id, fio, sal, orchestra_id):
        self.id = id
        self.fio = fio
        self.sal = sal
        self.orchestra_id = orchestra_id


class Orchestra:
    # оркестр
    def __init__(self, id, name):
        self.id = id
        self.name = name


class DirOrch:
    def __init__(self, orch_id, dir_id):
        self.orch_id = orch_id
        self.dir_id = dir_id


# оркестры
orchs = [
    Orchestra(1, "Военный оркестр"),
    Orchestra(2, "Симфонический оркестр"),
    Orchestra(3, "Эстрадный оркестр"),
    Orchestra(4, "Струнный оркестр")
]

# музыкальные композиции
dirs = [
    Dir(1, 'Петров', 25000, 1),
    Dir(2, 'Нагдимаев', 35000, 2),
    Dir(3, 'Саргсян', 45000, 2),
    Dir(4, 'Усынин', 35000, 3),
    Dir(5, 'Ибрагимов', 25000, 4),
]

comps_orchs = [
    DirOrch(1, 1),
    DirOrch(2, 2),
    DirOrch(3, 3),
    DirOrch(4, 3),
    DirOrch(5, 4),
]


def main():
    # соединение данных один-ко-многим
    one_to_many = [(c.fio, c.sal, o.name)
                   for o in orchs
                   for c in dirs
                   if c.orchestra_id == o.id]

    # соединение данных многие-ко-многим
    many_to_many_temp = [(o.name, co.orch_id, co.dir_id)
                         for o in orchs
                         for co in comps_orchs
                         if o.id == co.orch_id]

    many_to_many = [(c.fio, c.sal, orch_name)
                    for orch_name, orch_id, comp_id in many_to_many_temp
                    for c in dirs if c.id == comp_id]

    print('Задание Д1')
    res1 = []
    for i in one_to_many:
        if i[0][-2:] == "ов":
            res1.append(i[0:3:2])
    print(res1)

    print('\nЗадание Д2')
    res2_unsorted = []
    for o in orchs:
        o_dirs = list(filter(lambda i: i[2] == o.name, one_to_many))
        if len(o_dirs) > 0:
            o_listeners = [listeners for _, listeners, _ in o_dirs]
            o_listeners_sum = sum(o_listeners)
            o_listeners_count = len(o_listeners)
            o_listeners_average = o_listeners_sum / o_listeners_count
            res2_unsorted.append((o.name, int(o_listeners_average)))
    res2 = sorted(res2_unsorted, key=itemgetter(1), reverse=True)
    print(res2)

    print('\nЗадание Д3')
    res3 = {}
    for o in orchs:
        if o.name[0] == "С":
            o_dirs = list(filter(lambda i: i[2] == o.name, many_to_many))
            o_dirs_fio = [x for x, _, _ in o_dirs]
            res3[o.name] = o_dirs_fio
    print(res3)


if __name__ == '__main__':
    main()
