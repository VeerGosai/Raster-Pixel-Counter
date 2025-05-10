import rasterio
import numpy as np

raster_path = "file.tif"

with rasterio.open(raster_path) as src:
    band = src.read(1) 

band = band[band != src.nodata]
unique, counts = np.unique(band, return_counts=True)

print("Pixel counts by class:")
for value, count in zip(unique, counts):
    print(f"Class {int(value)}: {count} pixels")
