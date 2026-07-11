def remove_lines_with_pattern(file_path, pattern=" 0.0 "):
    # Read all lines from the file
    with open(file_path, 'r') as file:
        lines = file.readlines()
    # Filter out lines that start with the specified pattern
    filtered_lines = [line for line in lines if not line.startswith(pattern)]
    # Write the filtered lines back to the file
    with open("r2a_filtered.txt", 'w') as file:
        file.writelines(filtered_lines)

# Usage
file_path = 'r2a.txt'  # Replace with your file path
remove_lines_with_pattern(file_path)