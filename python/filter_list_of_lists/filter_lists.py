# Filter a list of lists, such that only the highest earning surname will be returned.

ANP = [
    ["Steve", "Peterson", 101229],
    ["Mary", "Peterson", 111029],
    ["Mark", "Williams", 99118]
]


def filterlist(inpt):
    xdict = {}
    op = []
    for i in inpt:
        try:
            if xdict[i[1]] < i[2]:  # check with an added key
                xdict[i[1]] = i[2]
        except KeyError as _: 
            xdict[i[1]] = i[2]  # add if key does not exist already

    for i in inpt:
        if i[2] == xdict[i[1]]:
            op.append(i)
            print("ai caramba")
    return op


print(filterlist(ANP))