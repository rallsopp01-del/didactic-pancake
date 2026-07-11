# Open the input file and read lines
import glob
pattern = 'upper.xyz'

file = glob.glob(pattern)

with open(file[0], 'r') as file:
    lines = file.readlines()

with open('txt.inp', 'w') as outfile:
    # Process each line
    for line in lines:
        # Check if there are double spaces in the line
        if '  ' in line:
            # Split the line into words
            words = line.split()
            # Replace the first word with its first letter only
            if words:  # Check if there are words to avoid index error
                words[0] = words[0][0]
            # Rejoin the modified line
            modified_line = ' '.join(words)
            outfile.write(modified_line + '\n')
        else:
            # If no double spaces, print the line as is
            outfile.write(line)