import numpy as np

def cal_percentile(data,percent):
    return np.percentile(data,percent)

if __name__ == "__main__":
    # Get user input for uniform distribution parameters
    low = float(input("Enter the lower bound: "))
    high = float(input("Enter the upper bound: "))
    size = int(input("Enter the number of random values: "))

    # Generate random numbers
    x = np.random.uniform(low, high, size)
    n = int(input("Give percent to find the values are lower than: "))

    # Print results
    print(f"Percentile is {cal_percentile(x,n)}")