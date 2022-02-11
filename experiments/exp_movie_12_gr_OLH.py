import frequency_oracle_3dim as freq
import linecache
import random

def query_on_adult_dim3(oraclePath,oracleInterval,queryPath,trueOraclePath,aggregation="count"):
    # adult sum range 12 sum KHW where age in [2,5]
    queriesStr = linecache.getline(queryPath, 1)
    queries = eval(queriesStr)
    answer = [0]*500

    trueOracleStr = linecache.getline(trueOraclePath, 1)
    trueOracle = eval(trueOracleStr)
    # print(trueOracle)
    n = sum([trueOracle[k] for k in trueOracle.keys()])

    TrueAnswer = [0]*500
    relativeError = 0
    averageError = 0

    for i in range(1, 501):
        for _ in range(10):
            kthoracle = random.randint(1, 500)
            oracleWithoutGroup = freq.frequency_oracle(oraclePath, oracleInterval, k_th_oracle=kthoracle)
            # print(oracleWithoutGroup)
            oracle = {}
            for oraclekey in oracleWithoutGroup.keys():
                if oraclekey[1] not in oracle.keys():
                    oracle[oraclekey[1]] = {}
                if oraclekey[0] not in oracle[oraclekey[1]].keys():
                    oracle[oraclekey[1]][oraclekey[0]] = 0
                oracle[oraclekey[1]][oraclekey[0]] += oracleWithoutGroup[oraclekey]
            # for key in oracle.keys():
            #     print(oracle[key])

            sum_value = 0
            true_sum_value = 0
            # print(queries[i-1])
            # print(trueOracle)
            for k in range(queries[i - 1][0], queries[i - 1][1] + 1):
                # print("k: ", k)
                for j in oracle.keys():
                    # print("j: ", j)
                    sum_value += j * oracle[j][k]
                    # print(oracle[j][k])
                    true_sum_value += j * trueOracle[(k,j)]
            answer[i - 1] += sum_value
            TrueAnswer[i - 1] += true_sum_value
            # print(answer)
            # print(TrueAnswer)
        answer[i - 1] /= 10.0
        TrueAnswer[i - 1] /= 10.0
        relativeError += (answer[i - 1] - TrueAnswer[i - 1]) / max(0.001 * n, float(TrueAnswer[i - 1]))
        averageError += answer[i - 1] - TrueAnswer[i - 1]
        # averageError += sum_value - true_sum_value
        # relativeError += (abs(sum_value - true_sum_value)) / max(0.001 * n, float(true_sum_value))
    return answer,TrueAnswer, relativeError / 500, averageError / 500


if __name__ == '__main__':
    oraclePath = "experiments//movie_4_gr_OLH_results.txt"
    oracleInterval = 5
    queryPath = "experiments//movie_query_2_4.txt"
    trueOraclePath = "movie//movie6.txt"

    # for i in range(6):
    #     tableStr=linecache.getline(oraclePath,i)
    #     print(tableStr)

    ans,trueans, relativeError, averageError = query_on_adult_dim3(oraclePath, oracleInterval,
                                                           queryPath,
                                                           trueOraclePath,
                                                           aggregation="sum")
    print(relativeError)
    with open("experiments//final_movie_12_gr_OLH.txt", "w+") as f:
        f.write(str(ans) + "\n")
        f.write("true ans"+str(trueans)+"\n")
        f.write("relativeError:" + str(relativeError) + "\n")
        f.write("averageError:" + str(averageError) + "\n")

