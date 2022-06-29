def get_unique_loto(num):
    import numpy as np
    loto_arange = np.arange(1,101)
    list_loto = list()
    for i in range(num):
        list_loto.append(np.random.choice(loto_arange, size=(5,5), replace = False))
    list_loto = np.array(list_loto)
    print(list_loto)
    return list_loto

get_unique_loto(2)