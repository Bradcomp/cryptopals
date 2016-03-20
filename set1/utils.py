#compose :: (y -> z) -> (...) -> (b -> c) -> (a -> b) -> (a -> z)
def compose(*args):
    return lambda x: reduce(lambda acc, f: f(acc), reversed(args), x)

def letter_count(s):
    letters = sorted(s.lower())
    init = [[letters[0]]]
    def reducer(acc, l):
        if l == acc[-1][0]:
            acc[-1].append(l)
        else:
            acc.append([l])
        return acc
    letter_lists = reduce(reducer, letters[1:], init)
    return sorted([(l[0], len(l)) for l in letter_lists], key=lambda x: x[1] * -1)
