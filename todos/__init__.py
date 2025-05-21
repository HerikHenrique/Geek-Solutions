import os

# Get the absolute path of the current file
current_file_path = os.path.abspath(__file__)

# Get the directory of the current file
current_dir = os.path.dirname(current_file_path)

# Example usage
print(f"Current file path: {current_file_path}")
print(f"Current directory: {current_dir}")