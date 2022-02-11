import linecache

def table(filepath,lineSpan,k_th_oracle=1):
    initline=(k_th_oracle-1)*lineSpan
    tmp=linecache.getline(filepath,initline+4)
    totalstr=tmp.split("table without scaler:")

    total_table=eval(totalstr[1])

    return total_table

if __name__ == '__main__':
    print(table("experiments//adult_3_PGRR_results.txt", 4))