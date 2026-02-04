from PIL import Image
import os

def make_transparent(input_path, output_path):
    print(f"Processing {input_path}...")
    try:
        img = Image.open(input_path)
        img = img.convert("RGBA")
        datas = img.getdata()
        
        newData = []
        # Threshold for "white". Since it's a logo, we want to be careful.
        # Pure white is (255, 255, 255).
        # We'll use a high threshold to only remove the background.
        threshold = 240
        
        for item in datas:
            if item[0] > threshold and item[1] > threshold and item[2] > threshold:
                newData.append((255, 255, 255, 0))
            else:
                newData.append(item)
        
        img.putdata(newData)
        img.save(output_path, "PNG")
        print(f"Saved to {output_path}")
        
    except Exception as e:
        print(f"Error: {e}")

make_transparent("img/logo.png", "img/logo_transparent_v2.png")
