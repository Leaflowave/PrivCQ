import group_table4PGRR as freq
import linecache
import random

def query_on_adult_dim1(tablePath,tableInterval,queryPath,trueOraclePath,aggregation="count"):
    #adult_1 range  query 2th & 4th

    queriesStr=linecache.getline(queryPath,1)
    queries=eval(queriesStr)
    answer=[0]*500

    trueOracleStr=linecache.getline(trueOraclePath,1)
    trueOracle= eval(trueOracleStr)
    n=sum([sum(trueOracle[k].values()) for k in trueOracle.keys()])
    TrueAnswer=[0]*500
    relativeError = 0
    averageError=0


    for i in range(1,501):
        for _ in range(10):
            kthoracle = random.randint(1, 500)
            table = freq.group_table(tablePath, tableInterval, k_th_oracle=kthoracle)
            if aggregation=="count":
                count_value=0
                true_count_value=0
                # print(i)
                # print(queries[i-1])
                for k in range(queries[i - 1][0], queries[i - 1][1] + 1):
                    for j in table.keys():
                        for entry in table[j]:
                            if entry[0]==k:
                                count_value+=1
                        true_count_value += trueOracle[j][k]
                count_value=(count_value/32390)*n
                answer[i - 1] += count_value
                TrueAnswer[i - 1] = true_count_value
                # answer.append(count_value)
                # TrueAnswer.append(true_count_value)
                # relativeError+= (abs(count_value - true_count_value))/max(0.001*n,float(true_count_value))
                # averageError+=count_value - true_count_value
            elif aggregation=="sum":
                sum_value = 0
                true_sum_value = 0
                for k in range(queries[i-1][0], queries[i-1][1] + 1):
                    for j in table.keys():
                        for entry in table[j]:
                            if entry[0]==k:
                                sum_value +=j
                        true_sum_value += j*trueOracle[j][k]
                sum_value = (sum_value / 32390) * n
                answer[i - 1] += sum_value
                TrueAnswer[i - 1] = true_sum_value
            # answer.append(sum_value)
            # TrueAnswer.append(true_sum_value)
            # averageError += sum_value - true_sum_value
            # relativeError += (abs(sum_value - true_sum_value)) / max(0.001*n,float(true_sum_value))
        answer[i - 1] /= 10.0
        relativeError += (answer[i - 1] - TrueAnswer[i - 1]) / max(0.001 * n, float(TrueAnswer[i - 1]))
        averageError += answer[i - 1] - TrueAnswer[i - 1]
    return answer,TrueAnswer,relativeError/500,averageError/500


if __name__ == '__main__':
    tablePath="experiments//adult_1_gr_PGRR_results.txt"
    tableInterval=23
    queryPath="experiments//adult_query_2_4_12.txt"
    trueOraclePath="adult/adult4.txt"
    #
    # file_1 = open("experiments//adult_1_gr_PGRR_results.txt", "r")
    # a = file_1.readline()
    # print(a)


    ans,trueAns,relativeError,averageError=query_on_adult_dim1(tablePath,tableInterval,queryPath,trueOraclePath,aggregation="count")
    print(relativeError)
    with open("experiments//final_adult_1_count_gr_PGRR.txt","w+") as f:
        f.write(str(ans)+"\n")
        f.write("true ans" + str(trueAns) + "\n")
        f.write("relativeError:"+str(relativeError)+"\n")
        f.write("averageError:" + str(averageError) + "\n")

    ans,trueAns,relativeError,averageError=query_on_adult_dim1(tablePath,tableInterval,queryPath,trueOraclePath,aggregation="sum")
    print(relativeError)
    with open("experiments//final_adult_1_sum_gr_PGRR.txt","w+") as f:
        f.write(str(ans)+"\n")
        f.write("true ans" + str(trueAns) + "\n")
        f.write("relativeError:"+str(relativeError)+"\n")
        f.write("averageError:"+str(averageError)+"\n")




