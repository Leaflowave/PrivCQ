import linecache

def group_table(filepath,lineSpan,k_th_oracle=1):
    initline=(k_th_oracle-1)*lineSpan
    grouped_table=dict()
    for i in range(4,lineSpan+1):
        tmp = linecache.getline(filepath, initline+i)
        if (i-4)%2==0:
            grouptmp=tmp.split(" ")
            groupkey=eval(grouptmp[0])
        elif (i-4)%2==1:
            totalstr=tmp.split("table without scaler:")
            total=eval(totalstr[1])
            grouped_table[groupkey]=total

    return grouped_table

if __name__ == '__main__':
    print(group_table("experiments//adult_1_PGRR_results.txt", 23))