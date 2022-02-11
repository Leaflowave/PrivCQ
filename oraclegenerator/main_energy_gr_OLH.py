from Algorithm1 import *
import linecache
import time

def energy_main_exp1(delta,budget,repeatTimes):
    start=time.time()
    Spath="energy//energy_info.txt"
    temp= linecache.getline(Spath,1)
    S=eval(temp)
    print(len(S))
    budget=budget*len(S)

    exp1path="energy//energy1.txt"
    temp1=linecache.getline(exp1path,1)
    frequency=eval(temp1)
    sequence=list(frequency.keys())
    frequency.clear()

    grouppath="energy//energy_group.txt"
    temp2=linecache.getline(grouppath,1)
    groupDict=eval(temp2)

    framework(S,groupDict,sequence,budget,len(sequence),delta,"experiments//energy_1_gr_OLH_results.txt",[0],randomiser="OLH",auctionMethod="GR")
    end = time.time()
    print(end-start)
    return

def energy_main_exp2(delta,budget,repeatTimes):
    start=time.time()
    Spath = "energy//energy_info.txt"
    temp = linecache.getline(Spath, 1)
    S = eval(temp)
    print(len(S))
    budget = budget * len(S)

    exp1path = "energy//energy2.txt"
    temp1 = linecache.getline(exp1path, 1)
    frequency = eval(temp1)
    sequence = list(frequency.keys())
    frequency.clear()

    grouppath = "energy//energy_group.txt"
    temp2 = linecache.getline(grouppath, 1)
    groupDict = eval(temp2)

    framework(S, groupDict, sequence, budget, len(sequence), delta, "experiments//energy_2_gr_OLH_results.txt", [0,1],randomiser="OLH",auctionMethod="GR")
    end = time.time()
    print(end - start)
    return

def energy_main_exp3(delta,budget,repeatTimes):
    start=time.time()
    Spath = "energy//energy_info.txt"
    temp = linecache.getline(Spath, 1)
    S = eval(temp)
    print(len(S))
    budget = budget * len(S)

    exp1path = "energy//energy3.txt"
    temp1 = linecache.getline(exp1path, 1)
    frequency = eval(temp1)
    sequence = list(frequency.keys())
    frequency.clear()

    # grouppath = "energy//energy_group.txt"
    # temp2 = linecache.getline(grouppath, 1)
    # groupDict = eval(temp2)

    framework(S, None, sequence, budget, len(sequence), delta, "experiments//energy_3_gr_OLH_results.txt", [0, 1,2],randomiser="OLH",auctionMethod="GR")
    end = time.time()
    print(end - start)
    return


def energy_main_exp4(delta,budget,repeatTimes):
    start=time.time()
    Spath = "energy//energy_info.txt"
    temp = linecache.getline(Spath, 1)
    S = eval(temp)
    print(len(S))
    budget = budget * len(S)

    exp1path = "energy//energy6.txt"
    temp1 = linecache.getline(exp1path, 1)
    frequency = eval(temp1)
    sequence = list(frequency.keys())
    frequency.clear()

    # grouppath = "energy//energy_group.txt"
    # temp2 = linecache.getline(grouppath, 1)
    # groupDict = eval(temp2)

    framework(S, None, sequence, budget, len(sequence), delta, "experiments//energy_4_gr_OLH_results.txt", [0, 2],randomiser="OLH",auctionMethod="GR")
    end = time.time()
    print(end - start)
    return


if __name__ == '__main__':

    delta=0.1
    repeatTimes=1
    proportion=0.5
    for _ in [0] * 500:
        energy_main_exp1(delta, proportion * 100, repeatTimes)
        energy_main_exp2(delta, proportion*100,repeatTimes)
        energy_main_exp3(delta, proportion * 100, repeatTimes)
        energy_main_exp4(delta, proportion * 100, repeatTimes)
