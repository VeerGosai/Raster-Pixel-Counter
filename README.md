# 🌍 Raster Class Pixel Counter

This simple Python script reads a raster file (GeoTIFF format) and counts the number of pixels per class, ignoring `NoData` values. It's useful for analyzing land cover classifications or other raster-based datasets.

## 📦 Requirements

Ensure the following Python packages are installed:

```bash
pip install rasterio numpy
```

## 📝 Usage

1. Place your raster file (e.g., `file.tif`) in the same directory as the script.
2. Update the `raster_path` variable if needed.
3. Run the script:

```bash
python count_pixels.py
```

## 📜 Script

```python
import rasterio
import numpy as np

raster_path = "file.tif"

with rasterio.open(raster_path) as src:
    band = src.read(1)  # Read the first band

# Remove NoData values
band = band[band != src.nodata]

# Count unique class values
unique, counts = np.unique(band, return_counts=True)

print("Pixel counts by class:")
for value, count in zip(unique, counts):
    print(f"Class {int(value)}: {count} pixels")
```

## 📈 Example Output

```
Pixel counts by class:
Class 1: 15823 pixels
Class 2: 9127 pixels
Class 3: 4873 pixels
```

## 🧠 Notes

- This script reads only the **first band** of the raster.
- It assumes the raster has integer values representing class IDs (e.g., land cover types).

This script was created for use in a Stellenbosch University GIT 211 Classification assignment
