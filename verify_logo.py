from PIL import Image
import os

def check_transparency(path):
    print(f"Checking {path}...")
    try:
        img = Image.open(path)
        print(f"Format: {img.format}")
        print(f"Mode: {img.mode}")
        
        if img.mode != 'RGBA':
            print("FAILED: Image is not RGBA")
            return

        # Check a few distinct points for transparency
        points = [
            (0, 0), (10, 10), # Corners likely transparent
            (img.width//2, img.height//2) # Center likely opaque
        ]
        
        for x, y in points:
             # Ensure coordinates are within bounds
            if x < img.width and y < img.height:
                pixel = img.getpixel((x, y))
                print(f"Pixel at ({x}, {y}): {pixel}")
                
    except Exception as e:
        print(f"Error: {e}")

check_transparency("img/logo_transparent_v2.png")
