#!/usr/bin/env python3

import os
from PIL import Image

# Input and output directories
directory = "images/"
output_directory = "/opt/icons"

# For loop to make updates and save images
for file in os.listdir(directory):
    im = Image.open(os.path.join(directory, file)) # Open image
    im = im.rotate(-90) # Rotate image 90 degrees
    im = im.resize((128, 128)) # Resize image to 128x128
    im.save(os.path.join(output_directory, file+".jpeg")) # Save the image to new folder as .jpeg