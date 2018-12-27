from PIL import Image
import sys

symbols = {224: '@', 192: '#', 160: '$', 128: '=', 96: '|', 64: ':', 32: '.', 0: ' '}

img_file = sys.argv[1]
if len(sys.argv) > 2:
    pixel_scale = int(sys.argv[2])
else:
    pixel_scale = 1

# TODO: make a copy, instead of converting image
jpeg = Image.open(img_file).convert(mode = 'L')

loaded_img = jpeg.load()

w = jpeg.size[0]
h = jpeg.size[1]

# TODO: how to do this with a list comprehension?
for j in range(h):
    if j % pixel_scale == 0:
        row = []
        for i in range(w):
            if i % pixel_scale == 0:
                brightness = loaded_img[i, j]
                symbol = list(filter(lambda x: x <= brightness, symbols.keys()))
                row.append(symbols[symbol[0]])
        print(' '.join(row))
