import math
import random
import numpy as np
import xxhash


def queryMechanism(S,delta,Ycardinality,dic,dimension):
    # print("Y: ", Ycardinality)
    # print("dim: ", dimension)
    # print(dic)
    # print(S)

    n = len(S)
    g = Ycardinality
    # minepsilon = math.inf
    # for i in range(n):
    #     for j in dimension:
    #         minepsilon=min(minepsilon,S[i][1][j])
    # epsilon = minepsilon/100
    # g = int(round(math.exp(epsilon))) + 1
    # prob = math.exp(epsilon) / (math.exp(epsilon) + g - 1)

    perturbed_users = []
    seeds = np.random.randint(0, n, n)
    # print("seeds: ", seeds)
    for i in range(n):
        epsilon = S[i][1][0]/100
        for dim in dimension:
            epsilon = min(epsilon, S[i][1][dim]/100)
        # print(epsilon)
        # print("S: ", S[0])
        # print("epsilon: ", epsilon)
        # g = int(round(math.exp(epsilon))) + 1
        prob = math.exp(epsilon) / (math.exp(epsilon) + g - 1)
        # print("pt: ", prob)
        strValue=""
        for j in dimension:
            strValue += str(S[i][0][j])
        y = x = xxhash.xxh32(strValue, seed=seeds[i]).intdigest() % g  # hash value
        # print(seeds[i])
        # print("hash 1: ", x)
        # print("hash 2: ", xxhash.xxh32(str((414)), seed=seeds[i]).intdigest() % g)
        # for i in range(len(dic)):
        #     if dic[i]
        if random.random() > prob:
            y = random.choice(list(set(range(g))-{x}))
        # print("y: ", y)
        perturbed_users.append(y)

    estimate_dist=[0]*Ycardinality
    # f = []
    # print(dic)
    for i in range(n):
        for vidx in range(Ycardinality):
            # print(dic[vidx][0])
            string = ""
            if dimension == [0, 2]:
                string = str(dic[vidx][0])+str(dic[vidx][1])
            elif dimension == [0]:
                string = str(dic[vidx])
            else:
                for index in dimension:
                    string += str(dic[vidx][index])
            # print(string)
            # print("str: ", string)
            # x = xxhash.xxh32(str(dic[vidx]), seed=seeds[i]).intdigest() % g   #this is wrong
            x = xxhash.xxh32(string, seed=seeds[i]).intdigest() % g
            # print(seeds[i])
            # print("hash: ", x)
            # print("hash 3: ", xxhash.xxh32(str((54)), seed=seeds[i]).intdigest() % g)
            # print("dic: ", str(dic[vidx]))
            if perturbed_users[i] == x:
                estimate_dist[vidx] += 1
        # print(seeds[i])
        # print("hash 4: ", xxhash.xxh32(str((414)), seed=seeds[i]).intdigest() % g)

    # ignore estimation
    # for i in range(Ycardinality):
    #     f.append((2*(math.exp(epsilon)+1)*estimate_dist[i])/(math.exp(epsilon)-1) - (2*n)/(math.exp(epsilon)-1))
    # print(estimate_dist)
    # print(len(estimate_dist))
    return estimate_dist


if __name__ == '__main__':
    pass