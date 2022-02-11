# import random
# import numpy as np
# import pandas as pd
import math
import algorithm3 as alg3
import PGRR
import OLHPGRR

def framework(S,groupDict,dict,budget,Ycardinality,delta,filepath,dimension,auctionMethod=None,randomiser=None):
    """

    :param S:  whole data
    :param groupDict: grouped indexes by the attribute to sum
    :param dict: all possible attributes' combinations (aka, domain) with arbitrary order
    :param budget:
    :param Ycardinality: size of the domain of attributes
    :param delta:
    :param filepath:
    :param dimension:
    :return:
    """
    if auctionMethod is None:
        #beginning of the auction
        p, q = procurement(S, budget, dimension)
        if (len(q))==0:
            print("0 selected")

        #end of the auction
    elif auctionMethod=="Greedy":
        p, q = greedyProcurement(S, budget, dimension)
        if (len(q)) == 0:
            print("0 selected")

    elif auctionMethod=="GR":
        p, q, epsilon = grProcurement(S, budget, dimension)
        if (len(q)) == 0:
            print("0 selected")
        for index in q:
            for j in dimension:
                S[index][1][j] = epsilon
    else:
        print("wrong auction method===========")
        p=[]
        q=[]
    print(len(q))
    with open(filepath, 'a+') as f:
        f.write("# of selected records:" + str(len(q)) + "\n")
        f.write("payment:" + str(p) + "\n")
        f.write("allocation:" + str(q) + "\n")
    if groupDict is None:
        # build the selected dataset
        cur_S = []
        for index in q:
            cur_S.append(S[index])
        if randomiser is None:
            fvalues = [0] * Ycardinality
            if len(S)!= 0:
                fvalue = alg3.queryMechanism(cur_S, delta, Ycardinality,dict,dimension)
                for i in range(Ycardinality):
                    fvalues[i] += fvalue[i]
            with open(filepath,'a+') as f:
                f.write("    selected:"+"{")
                for i in range(len(dict)):
                    f.write(str(dict[i])+":"+ str(fvalues[i]))
                    if i!=len(dict)-1:
                        f.write(", ")
                f.write("}\n")
            with open(filepath,'a+') as f:
                f.write("    total:"+"{")
                for i in range(len(dict)):
                    f.write(str(dict[i])+":"+ str(fvalues[i]/ len(q)*len(S)))
                    if i!=len(dict)-1:
                        f.write(", ")
                f.write("}\n")
        elif randomiser=="PGRR":
            if len(S) != 0:
                ansTable = PGRR.queryMechanism(cur_S, delta, Ycardinality, dict, dimension)
            else:
                print("len(S)==0")
                return
            with open(filepath, 'a+') as f:
                f.write("table without scaler:" +str(ansTable)+"\n")
                # for i in range(len(ansTable)):
                #     f.write(str(ansTable[i])+"\n")
        # elif randomiser=="PGRRgr":
        #     # print("PGRRgr!!!")
        #     if len(S) != 0:
        #         ansTable = PGRR.queryMechanismGr(cur_S, delta, Ycardinality, dict, dimension)
        #     else:
        #         print("len(S)==0")
        #         return
        #     with open(filepath, 'a+') as f:
        #         f.write("table without scaler:" +str(ansTable)+"\n")
        
        elif randomiser == "OLHPGRR":
            # print("group???",len(groupDict))
            if len(S) != 0:
                fvalues = OLHPGRR.queryMechanism(cur_S, delta, Ycardinality, dict, dimension)
            else:
                print("len(S)==0")
                return
            with open(filepath, 'a+') as f:
                f.write("    selected:" + "{")
                for i in range(len(dict)):
                    f.write(str(dict[i]) + ":" + str(fvalues[i]))
                    if i != len(dict) - 1:
                        f.write(", ")
                f.write("}\n")

            with open(filepath, 'a+') as f:
                f.write("    total:" + "{")
                for i in range(len(dict)):
                    f.write(str(dict[i]) + ":" + str((len(S)/float(len(q)))*fvalues[i]))
                    if i != len(dict) - 1:
                        f.write(", ")
                f.write("}\n")
    else:
       
        groupDict1={}
        
        for key in groupDict.keys():
            #generate cur S according to the auction results
            #groupDict[key]=set(groupDict[key]).intersection(q)
            #cur_S=[S[x] for x in groupDict[key]]
            cur_S=[S[x] for x in set(groupDict[key]).intersection(q)]
            #print(groupDict.keys())
            #begainning of the randomizer
            if randomiser is None:
                fvalues = [0] * Ycardinality
                if len(cur_S)!= 0:
                    fvalue = alg3.queryMechanism(cur_S, delta, Ycardinality,dict,dimension)
                    for i in range(Ycardinality):
                        fvalues[i] += fvalue[i]
                with open(filepath,'a+') as f:
                    f.write(str(key)+" kwh\n")
                    f.write("    selected:"+"{")
                    for i in range(len(dict)):
                        f.write(str(dict[i])+":"+ str(fvalues[i]))
                        if i!=len(dict)-1:
                            f.write(", ")
                    f.write("}\n")
                with open(filepath,'a+') as f:
                    f.write("    total:"+"{")
                    for i in range(len(dict)):
                        f.write(str(dict[i])+":"+ str(fvalues[i]/ len(q)*len(S)))
                        if i!=len(dict)-1:
                            f.write(", ")
                    f.write("}\n")
            elif randomiser == "PGRR":
                if len(cur_S) != 0:
                    ansTable = PGRR.queryMechanism(cur_S, delta, Ycardinality, dict, dimension)
                else:
                    print("len(S)==0")
                    continue
                with open(filepath, 'a+') as f:
                    f.write(str(key) + " kwh\n")
                    f.write("table without scaler:" + str(ansTable) + "\n")
##            elif randomiser == "PGRRgr":
##                if len(cur_S) != 0:
##                    ansTable = PGRR.queryMechanismGr(cur_S, delta, Ycardinality, dict, dimension)
##                else:
##                    print("len(S)==0")
##                    return
##                with open(filepath, 'a+') as f:
##                    f.write(str(key) + " kwh\n")
##                    f.write("table without scaler:" + str(ansTable) + "\n")
            
            elif randomiser == "OLHPGRR":
                # print("OLHPGRR")

                if len(cur_S) != 0:

                    fvalues = OLHPGRR.queryMechanism(cur_S, delta, Ycardinality, dict, dimension)
                else:
                    print("len(S)==0")
                    continue  # return
                with open(filepath, 'a+') as f:
                    f.write(str(key) + " kwh\n")
                    f.write("    selected:" + "{")
                    for i in range(len(dict)):
                        f.write(str(dict[i]) + ":" + str(fvalues[i]))
                        if i != len(dict) - 1:
                            f.write(", ")
                    f.write("}\n")
                with open(filepath, 'a+') as f:
                    f.write("    total:" + "{")
                    for i in range(len(dict)):
                        f.write(str(dict[i]) + ":" + str(fvalues[i] / len(q) * len(S)))
                        if i != len(dict) - 1:
                            f.write(", ")
                    f.write("}\n")


def grProcurement(S, budget, dimension):
    n = len(S)
    epsilons = []
    percosts = []
    for i in range(n):
        epsilon = 0
        for j in dimension:
            # epsilon=min(epsilon, S[i][1][j])    # set epsilon as this guy's min epsilon
            epsilon += S[i][1][j]   # the total privacy of owner i
        epsilons.append(epsilon)
        percost = S[i][2][0] / epsilon  # v in FairQuery
        percosts.append(percost)
    percosts_idx = sorted(range(n), key=lambda k: percosts[k])
    # print("percosts_idx: ", percosts_idx)
    # print(len(percosts), min(percosts), max(percosts))
    # print(sorted(percosts))
    # print("percosts: ", percosts)
    min_ep = math.inf
    # print(S[percosts_idx[0]][1])
    # print("min ep: ", min_ep)
    k = 0
    for i in range(n):
        index = percosts_idx[i]
        # print("i: ", index)
        min_ep_tmp = min_ep
        for j in dimension:
            min_ep_tmp = min(min_ep_tmp, S[percosts_idx[i]][1][j])
        # print("tmp: ", min_ep_tmp)
        if percosts[index] * min_ep_tmp * len(dimension) <= budget/(i+1):
            min_ep = min_ep_tmp
            # print("min: ", min_ep)
        else:
            k = i-1
            # print("break")
            break
    if k == 0:
        k = n-1  # the last index
    # print("k:", k)
    allocations = percosts_idx[: k+1]  # first k owners
    payments = [0] * len(S)
    if k < n-1:
        payment = min(budget/k+1, percosts[percosts_idx[k+1]] * min_ep * len(dimension))
        # print("pay1: ", budget / k + 1)
        # print(percosts[percosts_idx[k+1]], len(dimension))
        # print("pay2: ", percosts[percosts_idx[k + 1]] * min_ep * len(dimension))
    else:
        payment = min(budget / k+1, percosts[percosts_idx[-1]] * min_ep * len(dimension))
        # print("pay1: ", budget / k + 1)
        # print(percosts[percosts_idx[-1]], len(dimension))
        # print("pay2: ", percosts[percosts_idx[-1]] * min_ep * len(dimension))
    for index in allocations:
        payments[index] = payment
    # print("allocation: ", allocations)
    # print("payment: ", payments)
    # print(S[percosts_idx[32557]])
    return (payments, allocations, min_ep)


def greedyProcurement(S,budget,dimension):
    n=len(S)
    epsilons = []
    percosts = []
    for i in range(n):
        epsilon = 0
        for j in dimension:
            # epsilon=min(epsilon, S[i][1][j])    # set epsilon as this guy's min epsilon
            epsilon += S[i][1][j]
        epsilons.append(epsilon)
        percost = S[i][2][0] / epsilon
        percosts.append(percost)
    percosts_idx = sorted(range(n), key=lambda k: percosts[k])
    k = -1
    epsilon_selected = 0
    select = []

    for i in range(n):
        idx = percosts_idx[i]
        epsilon = epsilons[idx]
        theta = S[idx][2][0]
        if theta*(epsilon_selected + epsilon) < (epsilon * budget) or math.isclose(theta*(epsilon_selected + epsilon) ,(epsilon * budget)):
            k += 1
            epsilon_selected += epsilon
            select.append(idx)
        else:
            break

    if len(select) == n:
        kplus1 = percosts_idx[len(select) - 1]
    else:
        kplus1 = percosts_idx[len(select)]

    payments = [0] * len(S)
    allocations = []

    for indx in select:
        x = S[kplus1][2][0]* epsilons[indx] /(100* epsilons[kplus1])
        y = budget * epsilons[indx] / (100*epsilon_selected)
        payment = min(x, y)
        allocations.append(indx)
        payments[indx] = payment

    return (payments,allocations)


def procurement(S, budget,dimension):

    #get epsilons and percosts
    epsilons = []
    percosts = []
    for i in range(len(S)):
        # epsilon=math.inf
        epsilon=0
        for j in dimension:
            # epsilon=min(epsilon, S[i][1][j])    # set epsilon as this guy's min epsilon
            epsilon+=S[i][1][j]               #epsilon as sum
        epsilons.append(epsilon)

        percost=S[i][2][0]/epsilon
        percosts.append(percost)
    # print("epsilon: ", epsilons, "percosts: ", percosts)

    #istar be the maximum epsilon i in epsilons
    maxepsilon=max(epsilons)
    istar = epsilons.index(maxepsilon)  # the index of the max epsilon
    # print("istar: ", istar)

    percosts_idx = sorted(range(len(S)), key=lambda k: percosts[k])
    # print("percosts_idx: ", percosts_idx)

    k = -1
    kplus1=0
    epsilon_selected = 0.0
    select = []  # index of owners selected in line5
    for i in range(len(S)):
        idx = percosts_idx[i]

        if idx != istar:
            theta = S[idx][2][0]
            epsilon = epsilons[idx]

            if theta*(epsilon_selected + epsilon) < (epsilon * budget) or math.isclose(theta*(epsilon_selected + epsilon) ,(epsilon * budget)):
                # print(theta)
                # print((epsilon * budget))
                # print(epsilon_selected + epsilon)

                k += 1
                kplus1+=1
                epsilon_selected += epsilon
                select.append(idx)
            else:
                break
        else: continue
    if kplus1==istar: kplus1+=1

    # print("k: ", k, "select: ", select, "k+1: ", kplus1)

    payments = [0] * len(S)
    allocations = []
    if k == -1:
        return(payments, allocations)

    if epsilon_selected < epsilons[istar]:
        allocations.append(istar)
        payments[istar] = budget
    else:
        for indx in select:
            x = S[kplus1][2][0] * epsilons[indx]/(100*epsilons[kplus1])   #kplus1 over?
            y = (budget * epsilons[indx]) /(100*epsilon_selected)
            payment = min(x, y)
            allocations.append(indx)
            payments[indx] = payment
    return(payments, allocations)


if __name__ == '__main__':
    # parameters


    delta = 0.0001  # confidence parameter
    # S = [[[1, 20, 1000], [0,10000,10000], [100]],[[1, 20, 1000], [0,10000,10000], [100]],[[1, 20, 1000], [0,10000,10000], [100]],[[1, 20, 1000], [0,10000,10000], [100]], [[1, 20, 1000], [0,10000,10000], [100]], [[1, 20, 1000], [0,10000,10000], [100]],
    #     [[1, 30, 2000], [0,10000,10000], [100]], [[1, 30, 1000], [0,10000,10000], [100]],[[1, 30, 1000], [0,10000,10000], [100]],[[1, 30, 1000], [0,10000,10000], [100]]]

    S = [[[1, 20, 1000], [1,2,1], [100]],[[1, 20, 1000], [2,3,2], [100]],[[1, 20, 1000], [2,1,1], [100]], [[1, 20, 1000], [1,1,1], [100]]]
    budget = 100 *len(S)*1
    # Ycardinality = 4
    # sequence=[20,30]
    sequence = [(20, 1000), (30, 2000), (30, 1000), (20, 2000)]  # sequence of pairs
    print(len(sequence))
    for i in S:
        print(i[1], i[2])

    # p,q = grProcurement(S, 320, [0, 1, 2])
    # framework(S,budget,4,sequence,0.00001,"experiments//test.txt",[1,2],auctionMethod=="GR",repeatTimes=1)
