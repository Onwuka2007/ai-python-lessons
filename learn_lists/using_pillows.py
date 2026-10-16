import sys
from PIL import Image

images = []

# Loop through all command-line arguments passed after the script name
for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

# Save the first image, append the rest, and set animation parameters
if len(images) > 1:
    images[0].save(
        "output.gif", save_all=True, append_images=images[1:], duration=200, loop=0
    )
    print("GIF created successfully as output.gif!")
else:
    print("Please provide at least two images to create a GIF.")

# python -u learn_lists\using_pillows.py data/raw-images/cos1.jpg data/raw-images/cos2.jpg
