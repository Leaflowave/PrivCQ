import table4PGRR_3dim as freq
import linecache
import random


def query_on_adult_dim3(oraclePath,oracleInterval,queryPath,trueOraclePath,aggregation="count"):
    # adult sum range 12 sum KHW where age in [2,5]
    queriesStr = linecache.getline(queryPath, 1)
    queries = eval(queriesStr)
    answer = [0]*500

    trueOracleStr = linecache.getline(trueOraclePath, 1)
    trueOracle = eval(trueOracleStr)
    n = sum([trueOracle[k] for k in trueOracle.keys()])

    TrueAnswer = [0]*500
    relativeError = 0
    averageError = 0

    for i in range(1, 501):
        for _ in range(10):
            kthoracle = random.randint(1, 500)
            oracleWithoutGroup = freq.table(oraclePath, oracleInterval, k_th_oracle=kthoracle)
            # print(oracleWithoutGroup)
            oracle = {}
            for oraclekey in oracleWithoutGroup:
                if oraclekey[1] not in oracle.keys():
                    oracle[oraclekey[1]] = {}
                if oraclekey[0] not in oracle[oraclekey[1]].keys():
                    oracle[oraclekey[1]][oraclekey[0]] = 0
                oracle[oraclekey[1]][oraclekey[0]] += 1
            # for key in oracle.keys():
            #     print(oracle[key])

            sum_value = 0
            true_sum_value = 0

            for k in range(queries[i - 1][0], queries[i - 1][1] + 1):
                for j in oracle.keys():
                    if k in oracle[j]:
                        sum_value += j * oracle[j][k]
                    true_sum_value += j * trueOracle[(k, j)]
            sum_value=(sum_value/12080)*n
            answer[i - 1] += sum_value
            TrueAnswer[i - 1] += true_sum_value
            # answer.append(sum_value)
            # TrueAnswer.append(true_sum_value)
        answer[i - 1] /= 10.0
        TrueAnswer[i - 1] /= 10.0
        relativeError += (answer[i - 1] - TrueAnswer[i - 1]) / max(0.001 * n, float(TrueAnswer[i - 1]))
        averageError += answer[i - 1] - TrueAnswer[i - 1]
        # averageError += sum_value - true_sum_value
        # relativeError += (abs(sum_value - true_sum_value)) / max(0.001 * n, float(true_sum_value))
    return answer,TrueAnswer, relativeError / 500, averageError / 500


if __name__ == '__main__':
    oraclePath = "experiments//energy_4_gr_PGRR_results.txt"
    oracleInterval = 4
    queryPath = "experiments//energy_query_2_4.txt"
    trueOraclePath = "energy//energy6.txt"

    # for i in range(5):
    #     tableStr=linecache.getline(oraclePath,i)
    #     print(tableStr)

    ans,trueans, relativeError, averageError = query_on_adult_dim3(oraclePath, oracleInterval,
                                                           queryPath,
                                                           trueOraclePath,
                                                           aggregation="sum")
    print(relativeError)
    with open("experiments//final_energy_12_gr_PGRR.txt", "w+") as f:
        f.write(str(ans) + "\n")
        f.write("true ans"+str(trueans)+"\n")
        f.write("relativeError:" + str(relativeError) + "\n")
        f.write("averageError:" + str(averageError) + "\n")

