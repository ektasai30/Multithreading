import threading
import random
import time

# normal single thread merge sort 
def mergesort(arr):
    if len(arr)<=1:
        return arr
        
    m=len(arr)//2
    lef=arr[0:m]
    rig=arr[m:len(arr)]
    mergesort(lef)
    mergesort(rig)
    i=j=k=0
    while i<len(lef) and j<len(rig):
        if lef[i]<rig[j]:
            arr[k]=lef[i]
            i+=1
        else:
            arr[k]=rig[j]
            j+=1
        k+=1
    while i<len(lef):
        arr[k]=lef[i]
        i+=1
        k+=1
    while j<len(rig):
        arr[k]=rig[j]
        j+=1
        k+=1

# multi-thread mearge sort
def threaded_mergesort(arr):
  if len(arr)<=1:
        return arr
        
  m=len(arr)//2
  lef=arr[0:m]
  rig=arr[m:len(arr)]

#create two threads
  t1 = threading.Thread(target=threaded_mergesort, args=(lef,))
  t2 = threading.Thread(target=threaded_mergesort, args=(rig,))

  t1.start()
  t2.start()
  t1.join()
  t2.join()

  i=j=k=0
  while i<len(lef) and j<len(rig):
    if lef[i]<rig[j]:
      arr[k]=lef[i]
      i+=1
    else:
      arr[k]=rig[j]
      j+=1
    k+=1
  while i<len(lef):
    arr[k]=lef[i]
    i+=1
    k+=1
  while j<len(rig):
    arr[k]=rig[j]
    j+=1
    k+=1

def measure_time(sort_function, arr):
    start = time.time()
    sort_function(arr)
    end = time.time()
    return end - start


#main program
if __name__ == "__main__":
    #create a random list
    size = 5000
    arr = [random.randint(0, 100000) for _ in range(size)]
    arr_copy = arr.copy()

    #single-threaded
    time_single = measure_time(mergesort, arr)
    print(f"single-threaded Merge Sort Time: {time_single:.4f} seconds")

    #multi-threaded
    time_threaded = measure_time(threaded_mergesort, arr_copy)
    print(f"multi-threaded Merge Sort Time: {time_threaded:.4f} seconds")