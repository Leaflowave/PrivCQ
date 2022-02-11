import random
import numpy as np
"""
我们有3个数据集，每个数据集包含3组FO，每一组有500个。
我们有6种方法。
我们有10种不同的query（以movie为例）：

我们在一维的500个FO上、用6种不同的table(oracle)(分别做以下query：
#1. SELECT count(*) WHERE Age = x
2. SELECT count(*) WHERE Age in [2, 4]
#3. SELECT sum(hpw) WHERE Age = x （有无必要？精确度应与1相同）
4. SELECT sum(hpw) WHERE Age in [2, 4]

我们在二维的500个FO上、用6种不同的table(oracle)分别做以下query：
5. SELECT count(*) WHERE Age = x AND Education = y
6. SELECT count(*) WHERE Age in [2,4] AND Education = [5, 8]
7. SELECT sum(hpw) WHERE Age = x AND Education = y （同3）
8. SELECT sum(hpw) WHERE Age in [2,4] AND Education = [5, 8]

我们在三维的500个FO上、用6种不同的table(oracle)分别做以下query：
9. SELECT sum(hpw) WHERE Age = x AND Education = y 
10.  SELECT sum(hpw) WHERE Age in [2,4] AND Education = [5, 8]

在每个数据集上，我们以6种不同的table(oracle)分别做以上10种query。
每次的input都是相应的FO上全部的500条vector。
range query时我们在domain里随机生成两个不同的整数，组成一个range。
"""
def movie_generate_random_count_dim2(filepath,dim_1_low,dim_1_high,dim_2_low,dim_2_high,num=500):
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

def movie_generate_random_range_dim2(filepath,dim_1_low,dim_1_high,dim_2_low,dim_2_high,num=500):
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


def movie_generate_random_range_dim1(filepath, low, high, num=500):
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
    print(movie_generate_random_range_dim1("experiments/movie_query_2_4.txt", 1, 7))
    print(movie_generate_random_count_dim2("experiments/movie_query_5_7_9.txt", 1, 7, 1, 2))
    print(movie_generate_random_range_dim2("experiments/movie_query_6_8_10.txt", 1, 7, 1, 2))
