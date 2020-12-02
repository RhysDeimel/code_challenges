def get_inputs(file):
    with open(file, "r") as fd:
        lines = fd.readlines()
        return [int(num) for num in lines]

# >>> from itertools import combinations
# >>> L = [1, 2, 3, 4]
# >>> [",".join(map(str, comb)) for comb in combinations(L, 3)]
# ['1,2,3', '1,2,4', '1,3,4', '2,3,4']