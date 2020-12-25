import itertools
import random

OPS = "-+/*-+/*-+"
EQU = ">=>=<=>=<="
N_DISC = 6

def one_string(pos_list):
    """Take list of position of all 6 rings."""
    output = str(pos_list[0]) # digit
    output += OPS[pos_list[1]]
    output += str(pos_list[2])
    output += EQU[pos_list[3]]
    if str(pos_list[4]) != '0':
        output += str(pos_list[4])
    output += str(pos_list[5])
    return(output)

def simple_eval(expr_string):
    Se = expr_string.replace('=', '==')
    return(eval(Se))

def all_strings(pos_list):
    str_list = []
    TF_list = []
    for offset in range(10):
        offsetted_pos_list = [(e + offset) % 10 for e in pos_list]
        str_i = one_string(offsetted_pos_list)
        str_list.append(str_i)
        TF_list.append(simple_eval(str_i))
    return(str_list, TF_list)

def all_pos_lists():
    for p in itertools.product(range(10), repeat=N_DISC):
        yield list(p)

if __name__ == '__main__':
    for p in all_pos_lists():
        SL, TFL = all_strings(p)
        print(SL)
        print(TFL)
