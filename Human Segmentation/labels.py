import numpy as np
import imageio as ii
from PIL import Image
nxb_img   = Image.open('datasets/CIHP/images/000001_0.jpg')      # This is your image.
 
# Reshape their label image to our size 
label_img = Image.open('datasets/CIHP/labels/0005008.png')  # This is the label image from CIHP.
nxb_label_img = label_img.resize(nxb_img.size, Image.NEAREST)
nxb_label_img.save('datasets/CIHP/labels/000001_0.png')

# Reshape their edge image to our size 
edge_img  = Image.open('datasets/CIHP/edges/0005008.png')
nxb_edge_img  = edge_img.resize(nxb_img.size, Image.NEAREST)
nxb_edge_img.save('datasets/CIHP/edges/000001_0.png')