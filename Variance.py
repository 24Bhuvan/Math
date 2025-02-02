import numpy

def variance(arr):
    return numpy.var(arr)

if __name__=="__main__":
    n=int(input("Enter size of array: "))
    ls=[]
    for i in range(n):
        item=int(input(f"Enter your {i} element: "))
        ls.append(item)
    print(variance(ls))