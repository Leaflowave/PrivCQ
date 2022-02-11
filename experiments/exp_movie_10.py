import frequency_oracle_3dim as freq
import linecache
import random

def query_on_adult_dim3(oraclePath,oracleInterval,queryPath,trueOraclePath,aggregation="count"):
    # adult_3 range 10
    queriesStr = linecache.getline(queryPath, 1)
    queries = eval(queriesStr)
    answer = [0]*500

    trueOracleStr = linecache.getline(trueOraclePath, 1)
    trueOracle = eval(trueOracleStr)
    n = sum([sum(trueOracle[k].values()) for k in trueOracle.keys()])

    TrueAnswer = [0]*500
    relativeError = 0
    averageError = 0

    for i in range(1, 501):
        for _ in range(10):
            kthoracle = random.randint(1, 500)
            oracleWithoutGroup = freq.frequency_oracle(oraclePath, oracleInterval, k_th_oracle=kthoracle)
            oracle = {}
            for oraclekey in oracleWithoutGroup.keys():
                if oraclekey[2] not in oracle.keys():
                    oracle[oraclekey[2]] = {}
                if (oraclekey[0], oraclekey[1]) not in oracle[oraclekey[2]].keys():
                    oracle[oraclekey[2]][(oraclekey[0], oraclekey[1])] = 0
                oracle[oraclekey[2]][(oraclekey[0], oraclekey[1])] += oracleWithoutGroup[oraclekey]

            sum_value = 0
            true_sum_value = 0
            for k1 in range(queries[i - 1][0][0], queries[i - 1][0][1] + 1):
                for k2 in range(queries[i - 1][1][0], queries[i - 1][1][1] + 1):
                    for j in oracle.keys():
                        sum_value += j * oracle[j][(k1,k2)]
                        true_sum_value += j * trueOracle[j][(k1,k2)]
            answer[i - 1] += sum_value
            TrueAnswer[i - 1] += true_sum_value
        answer[i - 1] /= 10.0
        TrueAnswer[i - 1] /= 10.0
        relativeError += (answer[i - 1] - TrueAnswer[i - 1]) / max(0.001 * n, float(TrueAnswer[i - 1]))
        averageError += answer[i - 1] - TrueAnswer[i - 1]
        # averageError += sum_value - true_sum_value
        # relativeError += (abs(sum_value - true_sum_value)) / max(0.001 * n, float(true_sum_value))
    return answer,TrueAnswer, relativeError / 500, averageError / 500


if __name__ == '__main__':
    oraclePath = "experiments//movie_3_results.txt"
    oracleInterval = 5
    queryPath = "experiments//movie_query_6_8_10.txt"
    trueOraclePath = "movie//movie5.txt"

    ans,trueans, relativeError, averageError = query_on_adult_dim3(oraclePath, oracleInterval,
                                                           queryPath,
                                                           trueOraclePath,
                                                           aggregation="sum")
    print(relativeError)
    with open("experiments//final_movie_3_sum_range.txt", "w+") as f:
        f.write(str(ans) + "\n")
        f.write("true ans"+str(trueans)+"\n")
        f.write("relativeError:" + str(relativeError) + "\n")
        f.write("averageError:" + str(averageError) + "\n")

