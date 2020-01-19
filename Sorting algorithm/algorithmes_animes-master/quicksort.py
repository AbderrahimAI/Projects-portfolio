#Implementing the quicksort algorithm as a seperate thread in parallel to the GUI mainloop
#otherwise mainloop and quicksort algorithm block each other

import threading
import time
import config

class Quicksort(threading.Thread):

    def __init__(self, display, arr):
        threading.Thread.__init__(self)
        self.display=display
        self.arr = arr
        self.start()


    def callback(self):
        #self.root.quit()
        pass

    def run(self):
        #This section gets executed in thread seperate from the mainloop
        self.quick_sort(self.arr, 0, len(self.arr)-1)

    #---------
    #Quicksort Algorithm using Median of 3
    #---------
    def quick_sort(self, A, low, hi):
        config.runvar = 1
        if low<hi:
            p = self.partition(A, low, hi)
            self.quick_sort(A, low, p-1)
            self.quick_sort(A, p+1, hi)
        config.runvar = 0

    def get_pivot(self, A, low, hi):
        mid = (hi + low)//2
        pivot = hi
        if A[low] < A[mid]:
            if A[mid] < A[hi]:
                pivot = mid
        elif A[low] < A[hi]:
            pivot = low
        return pivot

    def partition(self, A, low, hi):
        pivotIndex = self.get_pivot(A, low, hi)
        #Marker for current pivot Index
        config.pivot = pivotIndex
        pivotValue = A[pivotIndex]
        A[pivotIndex], A[low] = A[low], A[pivotIndex]
        time.sleep(config.speeds[config.speedind])
        border = low
        for i in range(low, hi+1):
            #Marker for current position
            config.currentPos = i
            if A[i] < pivotValue:
                border += 1
                A[i], A[border] = A[border], A[i]
                #self.mygui.sortedLabel.configure(text=A)
                time.sleep(config.speeds[config.speedind])
        A[low], A[border] = A[border], A[low]
        time.sleep(config.speeds[config.speedind])
        return border
    # ---------
    #End ofQuicksort Algorithm
    # ---------

