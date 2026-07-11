import numpy as np
import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import MinMaxScaler

# Define your matrices
y_obs = pd.read_csv('raw_data1.csv',header=0, index_col=None)
y_obs=y_obs.fillna(1)

data1=y_obs.iloc[0:400,0:3]
data2=y_obs.iloc[0:400,[4,5,3]]




data1_np=np.array(data1)
data2_np=np.array(data2)
#scaler = MinMaxScaler()

#scaler = StandardScaler()

#normalized_data1 = scaler.fit_transform(data1_np)
#normalized_data2 = scaler.fit_transform(data2_np)
normalized_data1=data1_np
normalized_data2=data2_np

#normalized_data1 = scaler.fit_transform(data1_np)
#normalized_data2 = scaler.fit_transform(data2_np)

# Fit the model on B
nbrs = NearestNeighbors(n_neighbors=1, metric_params={'w': [1,0,1]}).fit(normalized_data2)

# Find the nearest neighbors for A in B
distances, indices = nbrs.kneighbors(normalized_data1)

#distances, indices = nbrs.kneighbors(data1_np[0])
#distances, indices = nbrs.kneighbors(data1_np[10].reshape(1,-1))




min_value = np.min(distances)
min_row1 = np.where(distances == min_value)[0][0]  # Get the row index of the minimum value
distances2, indices2 = nbrs.kneighbors(data1_np[min_row1].reshape(1,-1))
min_row2 = indices2
new_mat = np.zeros((1,6))
new_mat = np.vstack([new_mat, np.concatenate((data1_np[min_row1],data2_np[min_row2][0,0])) ])
new_mat

data1_np = np.delete(data1_np, min_row1, axis=0)
data2_np = np.delete(data2_np, min_row2, axis=0)
normalized_data1 = np.delete(normalized_data1, min_row1, axis=0)
normalized_data2 = np.delete(normalized_data2, min_row2, axis=0)


for i in range(399):
    nbrs = NearestNeighbors(n_neighbors=1, metric_params={'w': [1,0,1]}).fit(normalized_data2)
    distances, indices = nbrs.kneighbors(normalized_data1)
    min_value = np.min(distances)
    min_row1 = np.where(distances == min_value)[0][0]  # Get the row index of the minimum value
    distances2, indices2 = nbrs.kneighbors(data1_np[min_row1].reshape(1,-1))
    min_row2 = indices2
    new_mat = np.vstack([new_mat, np.concatenate((data1_np[min_row1],data2_np[min_row2][0,0])) ])
    data1_np = np.delete(data1_np, min_row1, axis=0)
    data2_np = np.delete(data2_np, min_row2, axis=0)
    normalized_data1 = np.delete(normalized_data1, min_row1, axis=0)
    normalized_data2 = np.delete(normalized_data2, min_row2, axis=0)


pd.DataFrame(new_mat).to_csv('tmp.csv')



# Output the indices of the closest rows in B for each row in A
print(indices)







