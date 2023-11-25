import napari
import tifffile as tiff
import imageio

# Load images
image1 = tiff.imread('MAX_D09_F49_Ch01.tif')
image2 = tiff.imread('MAX_D09_F49_Ch02.tif')
image3 = tiff.imread('MAX_D09_F49_Ch03.tif')
image4 = tiff.imread('MAX_D09_F49_Ch04.tif')

# Create a viewer
viewer = napari.Viewer()

# Add images as seperate layers and set blending to 'additive'
layer1 = viewer.add_image(image1, name='Layer 1', blending='additive', colormap='yellow')
layer2 = viewer.add_image(image2, name='Layer 2', blending='additive', colormap='red')
layer3 = viewer.add_image(image3, name='Layer 3', blending='additive', colormap='blue')
layer4 = viewer.add_image(image4, name='Layer 4', blending='additive', colormap='green')

napari.run()