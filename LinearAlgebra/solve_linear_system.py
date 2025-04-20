#Solve System Linear Equations with this code
import numpy as np

n = int(input("Enter Number of input variable: "))
print("Coefficient matrix: ")
A = np.array([list(map(float,input(f"Row {i+1}: ").split())) for i in range(n)])
print("Constant matrix: ")  
B = np.array(list(map(float, input("Enter the constants: ").split())))

x=np.linalg.solve(A,B)
print("\nSolution:")
for i, val in enumerate(x):
    print(f"x{i+1} = {val}")