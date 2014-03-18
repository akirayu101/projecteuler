
def gen_triangle_number_below(x):
    start = 1
    ret = start * (start + 1) / 2
    while ret < x:
        yield ret
        start += 1
        ret = start * (start + 1) / 2


def solution():
    ret = 0
    with open("words.txt") as f:
        line = f.read().strip().split(",")
        words = [i[1:-1] for i in line]
        len_max = max([len(i) for i in words])
        ts = gen_triangle_number_below(26 * len_max)
        t_dict = {}
        for t in ts:
            t_dict[t] = 1
        for word in words:
            if get_word_num(word) in t_dict:
                ret += 1
    return ret


def get_word_num(word):
    return sum(ord(w) - ord("A") + 1 for w in word)


print solution()
