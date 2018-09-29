import numpy as np

# df = pd.read_csv("./")

# DOCSTRING

# Find the first repeated character in a string.
# input string is s


def firstrep(s):
    if s:
        s = s.lower()
        word = list(s)
        for i, c in enumerate(word):
            for j in word[i + 1:]:
                if c == j:
                    print("The first repeated character is", str.upper(c))
                    return c


firstrep("hellads")


# Filter a list of lists, such that only the highest earning surname will be returned.

ANP = [
    ["Steve", "Peterson", 101229],
    ["Mary", "Peterson", 111029],
    ["Mark", "Williams", 99118]
]


def filterlist(inpt):
    dict = {}
    op = []
    for i in inpt:
        try:
            if dict[i[1]] < i[2]:  # check with an added key
                dict[i[1]] = i[2]
        except:
            dict[i[1]] = i[2]  # add if key does not exist already

    for i in inpt:
        if i[2] == dict[i[1]]:
            op.append(i)
            print("ai caramba")
    return op


print(filterlist(ANP))


# open a file, count number of words,
# number of lines and frequency of each word

def get_fstat(f):
    allwords = []
    lcount = 0
    wcount = 0
    fn = open(f, "r")
    for line in fn:
        lcount += 1
        words = line.split()
        wcount += len(words)
        for word in words:
            word = word.strip().lower()
            if len(word) > 2:
                allwords.append(word)
    wdict = dict(zip(allwords, [allwords.count(i) for i in allwords]))
    wdict = sorted(wdict.items(), key=lambda x: x[1], reverse=True)
    return wdict


# op = get_fstat('/home/raz/Projects/practice/feed.txt')
# print("\n", op[:3])   # Display top 3



def firstNotRepeatingCharacter(s):
    arr = 26 * [0]
    tp = {}
    sd = {}
    for i, v in enumerate(s):
        sd[v] = i
        p = ord(v) - 97
        arr[p] += 1
        if arr[p] > 1:
            tp[v] = i
    print(tp, sd)
    c = {k: v for k, v in sd.items() if k not in tp}

    if len(c) > 0:
        return min(c, key=c.get)
    return "_"


print(firstNotRepeatingCharacter("abacabad"))
[a, b, c] = [[1, 5, 8], [11, 12, 13, 15], [21, 22, 23, 24]]


def findinLists(sl, n):
    for i in sl:
        if n <= i[len(i) - 1]:
            for k, v in enumerate(i):
                if v == n:
                    print("found in list", i,
                          "value {1} at index {0}".format(k, v))
                    return (k, v)


# findinLists([a, b, c], 22)

def firstDuplicate(a):
    for i in a:
        p = abs(i) - 1
        if a[p] < 0:
            print(p + 1)
            return p + 1
        a[p] = a[p] * -1
    return -1


def firstDuplicate1(a):  # also doubles as a shitty sorter
    arr = [0] * (len(a) + 1)
    max = (len(a))
    for i, v in enumerate(a):
        try:
            if arr[v - 1] == v:
                return v
            arr[v - 1] = v
        except IndexError:
            if arr[max] == 0:
                arr[max] = v
                max -= 1
    return -1


a = [1, 3, 6, 4, 4, 5, 9, 8]

# print(firstDuplicate1(a))

mat = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

desired = [[7, 4, 1],
           [8, 5, 2],
           [9, 6, 3]]


def rotateMatrix(mat):
    l1 = []
    r = len(mat)
    for m in range(r):  # because same ith from each list x3
        for i in reversed(range(r)):    # because down up i.e last element
            l1.append(mat[i][m])
    # generate len(row) steps and create r sub lists
    return [l1[i:i + r] for i in range(0, r * r, r)]


def rotateMatrix1(mat):
    l1 = []
    r = len(mat)
    m = 0
    while m < r:
        # because same ith from each list x3
        for i in reversed(range(r)):  # because down up i.e last element
            l1.append(mat[i][m])
        m += 1  # generate len(row) steps and create r sub lists
    return [l1[i:i + r] for i in range(0, r * r, r)]

# print(rotateMatrix1(mat) == desired)


def checkBST(root):  # Check if this is a binary search tree
    if root is None:
        return True  # if empty then you are done
    # Define stack with  [least-possible obj most-possible]
    stack = [(float('-inf'), root, float('+inf'))]
    while stack:
        mind, node, maxd = stack.pop()  # pops a tuple of three
        if not (mind < node.data < maxd):  # if the tuple set is not balanced return false
            return False
        if node.left is not None:  # Else add new entry to the stack
            # if left node is not null, left is now root left is always smaller than upper
            # thus node data is now maximum and min is unchanged
            stack.append((mind, node.left, node.data))
        if node.right is not None:  # if right node is not empty add it to stack
            # right is always greater than root so root is now new minimum
            # and max stays the same, and right is new root
            stack.append((node.data, node.right, maxd))
    return True


""" First word + secon word = third word , is true?
# words numeric representation should not start with 0 unless all are 0s

the output should be
isCryptSolution(crypt, solution) = true
"""
crypt = ["SEND", "MORE", "MONEY"]

solution = [['O', '0'],
            ['M', '1'],
            ['Y', '2'],
            ['E', '5'],
            ['N', '6'],
            ['D', '7'],
            ['R', '8'],
            ['S', '9']]


def isCryptSolution(crypt, solution):
    from collections import OrderedDict
    unz = list(zip(*solution))  # create pair of lists from input
    sol = dict(zip(list(unz)[0], list(unz)[1]))  # and then a dictionary
    d1 = OrderedDict()
    c = 0

    for i, word in enumerate(crypt):
        sums = ''
        for id, char in enumerate(word):
            print(id, char)
            if id == 0 and sol[char] == '0':
                c += 1
            sums += sol[char]
        d1[str(i) + word] = sums

    op = list(d1.items())
    sup = int(op[0][1]) + int(op[1][1])
    if sup == int(op[2][1]) and c == 0:
        return True
    elif c > 0:
        if all(len(op[i][1]) == 1 for i in range(3)):
            return True
    return False


lbls = [1, 0, 0, 1, 0]  # sum
scores = [0.6, 0.3, 0.1, .45, 0.55]
lpreds = [1, 0, 0, 1, 0]


# return list of (fpr, tpr) points..
def create_roc(scores, lbls):
    n = len(lbls)
    tmp = []
    for thrsh in range(0, 100, 10):
        tsp = sum(lbls)
        tn = (n - sum(lbls))
        tsum = 0
        fsum = 0
        thrsh = thrsh / 100

        for i, v in enumerate(lbls):  # [0, 0.3]
            print(thrsh, v, scores[i])
            if v == 1 and scores[i] > thrsh:
                tsum += 1
            elif v == 0 and scores[i] > thrsh:
                fsum += 1
        tmp.append([round((tsum / tsp), 2), round((fsum / tn), 3)])
    return tmp[:n + 1]


print(create_roc(scores, lbls))


def create_cfm(scores, labels):
    pass

# [[1.0, 1.0],     [1.0, 0.66], [1.0, 0.66], [1.0, 0.33],
# [1.0, 0.33], [0.5, 0.33]]


def get_reg_model(x, y):
    print("regression")
    x = np.array(x)
    y = np.array(y)
    n = len(x)

    x_m = np.mean(x)
    y_m = np.mean(y)
    ss_xy = np.sum(y * x - n * y_m * x_m)
    ss_xx = np.sum(x**2 - n * y_m * x_m)

    b0 = ss_xy / ss_xx
    b1 = y_m - b0 * x_m

    return [b0, b1]


thisText = "Amazon is amazing. "


def foo(text):
    dicy = {}
    list_text = text.split().strip().lowercase()
    for i in list_text:
        if i.isdigit() & len(i) < 3:
            pass
        else:
            dicy[i] += 1
    return zip(*dicy)
