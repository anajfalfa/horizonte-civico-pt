from PIL import Image
import os

def analyze_image(path):
    with open("log.txt", "a") as f:
        f.write(f"Analyzing {path}:\n")
        try:
            img = Image.open(path)
            f.write(f"  Format: {img.format}\n")
            f.write(f"  Mode: {img.mode}\n")
            f.write(f"  Size: {img.size}\n")
            
            if img.mode == 'RGBA':
                extrema = img.getextrema()
                alpha_extrema = extrema[3]
                f.write(f"  Alpha min/max: {alpha_extrema}\n")
            
            # Check corners
            corners = [
                (0, 0),
                (img.width - 1, 0),
                (0, img.height - 1),
                (img.width - 1, img.height - 1)
            ]
            
            f.write("  Corner pixels:\n")
            for x, y in corners:
                pixel = img.getpixel((x, y))
                f.write(f"    ({x}, {y}): {pixel}\n")
                
        except Exception as e:
            f.write(f"  Error: {e}\n")
        f.write("\n")

if os.path.exists("log.txt"):
    os.remove("log.txt")

analyze_image("img/logo.png")
analyze_image("img/logo_transparent.png")
