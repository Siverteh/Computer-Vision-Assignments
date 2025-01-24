import os

def print_txt_files(directory):
    """
    Reads and prints the contents of all .txt files in the specified directory.

    Args:
        directory (str): Path to the directory containing .txt files.
    """
    # Check if directory exists
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return

    # Iterate through all files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)
            try:
                # Print filename as header
                print(f"\n=== {filename} Contents ===")
                
                # Read and print the file contents
                with open(file_path, 'r', encoding='utf-8') as file:
                    print(file.read())
                    
                print("=" * (len(filename) + 15))  # Print footer line
                
            except Exception as e:
                print(f"Error reading {file_path}: {e}")

# Example usage
if __name__ == "__main__":
    # Replace this with your directory path
    target_directory = r"C:\path\to\your\txt\files"
    print_txt_files(target_directory)
