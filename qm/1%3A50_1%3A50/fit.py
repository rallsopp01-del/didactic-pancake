import numpy as np
import sys
import pandas
from sklearn.linear_model import LinearRegression
import os

parent_dir = os.path.abspath(os.path.join(os.getcwd(), ".."))
file_path1 = os.path.join(parent_dir, "r2.txt")
file_path2 = os.path.join(parent_dir, "r2a.txt")

# Get the current working directory
current_dir = os.getcwd()
# Get the name of the current folder
current_folder_name = os.path.basename(current_dir)

im1=sys.argv[1]
im1=int(im1)
jm22 = sys.argv[2]
jm22 = int(jm22)

# Load the data
data = pandas.read_csv('fit.csv')
X = data.iloc[:, 0]  # (in the first column of fit.txt)
y = data.iloc[:, 1]  # (in the second column of fit.txt)

# Fit the linear model
model = LinearRegression()

n=400
adjusted_r2=0
while adjusted_r2 < 0.99:
	n -= 1 #update
	model.fit(X.values[:n].reshape(-1,1), y.values[:n].reshape(-1,1))
	r2=model.score(X.values[:n].reshape(-1,1), y.values[:n].reshape(-1,1))
	p=2
	n1 = X.shape[0]
	# Calculate Adjusted R2
	adjusted_r2 = 1 - (1 - r2) * (n1 - 1) / (n1 - p - 1)
	print(n, adjusted_r2)


if im1 != jm22:
    with open(file_path1, "a") as file:
        file.write(f"{str(r2)} {current_folder_name}\n" )

if im1 != jm22:
    with open(file_path2, "a") as file:
        file.write(f"{str(adjusted_r2)} {str(n)} {current_folder_name}\n")

