from tqdm import tqdm
import itertools
import random

random.seed(3)

RINGS = "gtscfrle ylotriae aolesifc etrbwsoh".split()
N_DISC = len(RINGS)  # probably 4
LETTERS_PER_DISC = len(RINGS[0])  # probably 8


def all_pos_lists():
    for p in tqdm(
            itertools.product(range(LETTERS_PER_DISC), repeat=N_DISC),
            total=LETTERS_PER_DISC ** N_DISC
    ):
        yield list(p)


def pos_list_to_word_list(pos_list):
    word_list = []
    for word_n in range(LETTERS_PER_DISC):
        offsets = [word_n] * N_DISC  # always like [0,0,0,0] or [7,7,7,7]
        final_indices = [sum(x) % LETTERS_PER_DISC for x in zip(pos_list, offsets)]
        word = ""
        for disc_n in range(N_DISC):
            word += RINGS[disc_n][final_indices[disc_n]]
        word_list += [word]
    return word_list


def count_valid_words(word_list):  # FIXME
    if random.random() < 0.001:
        return 2
    else:
        return 1


for i in all_pos_lists():
    wl = pos_list_to_word_list(i)
    n = count_valid_words(wl)
    if n > 1:
        print(n, wl)
