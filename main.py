import os
from rembg import remove
from PIL import Image

def bulk_remove_background(input_folder, output_folder):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Process each image in the folder
    for filename in os.listdir(input_folder):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            print(f"Processing: {filename}")
            
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}_cut.png")

            # Open image and remove background
            with open(input_path, 'rb') as i:
                input_image = i.read()
                output_image = remove(input_image)
                
                with open(output_path, 'wb') as o:
                    o.write(output_image)

    print("Success: All images processed.")

if __name__ == "__main__":
    # Update these paths for your local setup
    input_dir = 'input_images'
    output_dir = 'output_images'
    bulk_remove_background(input_dir, output_dir)
