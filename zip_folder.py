import shutil
import os

def zip_folder(folder_path, output_zip_path):
    """
    Zips a folder and saves it to the specified output path.

    Parameters:
        folder_path (str): Path to the folder to be zipped.
        output_zip_path (str): Path where the zip file will be saved (including the filename).
    """
    try:
        # Ensure the folder exists
        if not os.path.exists(folder_path):
            raise FileNotFoundError(f"The folder '{folder_path}' does not exist.")

        # Create the zip archive
        shutil.make_archive(output_zip_path, 'zip', folder_path)
        print(f"Folder '{folder_path}' successfully zipped to '{output_zip_path}.zip'.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
folder_to_zip = "src/Practical Three"  # Replace with the path to your folder
output_zip_file = "Practical Three"  # Replace with the desired output path (without .zip extension)

zip_folder(folder_to_zip, output_zip_file)