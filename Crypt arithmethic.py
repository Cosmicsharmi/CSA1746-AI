import itertools
import re
def solve_cryptarithmetic():
    puzzle = 'SEND + MORE == MONEY'
    letters = sorted(set(re.findall(r'[A-Z]', puzzle)))
    assert len(letters) <= 10, "Too many letters (more than digits)"
    for perm in itertools.permutations(range(10), len(letters)):
        letter_map = dict(zip(letters, perm))
        if letter_map['S'] == 0 or letter_map['M'] == 0:
            continue
        expr = puzzle.translate(str.maketrans({ch: str(letter_map[ch]) for ch in letters}))
        if eval(expr):
            print(f"Solved: {expr}")
            print("Mapping:")
            for k, v in letter_map.items():
                print(f"  {k} = {v}")
            return
    print("No solution found.")
solve_cryptarithmetic()
