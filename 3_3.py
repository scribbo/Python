def thesaurus(*args):

    my_dict = {}

    for i in range(len(args)):
        if my_dict.get(args[i][0]) is not None:
            list = my_dict[args[i][0]]
            list.append(args[i])
            my_dict.update({args[i][0]: list})
        else:
            my_dict.update({args[i][0]: [args[i]]})

    return my_dict


print(thesaurus("Иван", "Харитон", "Мария", "Петр", "Илья"))


def sort_dict(dict_init):
    dict_sorted = {}
    list_keys = list(dict_init.keys())
    list_keys.sort()
    for i in list_keys:
        dict_sorted.update({i: dict[i]})
    print(dict_sorted)


sort_dict(thesaurus("Иван", "Харитон", "Мария", "Петр", "Илья"))

