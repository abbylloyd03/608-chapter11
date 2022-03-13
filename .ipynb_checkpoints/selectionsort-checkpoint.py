# selectionsort.py
"""Sorting an array with selection sort."""
import numpy as np
from ch11utilities import print_pass

def selection_sort(data):
    """Sort array using selection sort."""
    # loop over len(data) -1 elements
    for index1 in range(len(data)-1):
        smallest = index1 # first index of remaining array
        
        # loop to find index of smallest element
        for index2 in range(index1 + 1, len(data)):
            if data[index2] < data[smallest]:
                smallest = index2
        
        # swap smallest element into position
        data[smallest], data[index1] = data[index1], data[smallest]
        print_pass(data, index1 + 1, smallest)
        
def main():
    data = np.array([35, 73, 90, 65, 23, 86, 43, 81, 34, 58])
    print(f'Unsorted array: {data}\n')
    selection_sort(data)
    print(f'\nSorted array: {data}\n')
    
# call main if this file is executed as a script
if __name__ == '__main__':
    main()