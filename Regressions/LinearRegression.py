import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def parameters(data1,data2):
    global slope, intercept, r, p, std_err
    slope, intercept, r, p, std_err = stats.linregress(x,y)

def lin_func(query):
    return (slope*query)+intercept

if __name__=="__main__":
    # Get user input for uniform distribution parameters
    low = float(input("Enter the lower bound: "))
    high = float(input("Enter the upper bound: "))
    size = int(input("Enter the number of random values: "))

    # Generate random numbers
    x = np.random.uniform(low, high, size)
    y = np.random.uniform(low, high, size)
    
    # Building Model parameters
    parameters(x,y)
    myline = list(map(lin_func,x))

    # Ploting Section
    plt.scatter(x,y)
    plt.plot(x,myline)
    plt.show()

    # Querying Future values
    myfuture = int(input("Type 1 if want to Predict value: "))
    if myfuture == 1:
        qry =int(input ("Enter the number whose value is to be predicted: "))
        print(lin_func(qry))

    

