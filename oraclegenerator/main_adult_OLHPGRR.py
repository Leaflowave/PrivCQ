from Algorithm1 import *
import linecache
import time

def adult_main_exp1(delta,budget,repeatTimes):
    start=time.time()
    Spath="adult//adult_info.txt"
    temp= linecache.getline(Spath,1)
    S=eval(temp)
    print(len(S))
    budget=budget*len(S)

    exp1path="adult//adult1.txt"
    temp1=linecache.getline(exp1path,1)
    frequency=eval(temp1)
    sequence=list(frequency.keys())
    frequency.clear()

    grouppath="adult//adult_group.txt"
    temp2=linecache.getline(grouppath,1)
    groupDict=eval(temp2)

    framework(S,groupDict,sequence,budget,len(sequence),delta,"experiments//adult_1_OLHPGRR_results.txt",[0],randomiser="OLHPGRR")
    end = time.time()
    print(end-start)
    return

def adult_main_exp2(delta,budget,repeatTimes):
    start=time.time()
    Spath = "adult//adult_info.txt"
    temp = linecache.getline(Spath, 1)
    S = eval(temp)
    print(len(S))
    budget = budget * len(S)

    exp1path = "adult//adult2.txt"
    temp1 = linecache.getline(exp1path, 1)
    frequency = eval(temp1)
    sequence = list(frequency.keys())
    frequency.clear()

    grouppath = "adult//adult_group.txt"
    temp2 = linecache.getline(grouppath, 1)
    groupDict = eval(temp2)

    framework(S, groupDict, sequence, budget, len(sequence), delta, "experiments//adult_2_OLHPGRR_results.txt", [0,1],randomiser="OLHPGRR")
    end = time.time()
    print(end - start)
    return

def adult_main_exp3(delta,budget,repeatTimes):
    start=time.time()
    Spath = "adult//adult_info.txt"
    temp = linecache.getline(Spath, 1)
    S = eval(temp)
    print(len(S))
    budget = budget * len(S)

    exp1path = "adult//adult3.txt"
    temp1 = linecache.getline(exp1path, 1)
    frequency = eval(temp1)
    sequence = list(frequency.keys())
    frequency.clear()

    # grouppath = "adult//adult_group.txt"
    # temp2 = linecache.getline(grouppath, 1)
    # groupDict = eval(temp2)

    framework(S, None, sequence, budget, len(sequence), delta, "experiments//adult_3_OLHPGRR_results.txt", [0, 1,2],randomiser="OLHPGRR")
    end = time.time()
    print(end - start)
    return

def adult_main_exp4(delta,budget,repeatTimes):
    start=time.time()
    Spath = "adult//adult_info.txt"
    temp = linecache.getline(Spath, 1)
    S = eval(temp)
    print(len(S))
    budget = budget * len(S)

    exp1path = "adult//adult6.txt"
    temp1 = linecache.getline(exp1path, 1)
    frequency = eval(temp1)
    sequence = list(frequency.keys())
    frequency.clear()

    # grouppath = "adult//adult_group.txt"
    # temp2 = linecache.getline(grouppath, 1)
    # groupDict = eval(temp2)

    framework(S, None, sequence, budget, len(sequence), delta, "experiments//adult_4_OLHPGRR_results.txt", [0, 2],randomiser="OLHPGRR")
    end = time.time()
    print(end - start)
    return


if __name__ == '__main__':

    delta=0.1
    repeatTimes=1
    proportion=0.5
    for _ in [0] * 500:
        adult_main_exp1(delta, proportion * 100, repeatTimes)
        adult_main_exp2(delta, proportion*100,repeatTimes)
        adult_main_exp3(delta, proportion * 100, repeatTimes)
        adult_main_exp4(delta, proportion * 100, repeatTimes)
