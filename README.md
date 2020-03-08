# Helper-Utilities-for-image-processing
adding useful scripts used during various image processing projects

1. roipoly_mask_images

Uses the roiploy package : https://github.com/jdoepfert/roipoly.py
Loads images from a folder and lets user to draw a polygon to select the region of interest. This produces a mask where all the pixels within the polygon will be 1's and outside the polygon will be 0's. Masked images are stored in a result folder.
Input images are in : train_images and output images are in : masked_images

