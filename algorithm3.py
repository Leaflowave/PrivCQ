import math
import random
import numpy as np
import linecache
from scipy import sparse

def queryMechanism(S,delta,Ycardinality,dict,dimension):
    n=len(S)
    # print(Ycardinality)
    # print(dimension)

    tau=Ycardinality
    gamma=math.sqrt(math.log(2*tau/float(delta))/float(n))
    sigma=math.ceil(math.log(tau+1)*math.log(2/float(delta))/(gamma*gamma))

    matrixValue=1/float(math.sqrt(sigma))
    # if len(dimension)>=3:
    #     # with open("R.txt", 'w') as f:
    #     R=[]
    #     for i in range(sigma):
    #         # Ri = np.random.randint(0, 2, tau)
    #         # sparseRi = sparse.csr_matrix(Ri)
    #         Ri=np.random.choice(['0', '1'], (sigma, tau))
    #         # R.append(randomBooleanString(tau))
    #         R.append(''.join(Ri))
    #         # sparse.save_npz('npz//sparseR'+str(i)+'.npz', sparseRi)
    #             # f.write(str(list(sparseRi))+"\n")
    # else:
    # print(sigma)
    R=np.random.randint(0, 2, size=(sigma,tau))
    # R=np.random.choice([-matrixValue,matrixValue],(sigma,tau))

    z=[0]*sigma
    f=[0]*tau
    for idx in range(n):
        j=random.randint(0,sigma-1)
        # if len(dimension)<=2:
        zi=LocalRandomiser(R[j],S[idx][0],S[idx][1], tau,sigma,dict,dimension,matrixValue)   # LR(R_j., yi, epsiloni)
        # else:
        #     # print(j)
        #     # Rjstr = linecache.getline("R.txt", j + 1)
        #     # Rj=sparse.load_npz('npz//sparseR' + str(j+1) + '.npz')
        #     Rj=R[j]
        #     # Rj=eval(Rjstr)
        #     zi=LocalRandomiser(Rj,S[idx][0],S[idx][1], tau,sigma,dict,dimension,matrixValue)   # LR(R_j., yi, epsiloni)
        z[j]+=zi

    for k in range(tau):
        # ek = [0] * tau
        # ek[k] = 1
        # tmp=np.dot(R,np.transpose(ek))   #output: n by 1
        # tmp=R[:,k]
        for i in range(sigma):
            # if len(dimension)>2:
            #     if R[i][k]==1:
            #         t = matrixValue
            #     else:
            #         t = -matrixValue
            # else:
            if R[i,k]==1:
                t=matrixValue
            else:
                t=-matrixValue
            f[k] += z[i] * t
        # f[k]=np.dot(z,np.transpose(tmp))         #<Rc_k, z>  output: 1 by 1
    return f


def LocalRandomiser(Rj,yi,epsiloni100,tau,sigma,dict,dimension,matrixvalue):
    # print(epsiloni100)
    if len(dimension)==1:
        epsiloni=epsiloni100[dimension[0]]/100
        # epsiloni=epsiloni100[0]/100
    elif len(dimension)>=2:
        epsiloni=min([epsiloni100[x]/100 for x in dimension])
    # print(epsiloni)
    # find l_i of yi
    # dict=[(20,1000),(30,2000),(30,1000),(20,2000)]  #sequence of pairs

    # l_i=dict.index((yi[0],yi[2]))
    if len(dimension)==1:
        l_i=dict.index(yi[dimension[0]])
    # modified by Weidong
    elif len(dimension)==2:
        l_i=dict.index((yi[dimension[0]],yi[dimension[1]]))
    elif len(dimension) == 3:
        l_i = dict.index((yi[dimension[0]], yi[dimension[1]],yi[dimension[2]]))
    # ei=[0]*tau
    # ei[l_i]=1
    # if len(dimension)>2:
    #     if eval(Rj[l_i])==1:
    #         xi = matrixvalue
    #     else:
    #         xi = -matrixvalue
    # else:
    if Rj[l_i]==1:
        xi=matrixvalue
    else:
        xi=-matrixvalue
    # xi=Rj[l_i]
    # xi=np.dot(Rj,np.transpose(ei))
    # if type(epsiloni) is not list:
    p=math.exp(epsiloni)/(math.exp(epsiloni)+1)
    ci=(math.exp(epsiloni)+1)/(math.exp(epsiloni)-1)
    # elif len(epsiloni)==2:
    #     p = (1+math.exp(epsiloni[0]+epsiloni[1])) / ((math.exp(epsiloni[0]) + 1)*(math.exp(epsiloni[1])+1))
    #     ci =((math.exp(epsiloni[0]) + 1)*(math.exp(epsiloni[1])+1)) / ((math.exp(epsiloni[0]) - 1)*(math.exp(epsiloni[1])-1))
        #sigma may not appropriate
    if random.random()<=p:
        zi=ci*sigma*xi
        # zi=xi*sigma
    else:
        zi=-ci*sigma*xi
        # zi = -xi*sigma
    # print(sigma)
    return zi


if __name__ == '__main__':
    S=[[[1,20,1000],[0,100,100],[100]],[[1,20,1000],[0,100,100],[100]],[[1,20,1000],[0,100,100],[100]],[[1,30,2000],[0,100,100],[100]]]

    dict = [1000,2000]  # sequence of pairs
    # S=[[[1, 20, 1000], [0.1], [100]], [[1, 20, 1000], [0.1], [100]], [[1, 30, 2000], [0.2], [100]], [[1, 30, 1000], [0.1], [100]]]


    fvalues=[0]*4
    for _ in range(1000):
        fvalue = queryMechanism(S, 0.0001, 4,dict,[2])
        for i in range(4):
            fvalues[i]+=fvalue[i]

    for i in range(len(dict)):
        print(dict[i],fvalues[i]/1000)
    # print(np.random.choice([-1,1],(3,4)))
