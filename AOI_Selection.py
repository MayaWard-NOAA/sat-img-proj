# This file opens raw satellite image downloads and translates it to a raster or aoi selection

## OUTSTANDING QUESTIONS : 
#### 1. How to code converting kml (googleEarth file) to shapefile
#### 2. How to code downloading kml file automatically : or will we already have these ? 
#### 3. 

# import libraries
import pandas as pd
import numpy as np

from rasterio.plot import show
from rasterio.merge import merge
import glob
import os
import matplotlib.pyplot as plt
import xarray as xr
import dask

# needed to use shapefile and crop raster image. 
import fiona
import rasterio
import rasterio.mask



# Convert kml to shapefile using Anaconda prompt. Ogr2ogr from GDAL/OGR
# ogr2ogr -f 'ESRI Shapefile' output.shp input.kml

# file:///C:/Users/Maya.Ward/AppData/Roaming/jupyter/runtime/nbserver-17352-open.html 
# above is file for jupyter-lab notebook

# return plt

# Write full file path to the jpg with the jpw in the same folder
# r means raw string (vs formatted string)
# Write file path relative to where python script is stored
""" comments comments blah
blah blah
paragraphs in comments
"""

fp = r'SEA1\\filename.jpg' # check syntax: need 1 or 2 \ ?
img = rasterio.open(fp)
show(img)

"""
Next Steps
** Commit to GitHub **
1. Merge into mosaic
2. Select AOI (area of interest)
3. Crop AOI with rasterio (select and crop one command?)
4. Save output file as another image file
5. Create functions!
"""

# merge into mosaic
## file and folder paths
dirpath = r"C:\Users\Maya.Ward\Documents\Projects\Satellite_Training\SEA1"
out_fp = r"C:\Users\Maya.Ward\Documents\Projects\Satellite_Training\SEA1\TEST\seattle_testchunk_mosaic.tif"

## make search criteria to select DEM files
search_criteria = "SEA1*.jpg"
q = os.path.join(dirpath, search_criteria)
print(q)

## list all dem files
dem_fps = glob.glob(q)
dem_fps

## create empty list for mosaic
src_files_to_mosaic = []
   


#check to see if looks ok
#  show(mosaic, cmap='terrain')

# check out tutorials for cropping with rasterio. do simple crop and save as another file

# Using rasterio with fiona, it is simple to open a shapefile, read geometries, and mask out regions of a raster that are outside the polygons defined in the shapefile
shapefile = r"C:\Users\Maya.Ward\Documents\Projects\Satellite_Training\SEA1\TEST\SEA_test.shp"
shape_path= os.path.join(dirpath, shapefile)
with fiona.open(shape_path, "r") as shapefile:
    shapes = [feature["geometry"] for feature in shapefile]

# This shapefile contains a single polygon, a box near the center of the raster, so in this case, our list of features is one element long
with rasterio.open(r"C:\Users\Maya.Ward\Documents\Projects\Satellite_Training\SEA1\TEST\seattle_testchunk_mosaic.tif") as src:
    out_image, out_transform = rasterio.mask.mask(src, shapes, crop=True)
    out_meta = src.meta

# Using plot and imshow from matplotlib, we can see the region defined by the shapefile in red overlaid on the original raster    

# use the updated spatial transform and raster height and width to write the masked raster to a new file
out_meta.update({"driver": "GTiff",
                 "height": out_image.shape[1],
                 "width": out_image.shape[2],
                 "transform": out_transform})

with rasterio.open("SEA_test_masked.tif", "w", **out_meta) as dest:
    dest.write(out_image)
 
# write above into a function? Feed function area of interest coordinates and it crops for you?



# Within a single jpg, select an area of interest and crop the file
## play with code to do this... ##

"""
########################################################################################################################
########################################################################################################################
# process from link: https://www.earthdatascience.org/courses/use-data-open-source-python/intro-raster-data-python/raster-data-processing/crop-raster-data-with-shapefile-in-python/
import os
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from shapely.geometry import mapping
import rioxarray as rxr
import xarray as xr
import geopandas as gpd

import earthpy as et
import earthpy.plot as ep

lidar_chm_path = os.path.join("colorado-flood", 
                              "spatial"
                              "boulder-leehill-rd",
                              "outputs",
                              "lidar_chm.tif")

lidar_chm_im = rxr.open_rasterio("colorado-flood/spatial/boulder-leehill-rd/outputs/lidar_chm.tif",
                                 masked=True).squeeze()

f, ax = plt.subplots(figsize=(10, 5))
lidar_chm_im.plot.imshow()
ax.set(title="Lidar Canopy Height Model (CHM)")

ax.set_axis_off()
plt.show()

# open layer vector
aoi = os.path.join("colorado-flood",
                   "spatial",
                   "boulder-leehill-rd",
                   "clip-extent.shp")

# Open crop extent (your study area extent boundary)
crop_extent = gpd.read_file(aoi)

print('crop extent crs: ', crop_extent.crs)
print('lidar crs: ', lidar_chm_im.rio.crs)
## crop extent crs:  epsg:32613
# lidar crs:  EPSG:32613
        
# Plot the crop boundary layer
# Note this is just an example so you can see what it looks like
# You don't need to plot this layer in your homework!
fig, ax = plt.subplots(figsize=(6, 6))

crop_extent.plot(ax=ax)

ax.set_title("Shapefile Crop Extent",
             fontsize=16)
plt.show()

# Now that you have imported the shapefile. You can use the crop_image function from earthpy.spatial to crop the raster data using the vector shapefile

f, ax = plt.subplots(figsize=(10, 5))
lidar_chm_im.plot.imshow(ax=ax)

crop_extent.plot(ax=ax,
                 alpha=.8)
ax.set(title="Raster Layer with Shapefile Overlayed")

ax.set_axis_off()
plt.show()

## Clip Raster Data Using RioXarray .clip
# If you want to crop the data you can use the rio.clip function. When you clip the data, you can then export it and share it with colleagues. Or use it in another analysis.

"""