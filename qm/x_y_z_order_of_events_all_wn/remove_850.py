import csv

# File paths
input_file_path = 'intenslist.csv'
output_file_path = 'intenslist.csv'

# Read data from the CSV file
with open(input_file_path, mode='r') as infile:
    reader = csv.reader(infile)
    # Skip the header row
    next(reader)
    # Convert data to a list of tuples
    data = [(float(row[0]), float(row[1])) for row in reader]

# Filter rows where the first column is greater than or equal to 850
filtered_data = [row for row in data if row[0] >= 850]

# Write the filtered data to a new CSV file
with open(output_file_path, mode='w', newline='') as outfile:
    writer = csv.writer(outfile)
    # Optionally write the header row
    writer.writerow(['Column1', 'Column2'])
    writer.writerows(filtered_data)