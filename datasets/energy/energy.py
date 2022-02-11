import pandas as pd
import random
import numpy as np


def main():
    df = pd.read_csv('energy.csv')
    n = len(df)
    print(n)

    for i in range(n):  # round kwh to hundreds
        df["KWH"].iloc[i] = df["KWH"].iloc[i] // 1000

    file0 = open("energy/info0.csv", "w")
    df.to_csv(file0)
    file0.close()

    data_list = df.values.tolist()
    
    # generate epsilon and theta
    output = []
    epsilon_1 = 100 - np.random.randint(0, 100, n)
    epsilon_2 = 100 - np.random.randint(0, 100, n)
    epsilon_3 = 100 - np.random.randint(0, 100, n)
    theta = 100 - np.random.randint(0, 100, n)
    
    # # print(epsilon)
    # # print(theta)
    #
    for i in range(n):
        output.append([data_list[i]])
        output[i].append([epsilon_1[i], epsilon_2[i], epsilon_3[i]])
        output[i].append([theta[i]])

    file_info = open("energy/energy_info.txt", "w")
    file_info.write(str(output) + "\n")
    file_info.close()
    #
    # get groups according to sum attribute
    kwh = sorted(set(df["KWH"].to_list()))
    kwh_dict = {}
    for item in kwh:
        kwh_dict[item] = []
    for i in range(n):
        tmp = df["KWH"].iloc[i]
        kwh_dict[tmp].append(i)

    file_group = open("energy/energy_group.txt", "w")
    file_group.write(str(kwh_dict) + "\n")
    file_group.close()

    # single dimension
    dic1_group = {}
    for value in kwh:
        dic1_group[value] = {}
    attr_1 = [1, 2, 3, 4]
    for key in dic1_group.keys():
        for i in range(len(attr_1)):
            dic1_group[key][attr_1[i]] = 0
    for i in range(n):
        tmp = df["REGIONC"].iloc[i]
        group = df["KWH"].iloc[i]
        dic1_group[group][tmp] += 1
    file4 = open("energy/energy4.txt", "w")
    file4.write(str(dic1_group) + "\n")
    file4.close()

    dic1 = {}
    attr_1 = [1, 2, 3, 4]
    for item in attr_1:
        dic1[item] = 0
    for i in range(n):
        tmp = (df["REGIONC"].iloc[i])
        dic1[tmp] += 1
    file1 = open("energy/energy1.txt", "w")
    file1.write(str(dic1) + "\n")
    file1.close()
    #
    # # two dimensions
    dic2_group = {}
    for value in kwh:
        dic2_group[value] = {}
    attr_2 = [1, 2]
    for key in dic2_group.keys():
        for element in attr_1:
            for item in attr_2:
                tmp = (element, item)
                dic2_group[key][tmp] = 0

    for i in range(n):
        tmp = (df["REGIONC"].iloc[i], df["UR"].iloc[i])
        group = df["KWH"].iloc[i]
        dic2_group[group][tmp] += 1

    file5 = open("energy/energy5.txt", "w")
    file5.write(str(dic2_group) + "\n")
    file5.close()

    dic2 = {}
    attr_2 = [1, 2]
    for element in attr_1:
        for item in attr_2:
            tmp = (element, item)
            dic2[tmp] = 0
    for i in range(n):
        tmp = (df["REGIONC"].iloc[i], df["UR"].iloc[i])
        dic2[tmp] += 1
    file2 = open("energy/energy2.txt", "w")
    file2.write(str(dic2) + "\n")
    file2.close()

    # three dimensions
    dic3 = {}
    attr_3 = list(range(0, 78))
    for element in attr_1:
        for item in attr_2:
            for bla in attr_3:
                tmp = (element, item, bla)
                dic3[tmp] = 0
    for i in range(n):
        tmp = (df["REGIONC"].iloc[i], df["UR"].iloc[i], df["KWH"].iloc[i])
        dic3[tmp] += 1
    print(len(dic3))
    file3 = open("energy/energy3.txt", "w")
    file3.write(str(dic3) + "\n")
    file3.close()


    # new problem
    dic4 = {}
    attr_3 = list(range(0, 78))
    for element in attr_1:
        for bla in attr_3:
            tmp = (element, bla)
            dic4[tmp] = 0
    for i in range(n):
        tmp = (df["REGIONC"].iloc[i], df["KWH"].iloc[i])
        dic4[tmp] += 1
    print(len(dic4))
    file6 = open("energy/energy6.txt", "w")
    file6.write(str(dic4) + "\n")
    file6.close()

if __name__ == '__main__':
    main()
