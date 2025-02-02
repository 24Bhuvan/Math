import numpy

def std_dev(arr):
    return numpy.std(arr)

if __name__=="__main__":
    n=int(input("Enter size of array: "))
    ls=[]
    for i in range(n):
        item=int(input(f"Enter your {i} element: "))
        ls.append(item)
    print(std_dev(ls))