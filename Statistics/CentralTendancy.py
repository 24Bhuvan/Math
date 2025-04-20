import numpy as np
from scipy import stats

def central_tendancy(data):
    mean_val = np.mean(data)
    median_val = np.median(data)
    mode_val = stats.mode(data, keepdims=True).mode[0]  

    return mean_val, median_val, mode_val

if __name__ == "__main__":
    # Get user input for uniform distribution parameters
    low = float(input("Enter the lower bound: "))
    high = float(input("Enter the upper bound: "))
    size = int(input("Enter the number of random values: "))

    # Generate random numbers
    x = np.random.uniform(low, high, size)

    # Call the function and print results
    mean_x, median_x, mode_x = central_tendancy(x)
    print("\nStatistics:")
    print("Mean:", mean_x)
    print("Median:", median_x)
    print("Mode:", mode_x)