from PIL import Image
import os

# Set the directory to your specific path
directory = r"C:\path_to_your_files" #Set working file path, converts all webp files in this path

# Loop through all files in the specified directory
for filename in os.listdir(directory):
    if filename.endswith(".webp"):
        # Construct the full file path
        file_path = os.path.join(directory, filename)

        # Open the .webp image
        with Image.open(file_path) as img:
            # Define the new filename, replacing .webp with .jpg
            new_filename = filename[:-5] + ".jpg"
            new_file_path = os.path.join(directory, new_filename)

            # Convert and save the image as .jpg
            img.convert('RGB').save(new_file_path, "JPEG")

            print(f"Converted {filename} to {new_filename}")

print("Conversion complete.")
