import group_frequency_oracle as freq
import linecache
import random

if __name__ == '__main__':
    Path = "experiments//final_energy_12_gr.txt"
    n = 12080  # 12080 for gr; 7829 for none
    answerStr = linecache.getline(Path, 1)
    trueAnsStr = linecache.getline(Path, 2)
    relativeError = 0
    averageError = 0
    absRelativeError = 0
    answer = eval(answerStr)
    # print(trueAnsStr)
    trueAnsStr = trueAnsStr[8: ]
    trueAns = eval(trueAnsStr)
    # print(trueAns)
    for i in range(501):
        relativeError += (answer[i - 1] - trueAns[i - 1]) / max(0.001 * n, float(trueAns[i - 1]))
        averageError += answer[i - 1] - trueAns[i - 1]
        absRelativeError += abs(answer[i - 1] - trueAns[i - 1]) / max(0.001 * n, float(trueAns[i - 1]))

        # relativeError += (answer[i - 1] - trueAns[i - 1]) / float(trueAns[i - 1])
        # absRelativeError += abs(answer[i - 1] - trueAns[i - 1]) /float(trueAns[i - 1])
    print(relativeError/500)
    print(averageError/500)
    print(absRelativeError/500)

    with open(Path,"a") as file:
        file.write("\n" + "\n" + "From the frequency vector, we compute: " + "\n")
        file.write("relativeError: " + str(relativeError / 500) + "\n")
        file.write("averageError: " + str(averageError / 500) + "\n")
        file.write("absRelativeError: " + str(absRelativeError / 500))
    # file.close()



