import pandas as pd
import pandas
import numpy as np
import numpy
import os






def find_first_line_with_words(filename, words):
    # Open the file in read mode
    with open(filename, 'r') as file:
        # Iterate through each line in the file
        for line_number, line in enumerate(file, start=1):
            # Check if all words are in the current line
            if all(word in line for word in words):
                # Return the line number and the line
                return line_number, line.strip()
    # If no line is found, return None
    return None


# Find the line just above the inactive lines
filename = 'freq.out'
words = ['  0          1          2          3          4          5   ']
result = find_first_line_with_words(filename, words)

# Find the line just above the inactive lines
filename = 'freq.out'
words = ['L/(mol*cm)']
result2 = find_first_line_with_words(filename, words)



with open(filename, 'r') as file:
    lines = file.readlines()


extracted_lines = lines[result[0]-1:result2[0]-7]
output_file = 'output.txt'
# Write the extracted lines to the output file
with open(output_file, 'w') as file:
    file.writelines(extracted_lines)


# Step 1: Read the data from the text file, skipping index label columns
file_path = 'output.txt'

# Read the data from the file and handle rows with unexpected number of columns
data = []
with open(file_path, 'r') as file:
    for line in file:
        row = line.split()
        # Assume that the first column is an index label, and we skip it
        if len(row) >= 7:  # Considering there can be more columns but we need 6 numerical values
            data.append([float(value) for value in row[1:7]])  # Skip the first column (index label)


submatrix_rows=int(lines[result2[0]-9].strip()[0:3])+1 #add the number 1 to the value
data=np.array(data)
submatrices = [data[i:i + submatrix_rows] for i in range(0, data.shape[0], submatrix_rows)]
final_matrix = np.hstack(submatrices)
final_matrix1 = pandas.DataFrame(final_matrix) # M(i,j) defined

#
#averaging the three X,Y,Z displacements into one score ################should be sqrt(X^2+Y^2+Z^2)
#

# Create a new DataFrame to store the results
averaged_df = pd.DataFrame()
averaged_df = averaged_df[0:198-60]

averaged_df = [] #Creates the Snm(k,j)
# Iterate through the columns and calculate the mean for each group of 3 rows
for col in final_matrix1.columns:
    # Group every three rows and calculate the mean
    #averaged_col = final_matrix1[col].abs().groupby(np.arange(len(final_matrix1)) // 3).mean() #need to make this cartesian#####################
    grouped = final_matrix1[col].groupby(np.arange(len(final_matrix1)) // 3)
    # Compute sqrt(x^2 + y^2 + z^2) for each group of three rows
    averaged_col = grouped.apply(lambda group: np.sqrt(np.sum(group**2)))
    # Add the averaged column to the new DataFrame
    #averaged_df[col] = averaged_col
    averaged_df.append(averaged_col)


averaged_df = pd.concat(averaged_df, axis=1)


print(averaged_df.shape)

#
#averaging the three X,Y,Z displacements into one score
#

normalized_df = averaged_df.div(averaged_df.sum(axis=0), axis=1)

#final_matrix1.iloc[:,(len(normalized_df.T)-414):len(normalized_df.T)]

#This is the final line of code that is the displacements matrix
averaged_df.iloc[:,(len(normalized_df.T)-414):len(normalized_df.T)]












# Find the line just below the IR spectrum start
filename = 'freq.out'
words = ['L/(mol*cm)']
result = find_first_line_with_words(filename, words)



# Find the line below end lines
#* The epsilon (eps) is given for a Dirac delta lineshape.

words = ['*', 'The', 'epsilon', '(eps)', 'is', 'given', 'for', 'a', 'Dirac', 'delta', 'lineshape']
result2 = find_first_line_with_words(filename, words)


with open(filename, 'r') as file:
    lines = file.readlines()


extracted_lines = lines[(result[0]+1):(result2[0]-2)]
output_file = 'ir_spectra.txt'
# Write the extracted lines to the output file
with open(output_file, 'w') as file:
    file.writelines(extracted_lines)


#column_means.sort_values(ascending=False).head(20)
#averaged_df.iloc[19,(len(normalized_df.T)-314):len(normalized_df.T)].sort_values(ascending=False).head(20)
#18 is the phosphate atom

#averaged_df.iloc[0:(0+138),(len(normalized_df.T)-314):len(normalized_df.T)]
#extracted_df=averaged_df.iloc[0:(0+138),:]
extracted_df=averaged_df.iloc[0:(0+138),(len(normalized_df.T)-414):len(normalized_df.T)]


#These lines from 150 down to 162 are equivilant to Cxi=sum from 0 to i (yi*xi)/ sum from 0 to i (yi)
normalized_df = extracted_df.div(extracted_df.sum(axis=0), axis=1)
df_zcoords = pd.read_csv('freq.activeRegion.xyz', header=1, delimiter=' ', skipinitialspace=True)
#to get this we need an updated recentered membrane around each lipid and use those positions here
df_zcoords_whole = pd.read_csv('memb.txt', header=None, delimiter=' ', skipinitialspace=True)
df_zcoords.iloc[:,3]
#The re-scaling occurs here with the offset of 40
#Here P(k,j)=df_zcoords.iloc[:,3]
df_zcoords=df_zcoords.iloc[:,3]-df_zcoords_whole.mean().values+40
z_shift=df_zcoords_whole.mean().values
#It can be useful to track the shift so that it can be undone
np.savetxt('z_shift.txt', z_shift, delimiter=',')
#c=normalized_df.multiply(df_zcoords.iloc[:,3], axis=0)  ##normalized_df
c=normalized_df.multiply(df_zcoords.values, axis=0)  ##normalized_df
#fraction of total motions// what is that
#
#This is the last step in the normalization
cm=c.sum()
cm.to_csv('ranked_modes_1.csv')


os.system("python orca-ir.py freq.out")
ranks = pd.read_csv('ranked_modes_1.csv',header=0, index_col=0)
gauss = pd.read_csv('intenslist.csv',header=0, index_col=0)
mr=ranks.iloc[len(ranks)-414:len(ranks)]
#********Need to erase the normal modes that are not actually counted in the spectra *****check this line of code**
mg=gauss.values
ranked_gaussians=np.array(mr.iloc[414-len(mg):len(mr)])*mg
ranked_gaussians=ranked_gaussians[1:len(ranked_gaussians)]
ranked_gaussians=pandas.DataFrame(ranked_gaussians)
ranked_gaussians.to_csv('ranked_gaussians.csv')
summation_ranked_wn=ranked_gaussians.sum(axis=0)
rankedsum=ranked_gaussians
gausssum=gauss.iloc[1:len(gauss)]
int_dist=pandas.DataFrame(np.divide(np.array(rankedsum), np.array(gausssum)))
int_dist=int_dist.iloc[4:len(int_dist)]
int=gausssum
input_2d=pd.concat([int.iloc[5:len(int)].reset_index(drop=True), rankedsum.iloc[5:len(int)].reset_index(drop=True)], axis=1)
input_2d.index=gauss.index[6:len(gauss)]

input_2d.to_csv('2t2d_input_z.csv')

os.system("python 2Dpy_z.py")

spec1 = pandas.read_csv('ref_gaussians_z.csv', header=0, index_col=0).T
int_dist=int_dist.iloc[1:len(int_dist)]
int_dist.index=spec1.T.index

out_count_dist=pd.concat([spec1.T, int_dist], axis=1)
out_count_dist.to_csv('count_dist_z.csv')








