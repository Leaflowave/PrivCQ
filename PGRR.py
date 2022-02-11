import math
import random

def queryMechanism(S,delta,Ycardinality,dic,dimension):
    """
    :param S:
    :param delta:
    :param Ycardinality: =len(dic)
    :param dic: list of keys
    :param dimension: [0,1]
    :return:
    """
    n = len(S)
    Answer_Table = []

    attr={}
    if len(dimension)==1:
        attr[dimension[0]]=dic
    elif len(dimension) == 3:
        for i in dimension:
            attr[i]=[x[i] for x in dic]
    elif dimension == [0, 1]:
        attr[0] = [x[0] for x in dic]
        attr[1] = [x[1] for x in dic]
    elif dimension == [0, 2]:
        attr[0] = [x[0] for x in dic]
        attr[2] = [x[1] for x in dic]
    else:
        print("Wrong dimension.")

    # print(attr[0])
    for i in range(n):  # the index of data owner
        data_entry_perturbed = []

        for idx in dimension:  # the index of data entry [0, 2]
            p = (math.exp(S[i][1][idx] / 100.0)) / (math.exp(S[i][1][idx] / 100.0) + len(set(attr[idx])) - 1)
            if random.random() <= p:
                data_entry_perturbed.append(S[i][0][idx])
            else:
                newValue = random.choice(list(set(attr[idx])-{S[i][0][idx]}))
                data_entry_perturbed.append(newValue)
        Answer_Table.append(data_entry_perturbed)
    return Answer_Table


# def queryMechanismGr(S,delta,Ycardinality,dic,dimension):
#     """
#     :param S:
#     :param delta:
#     :param Ycardinality: =len(dic)
#     :param dic: list of keys
#     :param dimension: [0,1]
#     :return:
#     """
#     print("GR!!!")
#     n = len(S)
#     Answer_Table = []
#     epsilon = math.inf   # the smallest epsilon, the highest protection level
#     for i in range(n):
#         for j in dimension:
#             epsilon = min(epsilon, S[i][1][j])
#     print(epsilon)
#     attr={}
#     if len(dimension)==1:
#         attr[dimension[0]]=dic
#     elif len(dimension) == 3:
#         for i in dimension:
#             attr[i]=[x[i] for x in dic]
#     elif dimension == [0, 1]:
#         attr[0] = [x[0] for x in dic]
#         attr[1] = [x[1] for x in dic]
#     elif dimension == [0, 2]:
#         attr[0] = [x[0] for x in dic]
#         attr[2] = [x[1] for x in dic]
#     else:
#         print("Wrong dimension.")
#
#     for i in range(n):  # the index of data owner
#         data_entry_perturbed = []
#
#         for idx in dimension:  # the index of data entry [0, 2]
#             # p = (math.exp(S[i][1][idx] / 100.0)) / (math.exp(S[i][1][idx] / 100.0) + len(attr[idx]) - 1)
#             p = (math.exp(epsilon / 100.0)) / (math.exp(epsilon / 100.0) + len(set(attr[idx])) - 1)
#             if random.random() <= p:
#                 data_entry_perturbed.append(S[i][0][idx])
#             else:
#                 newValue = random.choice(list(set(attr[idx])-{S[i][0][idx]}))
#                 data_entry_perturbed.append(newValue)
#         Answer_Table.append(data_entry_perturbed)
#     return Answer_Table