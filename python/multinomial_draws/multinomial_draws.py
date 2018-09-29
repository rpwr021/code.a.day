from collections import Counter
import numpy as np 

probs = [0.17, 0.4, 0.32, .11]
events = 4


def rand_dist(n, probz):
    emp = np.zeros(n, dtype='int32')  # init empty results array
    vec = np.random.uniform(0, 1, n)
    probz = np.cumsum(probz)
    for i, v in enumerate(vec):
        for ix, p in enumerate(probz):
            if v > probz[ix] and v < probz[(ix + 1)]:
                # print((ix + 1), probz[ix], v ,probz[(ix + 1)])
                emp[i] = ix + 1
    emp = emp + 1  # for 0 labels
    return emp


obj = rand_dist(1000, probs)
print("\n", Counter(obj))
# print("", np.unique(obj, return_counts=True))
