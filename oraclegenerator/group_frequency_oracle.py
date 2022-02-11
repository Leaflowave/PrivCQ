import linecache

def group_frequency_oracle(filepath,lineSpan,k_th_oracle=1):
    initline=(k_th_oracle-1)*lineSpan
    grouped_frequency_oracle=dict()
    for i in range(4,lineSpan+1):
        if (i-4)%3==1: continue
        tmp = linecache.getline(filepath, initline+i)
        if (i-4)%3==0:
            grouptmp=tmp.split(" ")
            groupkey=eval(grouptmp[0])
        elif (i-4)%3==2:
            totalstr=tmp.split("total:")
            total=eval(totalstr[1])
            grouped_frequency_oracle[groupkey]=total

    return grouped_frequency_oracle

if __name__ == '__main__':
    print(group_frequency_oracle("experiments//adult_1_results.txt",33))
    # print(group_frequency_oracle("experiments//energy_1_results.txt",192))
    # print(group_frequency_oracle("experiments//adult_1_Greedy_OLH_results.txt", 33))
    # print(group_frequency_oracle("experiments//adult_1_results.txt", 33))