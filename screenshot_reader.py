import os
import pytesseract
from PIL import Image

def extract_text_from_screenshots(screenshots_folder, output_folder):
    # Iterate through each folder inside the screenshots folder
    for website_folder in os.listdir(screenshots_folder):
        website_folder_path = os.path.join(screenshots_folder, website_folder)

        # Check if the item is a directory
        if os.path.isdir(website_folder_path):
            # Create corresponding folder structure in the output folder
            output_website_folder = os.path.join(output_folder, website_folder)
            os.makedirs(output_website_folder, exist_ok=True)

            # Iterate through screenshot files inside the website folder
            for screenshot_file in os.listdir(website_folder_path):
                screenshot_file_path = os.path.join(website_folder_path, screenshot_file)

                # Check if the item is a file and ends with .png
                if os.path.isfile(screenshot_file_path) and screenshot_file.endswith('.png'):
                    # Read the screenshot image
                    with Image.open(screenshot_file_path) as img:
                        # Use Tesseract to extract text from the image
                        extracted_text = pytesseract.image_to_string(img)

                        # Save the extracted text to a text file in the corresponding output folder
                        text_file_path = os.path.join(output_website_folder, f"{screenshot_file[:-4]}.txt")
                        with open(text_file_path, 'w') as text_file:
                            text_file.write(extracted_text)

                            

# Define the input screenshots folder and output data folder
screenshots_folder = 'screenshots'
output_folder = 'data'
# Extract text from screenshots and save them to data folder
extract_text_from_screenshots(screenshots_folder, output_folder)