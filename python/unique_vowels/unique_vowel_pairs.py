# from a given line, find out how many vowels each word has then create a pair of words
# each word having its unique set of vowels (no repeats)

inp = "the quick brown fox jumps over the lazy dog"


def keep_vws(s):
    cnts = {}
    for w in s.lower().split():
        d = set()
        for c in w:
            if c in vws:
                d.add(c)
        cnts[w] = (len(d), d)
    # print(cnts)
    return cnts

def makepairs(inp):
    op = keep_vws(inp)
    # Faster convergence with sorted list
    op = sorted(op.items(), key=lambda x: x[1], reverse=True)
    k = 0
    for i, item in enumerate(op):
        # print(item[1], i, item)
        try:
            # item 0 is set of vowels
            # op is dictionary being iterated with enumerator key
            if item[1] != op[i + 1][1][1] and k < 3:
                print((op[i][0], op[i + 1][0], (op[i][1][0] + op[i + 1][1][0])))
                k += 1
        except IndexError:
            print(".")


makepairs(inp)
