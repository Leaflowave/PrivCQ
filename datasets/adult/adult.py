import pandas as pd
import random
import numpy as np


def main():
    df = pd.read_csv('Adult.csv')
    n = len(df)
    print(n)
    # print(data_list)

    for i in range(n):  # round age and hpw to tens
        df["Age"].iloc[i] = df["Age"].iloc[i] // 10
        df["hourspw"].iloc[i] = df["hourspw"].iloc[i] // 10

    data_list = df.values.tolist()

    # generate epsilon and theta
    output = []
    epsilon_1 = 100 - np.random.randint(0, 100, n)
    epsilon_2 = 100 - np.random.randint(0, 100, n)
    epsilon_3 = 100 - np.random.randint(0, 100, n)
    theta = 100 - np.random.randint(0, 100, n)

    # print(epsilon)
    # print(theta)

    for i in range(n):
        output.append([data_list[i]])
        output[i].append([epsilon_1[i], epsilon_2[i], epsilon_3[i]])
        output[i].append([theta[i]])

    file_info = open("adult/adult_info.txt", "w")
    file_info.write(str(output) + "\n")
    file_info.close()


    # get groups according to sum attribute
    hpw = sorted(set(df["hourspw"].tolist()))
    hpw_dict = {}
    for item in hpw:
        hpw_dict[item] = []
    for i in range(n):
        tmp = df["hourspw"].iloc[i]
        hpw_dict[tmp].append(i)

    file_group = open("adult/adult_group.txt", "w")
    file_group.write(str(hpw_dict) + "\n")
    file_group.close()

    # single dimension
    dic1 = {}
    max_age = max(df['Age'])
    min_age = min(df['Age'])
    attr_1 = list(range(min_age, max_age+1))
    for i in range(len(attr_1)):
        dic1[attr_1[i]] = 0
    for i in range(n):
        tmp = (df["Age"].iloc[i])
        dic1[tmp] += 1
    file1 = open("adult/adult1.txt", "w")
    file1.write(str(dic1) + "\n")
    file1.close()

    # two dimensions
    dic2 = {}
    max_edu = max(df['Education'])
    min_edu = min(df['Education'])
    attr_2 = list(range(min_edu, max_edu + 1))
    # print(attr_2)
    for element in attr_1:
        for item in attr_2:
            tmp = (element, item)
            dic2[tmp] = 0
    for i in range(n):
        tmp = (df["Age"].iloc[i], df["Education"].iloc[i])
        dic2[tmp] += 1
    file2 = open("adult/adult2.txt", "w")
    file2.write(str(dic2) + "\n")
    file2.close()

    # three dimensions
    dic3 = {}
    max_hpw = max(df['hourspw'])
    min_hpw = min(df['hourspw'])
    attr_3 = list(range(min_hpw, max_hpw+1))
    for element in attr_1:
        for item in attr_2:
            for bla in attr_3:
                tmp = (element, item, bla)
                dic3[tmp] = 0
    for i in range(n):
        tmp = (df["Age"].iloc[i], df["Education"].iloc[i], df["hourspw"].iloc[i])
        dic3[tmp] += 1
    file3 = open("adult/adult3.txt", "w")
    file3.write(str(dic3) + "\n")
    file3.close()


if __name__ == '__main__':
    main()
