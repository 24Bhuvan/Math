import numpy
from scipy import stats

def mean(arr):
    return numpy.mean(arr) 
def median(arr):
    return numpy.median(arr)
def mode(arr):
    return stats.mode(arr)
    
if __name__=="__main__":
    n=int(input("Enter size of array: "))
    ls=[]
    for i in range(n):
        item=int(input(f"Enter your {i} element: "))
        ls.append(item)
    print(mean(ls))
    print(median(ls))
    print(mode(ls))