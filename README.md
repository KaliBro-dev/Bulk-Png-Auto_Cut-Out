​1. Setup Your Environment
​Before running the tool, you must install the necessary Python libraries on your computer.
​Install Python: Ensure Python is installed on your system.  
​Install Dependencies: Open your terminal or command prompt in the project folder and run:
pip install -r requirements.txt. This installs rembg (for background removal) and Pillow (for image handling).


​2. Prepare Your Folders
​The script is designed to look for specific folder names to automate the "batch" process:
​Input Folder: Create a folder named input_images. Place all the JPG or PNG photos you want to cut into this folder.
​Output Folder: The script will automatically create an output_images folder if it doesn't already exist.


​3. Run the Automation
​Execute the script by running python main.py in your terminal.
​The tool will "iterate" through every image in your input folder, remove the background using AI, and save a new version in the output folder.
​The results will be transparent PNG files, which are perfectly formatted for use in Silhouette Studio without needing manual clipping in Photoshop.  