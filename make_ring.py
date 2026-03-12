import numpy as np
from PIL import Image
import os
import traceback

print("Starting ring radial texture generation...")
img_path = r"solar_system/planets/static/planets/textures/saturn_ring.jpg"
out_path = r"solar_system/planets/static/planets/textures/saturn_ring_2d.jpg"

try:
    img = Image.open(img_path).convert('RGB')
    L = 1024
    img_1d = img.resize((L, 1))
    strip = np.array(img_1d)[0]
    
    out_size = 2 * L
    Y, X = np.ogrid[0:out_size, 0:out_size]
    center = L
    dist_from_center = np.sqrt((X - center)**2 + (Y - center)**2)
    
    indices = dist_from_center.astype(int)
    mask = indices < L
    
    out_arr = np.zeros((out_size, out_size, 3), dtype=np.uint8)
    out_arr[mask] = strip[indices[mask]]
    
    out_img = Image.fromarray(out_arr)
    out_img.save(out_path, quality=85)
    print(f"Successfully saved 2D ring to {out_path}")
except Exception as e:
    print(f"Error: {e}")
    traceback.print_exc()
