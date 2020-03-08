import os
import logging
import numpy as np
from PIL import Image
from roipoly import RoiPoly
import matplotlib.image as img
from matplotlib import pyplot as plt

def loadImagesInToVector(folder, imageNames):
    images = {}
    for i in range(len(imageNames)):
        image = img.imread(os.path.join(folder, imageNames[i]))
        images[imageNames[i]] = image
    return images

logging.basicConfig(format='%(levelname)s ''%(processName)-10s : %(asctime)s '
                           '%(module)s.%(funcName)s:%(lineno)s %(message)s',
                    level=logging.INFO)
trainImageNames = os.listdir('C:/Users/Anvitha/PycharmProjects/HCI/train_images')
images = loadImagesInToVector('C:/Users/Anvitha/PycharmProjects/HCI/train_images', trainImageNames)
print(len(images))

for imagename, image in images.items():
    fig = plt.figure()
    plt.imshow(image)
    plt.colorbar()
    plt.title("left click: line segment         right click or double click: close region")
    plt.show(block=False)
    roi1 = RoiPoly(color='r', fig=fig)
    mask = roi1.get_mask(image)
    img = Image.fromarray(mask)
    img.save(os.path.join('C:/Users/Anvitha/PycharmProjects/HCI/mask/',imagename))
   


