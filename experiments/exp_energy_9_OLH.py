import frequency_oracle_3dim as freq
import linecache
import random

def query_on_adult_dim2(oraclePath,oracleInterval,queryPath,trueOraclePath,aggregation="count"):
    # adult_3 equal 9
    queriesStr=linecache.getline(queryPath,1)
    queries=eval(queriesStr)
    answer=[0]*500

    trueOracleStr=linecache.getline(trueOraclePath,1)
    trueOracle= eval(trueOracleStr)
    n=sum([sum(trueOracle[k].values()) for k in trueOracle.keys()])

    TrueAnswer=[0]*500
    relativeError = 0
    averageError=0
    # absrelativeError = 0
    # absaverageError = 0

    for i in range(1,501):
        for _ in range(10):
            kthoracle=random.randint(1,500)
            oracleWithoutGroup=freq.frequency_oracle(oraclePath, oracleInterval,k_th_oracle=kthoracle)
            oracle={}
            for oraclekey in oracleWithoutGroup.keys():
                if oraclekey[2] not in oracle.keys():
                    oracle[oraclekey[2]]={}
                if (oraclekey[0],oraclekey[1]) not in oracle[oraclekey[2]].keys():
                    oracle[oraclekey[2]][(oraclekey[0],oraclekey[1])]=0
                oracle[oraclekey[2]][(oraclekey[0], oraclekey[1])] += oracleWithoutGroup[oraclekey]
            sum_value = 0
            true_sum_value = 0
            for j in oracle.keys():
                sum_value += j*oracle[j][queries[i-1]]
                if j in trueOracle.keys():
                    true_sum_value += j*trueOracle[j][queries[i - 1]]
            answer[i - 1] += sum_value
            TrueAnswer[i - 1] += true_sum_value
            # averageError += sum_value - true_sum_value
            # relativeError += (abs(sum_value - true_sum_value)) /max(0.001*n,float(true_sum_value))
        answer[i - 1] /= 10.0
        TrueAnswer[i - 1] /= 10.0
        relativeError += (answer[i - 1] - TrueAnswer[i - 1]) / max(0.001 * n, float(TrueAnswer[i - 1]))
        averageError += answer[i - 1] - TrueAnswer[i - 1]
        # absrelativeError += (abs(answer[i - 1] - TrueAnswer[i - 1])) / max(0.001 * n, float(TrueAnswer[i - 1]))
        # absaverageError += abs(answer[i - 1] - TrueAnswer[i - 1])
    return answer,TrueAnswer,relativeError/500,averageError/500


if __name__ == '__main__':
    oraclePath = "experiments//energy_3_OLH_results.txt"
    oracleInterval = 5
    queryPath = "experiments//energy_query_5_7_9.txt"
    trueOraclePath = "energy//energy5.txt"


    ans, trueans,relativeError, averageError = query_on_adult_dim2(oraclePath, oracleInterval,
                                                           queryPath,
                                                           trueOraclePath,
                                                           aggregation="sum")
    print(relativeError)
    with open("experiments//final_energy_3_sum_OLH.txt", "w+") as f:
        f.write(str(ans) + "\n")
        f.write(str(trueans)+"\n")
        f.write("relativeError:" + str(relativeError) + "\n")
        f.write("averageError:" + str(averageError) + "\n")

