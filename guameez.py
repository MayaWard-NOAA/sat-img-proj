# Script for guam eez

import geopandas as gpd

# get current filepath
# print(os.getcwd())

# set current working directory
# os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 
guam = gpd.read_file('data/maps/guam_eez.shp')
guam.plot()

