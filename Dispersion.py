import numpy as np

# Range
def calculate_range(data):
    return np.max(data) - np.min(data)

# Standard Deviation (sample standard deviation, so ddof=1)
def calculate_std(data):
    return np.std(data)

# Variance (sample variance, so ddof=1)
def calculate_var(data):
    return np.var(data)

# Coefficient of Variation (CV)
def calculate_coeff_var(data):
    mean_val = np.mean(data)
    return (calculate_std(data) / mean_val) * 100 if mean_val != 0 else None

# Interquartile Range
def cal_iqr(data):
    return abs(np.percentile(data,25) - np.percentile(data,75))

if __name__ == "__main__":
    # Get user input for uniform distribution parameters
    low = float(input("Enter the lower bound: "))
    high = float(input("Enter the upper bound: "))
    size = int(input("Enter the number of random values: "))

    # Generate random numbers
    x = np.random.uniform(low, high, size)

    # Calculate measures of dispersion
    range_x = calculate_range(x)
    std_x = calculate_std(x)
    var_x = calculate_var(x)
    covar_x = calculate_coeff_var(x)
    iqr_x = cal_iqr(x)

    # Print results
    print("\nMeasures of Dispersion:")
    print("Range:", range_x)
    print("Standard Deviation:", std_x)
    print("Variance:", var_x)
    print("Coefficient of Variation:", covar_x)
    print("Interquartile range", iqr_x)