#todo: Дан массив размера N. Найти минимальное растояние между одинаковыми значениями в массиве и вывести их индексы.
#todo: Написать условие которое убирает дубликаты вывода для одинаковых значений из массива
# Для числа 1 минимальное растояние в массиве по индексам: 0 и 7
# Для числа 2 минимальное растояние в массиве по индексам: 7 и 10
# Для числа 17 нет минимального растояния т.к элемент в массиве один.


mass = [1,2,17,1,54,30,89,2,1,6,2]
dict_indx = {}

def create_dict(index_one, index_two):
    len_ = index_two - index_one
    return {"index_one": index_one, "index_two": index_two, "len_": len_}

def create__list_of_dict(mass_index):
    result = []
    if len(mass_index) == 0 or len(mass_index) == 1:
        return None
    start = None
    for i in mass_index:
        if start is None:
            start = i
            continue
        end = i
        obj = create_dict(start, end)
        result.append(obj)
        start = end
    return result


def min_dict(list_dict):
   prev = None
   for dict_ in  list_dict:
       if prev is None:
           prev = dict_['len_']
           min_ = dict_['len_']
           min_dic = dict_
           continue
       curr = dict_['len_']
       if prev > curr:
           min_ = curr
           min_dic = dict_
       prev = min_
   # print(min_dic)
   return min_dic


end = len(mass)
for i in mass:
    if mass.count(i) > 1:
        start = 0
        mass_index = []
        for j in range(mass.count(i)):
            curr = mass.index(i, start, len(mass))
            mass_index.append(curr)
            start = curr + 1
        result = create__list_of_dict(mass_index)
        print(i)
        print(min_dict(result))
    else:
        pass
        # print("Нет пары")

