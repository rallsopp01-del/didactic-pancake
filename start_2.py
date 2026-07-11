# Open the input file and read lines
import glob
pattern = '*xyz'

file = glob.glob(pattern)

with open(file[0], 'r') as file:
    lines = file.readlines()



with open('txt.inp', 'w') as outfile:
    for line in lines:
        # Strip any leading or trailing whitespace
        line = line.strip()
        
        # Split the line into words
        words = line.split()
        
        if words:
            # Replace the first word with its first letter only
            words[0] = words[0][0]
            # Rejoin the modified line
            modified_line = ' '.join(words)
            outfile.write(modified_line + '\n')
        else:
            # If line is empty, write a newline character
            outfile.write('\n')


