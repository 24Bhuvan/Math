import numpy

def percentile(arr,percentage_below):
    return numpy.percentile(arr,percentage_below)
    
if __name__=="__main__":
    Pb= int(input("Enter the percentage of the percentile to be calculated: "))
    n=int(input("Enter size of array: "))
    ls=[]
    for i in range(n):
        item=int(input(f"Enter your {i} element: "))
        ls.append(item)
    print(percentile(ls,Pb))