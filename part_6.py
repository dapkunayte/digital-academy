# Последний с четными
def last_even(list)->int:
    if len(list) < 1:
        return 0
    sum=0
    for i,value in enumerate(list):
        if i%2==0:
            sum+=value
    return sum*list[len(list)-1]

#Max-min
def max_min(list)->float:
    if len(list) < 1:
        return 0
    else:
        return round(max(list)-min(list),3) # округление до трёх

# Умная сортировка
def smart_sort(list):
    for i in range(len(list)):
        for j in range(len(list)):
            if abs(list[i])<abs(list[j]):
                list[i],list[j]=list[j],list[i]
    return list