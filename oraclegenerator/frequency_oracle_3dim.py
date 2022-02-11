import linecache

def frequency_oracle(filepath,lineSpan,k_th_oracle=1):
    initline=(k_th_oracle-1)*lineSpan
    tmp=linecache.getline(filepath,initline+5)
    oraclstr=tmp.split("total:")
    frequency_oracle=eval(oraclstr[1])
    return frequency_oracle

if __name__ == '__main__':
    # print(group_frequency_oracle("experiments//adult_1_results.txt",33))
    # print(group_frequency_oracle("experiments//adult_1_Greedy_OLH_results.txt", 33))
    print(frequency_oracle("experiments//adult_3_Greedy_OLH_results.txt", 5))