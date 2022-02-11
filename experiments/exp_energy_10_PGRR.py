import table4PGRR_3dim as freq
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
            oracleWithoutGroup = freq.table(oraclePath, oracleInterval, k_th_oracle=kthoracle)
            oracle = {}
            for oraclekey in oracleWithoutGroup:
                if oraclekey[2] not in oracle.keys():
                    oracle[oraclekey[2]] = {}
                if (oraclekey[0], oraclekey[1]) not in oracle[oraclekey[2]].keys():
                    oracle[oraclekey[2]][(oraclekey[0], oraclekey[1])] = 0
                oracle[oraclekey[2]][(oraclekey[0], oraclekey[1])] += 1
            # print(oracle)
            # print(oracle.keys())
            # for i in range(len(oracle)):
            #     print(len(oracle[i]), oracle[i])
            #     if not (8, 13) in oracle[i]:
            #         print("!!!!!!!!!!!!!!!!!!!!!1")
            sum_value = 0
            true_sum_value = 0
            for k1 in range(queries[i - 1][0][0], queries[i - 1][0][1] + 1):
                for k2 in range(queries[i - 1][1][0], queries[i - 1][1][1] + 1):
                    for j in oracle.keys():
                        if (k1, k2) in oracle[j]:
                            sum_value += j * oracle[j][(k1,k2)]
                        if j in trueOracle.keys():
                            if (k1, k2) in trueOracle[j]:
                                true_sum_value += j * trueOracle[j][(k1,k2)]
            sum_value=(sum_value/8051)*n
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
    oraclePath = "experiments//energy_3_PGRR_results.txt"
    oracleInterval = 4
    queryPath = "experiments//energy_query_6_8_10.txt"
    trueOraclePath = "energy//energy5.txt"

    # file_1 = open("experiments//energy_3_PGRR_results.txt", "r")
    # a = file_1.readline()
    # print(a)

    ans,trueans, relativeError, averageError = query_on_adult_dim3(oraclePath, oracleInterval,
                                                           queryPath,
                                                           trueOraclePath,
                                                           aggregation="sum")
    print(relativeError)
    with open("experiments//final_energy_3_sum_range_PGRR.txt", "w+") as f:
        f.write(str(ans) + "\n")
        f.write("true ans"+str(trueans)+"\n")
        f.write("relativeError:" + str(relativeError) + "\n")
        f.write("averageError:" + str(averageError) + "\n")

