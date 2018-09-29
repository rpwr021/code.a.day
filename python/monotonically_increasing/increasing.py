def isgood(ls):
    try:
        if len(ls) < 2:
            return True
        for i,_  in enumerate(ls):
            if ls[i] < ls[(i + 1)]:
                pass
            else:
                return (i + 1)
    except IndexError as exp:
        print(exp)
    return True


def isincreasing(seq):
    count = 0

    isinc = isgood(seq)  # first run

    while count < 2:
        t1 = seq[:isinc] + seq[isinc + 1:]  # check for both n and n+1 removed
        t2 = seq[:isinc - 1] + seq[isinc:]
        count += 1
        isinc = what = isgood(t1)  # recheck
        if what is True:
            return True
        isinc = what = isgood(t2)
        if what is True:
            return True
    print("False")
    return False


seq = [10, 1, 3, 4, 3]


print(isincreasing(seq))