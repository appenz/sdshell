#
# Stable Diffusion Shell
# Tool to automate SD workflow. For now just re-sizes images.
#
# (c) in 2022 by Guido Appenzeller

import sys
import os
import click
import tqdm
from PIL import Image

# Take the largest possible square from the center of the image  
# Right now, only works with square dimensions

def crop_center(img, tWidth, tHeight):
    width, height = img.size   # Get dimensions
    x = min(width, height)/2
    cx, cy = (width/2, height/2)
    tmp = img.crop((cx-x, cy-x, cx+x, cy+x))
    return tmp.resize((tWidth, tHeight), Image.Resampling.LANCZOS)

@click.command()
@click.option("--srcdir", help="Source directory for the raw, unformatted images.")
@click.option("--traindir", help="Storage directory for the resized training images.")
@click.option("--trainwidth", help="Training image width, needs to be same as height.", default=512)
@click.option("--trainheight", help="Training image height, needs to be same as width.", default=512)
@click.option("--iname", help="Name for the new instance that the model should be trained for.")

def sdshell(srcdir, traindir, trainwidth, trainheight, iname):
    """Resizes images to 512x512 pixels and stores them in the training directory."""

    if srcdir is None:
        srcdir = os.getcwd()
        traindir = os.getcwd()

    files = os.listdir(srcdir)
    print(f'Resizing {len(files)} files in {srcdir}.')
    i = 0
    for filename in tqdm.tqdm(files):
        print(filename)
        # Skip files that don't end with .png, .jpg or .jpeg
        if not filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            continue
        # Skip files that contain "sdcrop" in the filename
        if "sdcrop" in filename:
            continue
        
        img = Image.open(os.path.join(srcdir, filename))
        img = img.convert('RGB')
        out = crop_center(img,trainwidth,trainheight)

        if iname is not None:
            fname_out = iname+" ("+str(i)+")"
        else:
            fname_out = os.path.splitext(filename)[0]+"-sdcrop"
        print(fname_out)
        fname_out = os.path.join(traindir, fname_out+".jpeg")
        out.save(fname_out, "jpeg")
        i = i+1

if __name__ == '__main__':
    sdshell()