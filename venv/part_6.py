# Последний с четными
def lastEven(list)->int:
    if len(list) < 1:
        return 0
    sum=0
    for i,x in enumerate(list):
        if i%2==0:
            sum+=x
    return sum*list[len(list)-1]

#Max-min
def maxMin(list)->float:
    if len(list) < 1:
        return 0
    else:
        return round(max(list)-min(list),3)

# Умная сортировка
def smartSort(list):
    for i in range(len(list)):
        for j in range(len(list)):
            if abs(list[i])<abs(list[j]):
                list[i],list[j]=list[j],list[i]
    return list