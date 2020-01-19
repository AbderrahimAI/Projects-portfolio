#Implementing the insertionsort algorithm as a seperate thread in parallel to the GUI mainloop
#otherwise mainloop and insertionsort algorithm block each other

import threading
import time
import config

class Insertionsort(threading.Thread):

    def __init__(self, display, arr):
        threading.Thread.__init__(self)
        self.arr = arr
        self.start()


    def callback(self):
        #self.root.quit()
        pass

    def run(self):
        #This section gets executed in thread seperate from the mainloop
        self.insertionSort(self.arr)


    # Function to do insertion sort
    def insertionSort(self, arr):
        # Traverse through 1 to len(arr)
        config.runvar = 1
        for i in range(1, len(arr)):

            key = arr[i]

            # Move elements of arr[0..i-1], that are
            # greater than key, to one position ahead
            # of their current position
            j = i - 1
            while j >= 0 and key < arr[j]:
                config.currentElement = j
                arr[j + 1] = arr[j]
                time.sleep(config.speeds[config.speedind])
                j -= 1
            arr[j + 1] = key
        config.runvar = 0
