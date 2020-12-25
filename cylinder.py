import itertools
OPS = "-+/*-+/*-+"
EQU = ">=>=<=>=<="

def one_string(pos_list):
    """Take list of position of all 6 rings."""
    output = str(pos_list[0]) # digit
    output += OPS[pos_list[1]]
    output += str(pos_list[2])
    output += EQU[pos_list[3]]
    output += str(pos_list[4])
    output += str(pos_list[5])
    return(output)

print(one_string([1,2,3,4,5,6]))

