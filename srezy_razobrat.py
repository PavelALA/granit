def get_chess(a):
    import numpy as np
    zeros = np.zeros((a,a))
    zeros[1::2, ::2] = 1
    zeros[::2, 1::2] = 1
    print(zeros)
    return(zeros)
    

get_chess(4)