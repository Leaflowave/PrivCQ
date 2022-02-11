import random
import numpy as np

def energy_generate_random_count_dim2(filepath,dim_1_low,dim_1_high,dim_2_low,dim_2_high,num=500):
    """
    5, 7 and 9
    """
    queryPool=[]
    for _ in range(num):
        dim1Value=random.randint(dim_1_low,dim_1_high)
        dim2Value=random.randint(dim_2_low,dim_2_high)
        queryPool.append((dim1Value,dim2Value))
    with open(filepath,"w+") as f:
        f.write(str(queryPool))
    return queryPool

def energy_generate_random_range_dim2(filepath,dim_1_low,dim_1_high,dim_2_low,dim_2_high,num=500):
    """
    6, 8 and 10
    """
    queryPool=[]
    query=[]
    for _ in range(num):
        left1 = random.randint(dim_1_low, dim_1_high)
        right1 = random.randint(left1, dim_1_high)
        query.append((left1, right1))

        left2 = random.randint(dim_2_low, dim_2_high)
        # right2 = random.randint(left2, dim_2_high)
        query.append((left2, left2))

        queryPool.append(query[:])
        query.clear()


    with open(filepath,"w+") as f:
        f.write(str(queryPool))

    return queryPool


def energy_generate_random_range_dim1(filepath, low, high, num=500):
    """
    2 and 4
    """
    queryPool = []
    for _ in range(num):
        left=random.randint(low, high)
        right=random.randint(left, high)
        queryPool.append((left,right))
    with open(filepath, "w+") as f:
        # f.write("age_range\n")
        f.write(str(queryPool))
    return queryPool

if __name__ == '__main__':
    print(energy_generate_random_range_dim1("experiments/energy_query_2_4.txt", 1, 4))
    print(energy_generate_random_count_dim2("experiments/energy_query_5_7_9.txt", 1, 4, 1, 2))
    print(energy_generate_random_range_dim2("experiments/energy_query_6_8_10.txt", 1, 4, 1, 2))
