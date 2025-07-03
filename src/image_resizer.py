"""
image_resizer.py

🔹 Description:
This script automates the process of resizing and converting images in batch using the Pillow (PIL) library.
It scans all images in the 'input_images' folder, resizes them to 800x800 pixels, converts them to JPEG format,
and saves them into the 'output_images' folder.

🔹 Key Features:
- Supports common image formats (.jpg, .jpeg, .png, .bmp, .gif)
- Automatically creates output directory if not found
- Provides success messages in terminal for each image resized
- Can handle multiple images in one run

🔹 Technologies Used:
- Python 3
- Pillow (PIL)
- os module for file handling

🔹 Author: Rohith K N
🔹 Internship Task: Task 7 – Image Resizer Tool
🔹 Date: July 2025
"""


import os
from PIL import Image

# Input and Output Directories
INPUT_FOLDER = "../input_images"
OUTPUT_FOLDER = "../output_images"
RESIZE_SIZE = (800, 800)  # Resize to 800x800

# Creating output folder if it doesn't exist
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Supported formats
SUPPORTED_FORMATS = (".jpg", ".jpeg", ".png", ".bmp", ".gif")

# Process all images
for filename in os.listdir(INPUT_FOLDER):
    if filename.lower().endswith(SUPPORTED_FORMATS):
        input_path = os.path.join(INPUT_FOLDER, filename)
        output_path = os.path.join(OUTPUT_FOLDER, f"{os.path.splitext(filename)[0]}_resized.jpg")

        try:
            with Image.open(input_path) as img:
                # Resize and convert to RGB for consistency
                img = img.convert("RGB")
                img_resized = img.resize(RESIZE_SIZE)
                img_resized.save(output_path, "JPEG")
                print(f"[✔] Resized: {filename}")
        except Exception as e:
            print(f"[✘] Failed: {filename} -> {e}")


