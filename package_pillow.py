from PIL import Image, ImageDraw

img = Image.new('RGB', (400, 300), color='lightblue')

draw = ImageDraw.Draw(img)
draw.text((50, 50), "Hello PZN", fill='black')
draw.rectangle([50, 100, 350, 200], outline='red', width=3)
draw.ellipse([100, 150, 300, 250], fill='yellow')

img.save('pzn.png')