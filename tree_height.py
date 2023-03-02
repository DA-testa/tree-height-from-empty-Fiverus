# python3
# Vladislavs Fedins 221RDB416
import sys
import threading
import numpy


def compute_height(n, parents):
    paren = numpy.zeros(n)
    def height(i):
        if paren[i] != 0:
            return paren[i]
        if parents[i] == -1:
            paren[i] = 1
        else:
            paren[i] = height(parents[i])+1
        return paren[i]
    
    for i in range(n):
        height(i)
    return int(max(paren))


def main():
    # implement input form keyboard and from files
    input_type = input()

    if "F" in input_type:
        filename = input()
        if ".a" in filename:
            return
        if "test/" not in filename:
            filename = "test/" + filename
        if "test/" in filename:    
            with open(filename) as f:
                n = int(f.readline().strip())
                parents = list(map(int, f.readline().strip().split()))
                height = compute_height(n, parents)
    elif "I" in input_type:
        n = int(input())
        parents = list(map(int, input().split()))
        height = compute_height(n, parents)

    print(height)
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
