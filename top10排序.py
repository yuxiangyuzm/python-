import random

def sift(data,low,high):
    i=low
    j=2*i+1
    tmp = data[i]
    while j<=high:
        if j+1 <= high and data[j] > data[j+1]:
            j += 1
        if data[j] < tmp:
            data[i] = data[j]
            i = j
            j = 2*i + 1
        else:
            break
    data[i] = tmp
def topn(li,n):
    heap = li[0:n]
    for i in range(n//2-1,-1,-1):
        sift(heap,i,n-1)
    for i in range(n,len(li)):
        if li[i] > heap[0]:
            heap[0]=li[i]
            sift(heap,0,n-1)
    for i in range(n-1,-1,-1):
        heap[0],heap[i]=heap[i],heap[0]
        sift(heap,0,i-1)
    return heap

data = list(range(10000))
random.shuffle(data)
print(topn(data,10))
print(topk(data,10))