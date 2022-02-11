import math
import random
import numpy as np
import xxhash


def queryMechanism(S,delta,Ycardinality,dic,dimension):
    # print(Ycardinality)
    # print(dimension)
    n = len(S)
    minepsilon = math.inf
    for i in range(n):
        for j in dimension:
            minepsilon=min(minepsilon,S[i][1][j])
    epsilon = minepsilon/100
    g = int(round(math.exp(epsilon))) + 1
    prob = math.exp(epsilon) / (math.exp(epsilon) + g - 1)

    perturbed_users = []
    seeds = np.random.randint(0, n, n)
    for i in range(n):
        strValue=""
        for j in dimension:
            strValue+=str(S[i][0][j])
        y = x = xxhash.xxh32(strValue, seed=seeds[i]).intdigest() % g  # hash value
        if random.random()> prob:
            y=random.choice(list(set(range(g))-{x}))
        perturbed_users.append(y)

    estimate_dist=[0]*Ycardinality
    f = []
    for i in range(n):
        for vidx in range(Ycardinality):
            x = xxhash.xxh32(str(dic[vidx]), seed=seeds[i]).intdigest() % g
            if perturbed_users[i] == x:
                estimate_dist[vidx] += 1

    for i in range(Ycardinality):
        f.append((2*(math.exp(epsilon)+1)*estimate_dist[i])/(math.exp(epsilon)-1) - (2*n)/(math.exp(epsilon)-1))
    return f


if __name__ == '__main__':
    pass
