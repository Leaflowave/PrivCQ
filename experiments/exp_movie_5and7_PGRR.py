import group_table4PGRR as freq
import linecache
import random


def query_on_adult_dim2(oraclePath,oracleInterval,queryPath,trueOraclePath,aggregation="count"):
    # adult_2 equal 5 and 7
    queriesStr=linecache.getline(queryPath,1)
    queries=eval(queriesStr)
    answer=[0]*500

    trueOracleStr=linecache.getline(trueOraclePath,1)
    trueOracle= eval(trueOracleStr)
    n=sum([sum(trueOracle[k].values()) for k in trueOracle.keys()])
    print(n)
    TrueAnswer=[0]*500
    relativeError = 0
    averageError=0
    # absrelativeError=0
    # absaverageError=0


    for i in range(1,501):
        for _ in range(10):
            kthoracle=random.randint(1,500)
            # kthoracle=_+1
            oracle=freq.group_table(oraclePath, oracleInterval,k_th_oracle=kthoracle)
            if aggregation=="count":
                count_value=0
                true_count_value=0
                # print(i)
                # print(queries[i-1])
                # for k1 in range(queries[i - 1][0][0], queries[i - 1][0][1] + 1):
                #     for k2 in range(queries[i - 1][1][0], queries[i - 1][1][1] + 1):

                for j in oracle.keys():
                    count_value+=oracle[j].count([queries[i - 1][0],queries[i - 1][1]])
                    true_count_value += trueOracle[j][queries[i - 1]]
                count_value=(count_value/32451)*n
                answer[i - 1] += count_value
                TrueAnswer[i - 1]+= true_count_value
                # answer.append(count_value)
                # TrueAnswer.append(true_count_value)
                # averageError += count_value - true_count_value
                # relativeError+= (abs(count_value - true_count_value))/max(0.001*n,float(true_count_value))
            elif aggregation=="sum":
                sum_value = 0
                true_sum_value = 0
                # for k1 in range(queries[i - 1][0][0], queries[i - 1][0][1] + 1):
                #     for k2 in range(queries[i - 1][1][0], queries[i - 1][1][1] + 1):

                for j in oracle.keys():
                    sum_value += j*oracle[j].count([queries[i - 1][0],queries[i - 1][1]])
                    true_sum_value += j*trueOracle[j][queries[i - 1]]
                sum_value=(sum_value/32451)*n
                answer[i - 1] += sum_value
                TrueAnswer[i - 1]+= true_sum_value
                # answer.append(sum_value)
                # TrueAnswer.append(true_sum_value)
                # averageError += sum_value - true_sum_value
                # relativeError += (abs(sum_value - true_sum_value)) /max(0.001*n,float(true_sum_value))
        answer[i - 1] /= 10.0
        TrueAnswer[i - 1] /= 10.0
        # absrelativeError += (abs(answer[i - 1] - TrueAnswer[i - 1])) / max(0.001 * n, float(TrueAnswer[i - 1]))
        # absaverageError += abs(answer[i - 1] - TrueAnswer[i - 1])
        relativeError += (answer[i - 1] - TrueAnswer[i - 1]) / max(0.001 * n, float(TrueAnswer[i - 1]))
        averageError += answer[i - 1] - TrueAnswer[i - 1]
    return answer,TrueAnswer,relativeError/500,averageError/500


if __name__ == '__main__':
    oraclePath = "experiments//movie_2_PGRR_results.txt"
    oracleInterval = 13
    queryPath = "experiments//movie_query_5_7_9.txt"
    trueOraclePath = "movie//movie5.txt"

    # file_1 = open("experiments//movie_2_PGRR_results.txt", "r")
    # a = file_1.readline()
    # print(a)

    ans, Trueans,relativeError, averageError = query_on_adult_dim2(oraclePath, oracleInterval,
                                                           queryPath,
                                                           trueOraclePath,
                                                           aggregation="count")
    print(relativeError)
    with open("experiments//final_movie_2_count_PGRR.txt", "w+") as f:
        f.write(str(ans) + "\n")
        f.write("true ans"+str(Trueans)+"\n")
        f.write("relativeError:" + str(relativeError) + "\n")
        f.write("averageError:" + str(averageError) + "\n")
        # f.write("absrelativeError:" + str(absrelativeError) + "\n")
        # f.write("absaverageError:" + str(absaverageError) + "\n")

    ans, Trueans,relativeError, averageError = query_on_adult_dim2(oraclePath, oracleInterval,
                                                           queryPath,
                                                           trueOraclePath,
                                                           aggregation="sum")
    print(relativeError)
    with open("experiments//final_movie_2_sum_PGRR.txt", "w+") as f:
        f.write(str(ans) + "\n")
        f.write("true ans" + str(Trueans) + "\n")
        f.write("relativeError:" + str(relativeError) + "\n")
        f.write("averageError:" + str(averageError) + "\n")
        # f.write("absrelativeError:" + str(absrelativeError) + "\n")
        # f.write("absaverageError:" + str(absaverageError) + "\n")

