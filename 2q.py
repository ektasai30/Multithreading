import threading
import random
import time

#normal single thread
def quicksort(arr):
    if len(arr)<=1:
        return arr
    n = len(arr)
    pivot=arr[n-1]
    x=[i for i in arr if i<pivot]
    middel=[pivot]
    y=[j for j in arr if j>pivot]
    return quicksort(x)+middel+quicksort(y)


#multi thread 
def threaded_quicksort(arr):
    if len(arr)<=1:
        return arr
    n = len(arr)
    pivot=arr[n-1]
    pivot=arr[n-1]
    x=[i for i in arr if i<pivot]
    middel=[pivot]
    y=[j for j in arr if j>pivot]

    left=[]
    right=[]

    def sort_left():
        left.extend(threaded_quicksort(x))
    def sort_right():
        right.extend(threaded_quicksort(y))

    t1=threading.Thread(target=sort_left)
    t2=threading.Thread(target=sort_right)

    t1.start()
    t2.start()
    t1.join()
    t2.join()
    return left+middel+right


if __name__ == "__main__":
    size = 5000
    arr = [random.randint(0, 1000000) for _ in range(size)]
    arr_copy = arr.copy()

    start = time.time()
    sorted_arr = quicksort(arr)
    print(f"Single-threaded quicksort: {time.time() - start:.4f} seconds")

    start = time.time()
    sorted_arr2 = threaded_quicksort(arr_copy)
    print(f"Multi-threaded quicksort: {time.time() - start:.4f} seconds")