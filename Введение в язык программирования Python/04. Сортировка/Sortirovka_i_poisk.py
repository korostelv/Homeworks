import random

lst = [random.randint(-10,50) for i in range(50)]
# print(lst)

######## 1 ##################метод Шелла

def shell_sort(lst):
    last_index = len(lst)
    step =  len(lst)//2
    while(step>0):
        for i in range(step, last_index):
            j = i
            delta = j - step
            while delta>=0 and lst[delta] > lst[j]:
                lst[delta],lst[j] = lst[j],lst[delta]
                j = delta
                delta = j -step
        step //=2
    return lst


shell_sort(lst)
# print('Сортировка методом Шелла',lst)

################## 2 ######################## пирамидальная

def HeapSort(lst):
    for start in range(len(lst)-2//2,-1,-1):
        HeapSift(lst,start,len(lst)-1)
    for end in range(len(lst)-1,0,-1):
        lst[end],lst[0] = lst[0],lst[end]
        HeapSift(lst, 0 ,end-1)

def HeapSift(lst,start,end):
    root = start
    while True:
        child = root*2 +1
        if child > end:
            break
        if child+1 <= end and lst[child]<lst[child+1]:
            child+=1
        if lst[root] < lst[child]:
            lst[root],lst[child] = lst[child],lst[root]
            root = child
        else:
            break


HeapSort(lst)
# print('Сортировка кучей',lst)

################ 3 ################# Быстрая сортировка

def quick_sort(lst):
    if len(lst) > 1:
        x = lst[random.randint(0, len(lst)-1)]
        low = [i for i in lst if i < x]
        eq = [i for i in lst if i == x]
        hi = [i for i in lst if i > x]
        lst = quick_sort(low) + eq + quick_sort(hi)

    return lst


quick_sort(lst)
# print('Быстрая сортировка',lst)

################# 4 ##################### Оладушки

pancakes = [random.randint(1,10) for i in range(10)]
print(pancakes)

def pankSort(pancakes):
    # на первом заходе переворачивается вся стопка
    index_max = pancakes.index(max(pancakes[0:]))
    start = pancakes[:index_max+1]
    start.reverse()                     # Первое переворачивание от максимального блина
    end = pancakes[index_max+1:]
    pancakes = start + end
    pancakes = pancakes[::-1]   #Второе переворачивание всей стопки чтобы максимальный оказался снизу
    count = 2                   # Получается, нужно два переворачивания для отсортировки одного блина
    i = 1
    # Дальше в цикле каждый круг переворачивается стопка за минусом i отсортированных блинов снизу
    while pancakes != sorted(pancakes):
        index_max = pancakes.index(max(pancakes[0:-i]))
        start = pancakes[:index_max + 1]
        start.reverse()
        count+=1
        end = pancakes[index_max + 1:]
        pancakes = start + end
        pancakes = pancakes[-1-i::-1] + pancakes[0-i:]
        count+=1
        i+=1
    print('Количество переворачиваний: ',count)
    print('Отсортированные оладьи: ',pancakes)


pankSort(pancakes)





