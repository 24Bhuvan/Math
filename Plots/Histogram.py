import numpy as np
import matplotlib.pyplot as plt

if __name__=="__main__":
     # Get user input for uniform distribution parameters
    low = float(input("Enter the lower bound: "))
    high = float(input("Enter the upper bound: "))
    size = int(input("Enter the number of random values: "))

    # Generate random numbers
    x = np.random.uniform(low, high, size)
    n = int(input("Enter number of bars to plot: "))
    
    #Plot the data
    plt.hist(x,n)
    plt.show()