import itertools
import random

random.seed(3)

RINGS = "gtscfrle ylotriae aolesifc etrbwsoh".split()
N_DISC = len(RINGS)  # probably 4
LETTERS_PER_DISC = len(RINGS[0])  # probably 8

FOUR_LETTER_WORDS = []
with open('fourletter.txt') as fh:
    for line in fh:
        line = line.strip()
        FOUR_LETTER_WORDS.append(line)


def all_pos_lists():
    for p in itertools.product(range(LETTERS_PER_DISC), repeat=N_DISC):
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


def count_valid_words(word_list):
    n = 0
    matches = []
    for w in word_list:
        if w in FOUR_LETTER_WORDS:
            n += 1
            matches.append(w)
    return n, matches


for i in all_pos_lists():
    wl = pos_list_to_word_list(i)
    n, ml = count_valid_words(wl)
    if n > 1:
        wl.sort()
        ml.sort()
        print(n, wl, ml)
