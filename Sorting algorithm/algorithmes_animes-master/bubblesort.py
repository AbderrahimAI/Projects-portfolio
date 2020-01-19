#Implementing the bubblesort algorithm as a seperate thread in parallel to the GUI mainloop
#otherwise mainloop and insertionsort algorithm block each other

import threading
import time
import config

class Bubblesort(threading.Thread):

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
        self.bubbleSort(self.arr)


    # Function to do insertion sort
    def bubbleSort(self, arr):
        n = len(arr)
        config.runvar = 1
        # Traverse through all array elements
        for i in range(n):

            # Last i elements are already in place
            for j in range(0, n - i - 1):
                config.bubbleElement=j+1
                # traverse the array from 0 to n-i-1
                # Swap if the element found is greater
                # than the next element
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                time.sleep(config.speeds[config.speedind])
        config.runvar = 0