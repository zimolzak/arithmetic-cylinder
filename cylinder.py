import itertools
from tqdm import tqdm

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
    try:
        return(eval(Se))
    except ZeroDivisionError:
        return(False)

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
    for p in tqdm(itertools.product(range(10), repeat=N_DISC), total  = 10**N_DISC):
        yield list(p)

if __name__ == '__main__':
    means = []
    configs_found = 0
    tot_configs = 10 ** N_DISC
    configs_list = []
    for p in all_pos_lists():
        SL, TFL = all_strings(p)
        mean = sum(TFL) / len(TFL)
        means.append(mean)
        if mean == 0.5:  # empirically, the max Pr is 0.5
            configs_list.append(SL)
            configs_found += 1
    print('\n'.join([str(e) for e in configs_list]))
    print('----')
    print('Max proportion correct', max(means))
    print('Found %d of %d at 0.5, chances %f' % (configs_found, tot_configs, configs_found / tot_configs))
    print('----\nHistogram:')
    for i in range(10):
        pr = i / 10
        count = means.count(pr)
        print(pr, count)
