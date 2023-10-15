import random
import matplotlib
from PIL import Image, ImageEnhance
from fractals import MandelbrotSet
from viewport import Viewport
from cmaps import colorschemes

#interesting points
#x = -0.75, y = 0j, width = 3.5
#x = -1.04180483110546, y = 0.346342664848392j
#x = -0.747, y = -0.116817186889238j, width = 0.001
#x = -0.812223315621338, y = -0.185453926110785j

def paint(mandelbrot_set, viewport, palette, smooth):
    for pixel in viewport:
        stability = mandelbrot_set.stability(complex(pixel), smooth)
        index = int(min(stability * len(palette), len(palette) - 1))
        pixel.color = palette[index % len(palette)]

def denormalize(palette):
    return [
        tuple(int(channel * 255) for channel in color)
        for color in palette
    ]

resolution = 1024
color = random.choice(colorschemes)
mandelbrot_set = MandelbrotSet(max_iterations=512, escape_radius=1000)
colormap = matplotlib.cm.get_cmap(color).colors
palette = denormalize(colormap)

image = Image.new(mode="RGB", size=(resolution, resolution))
viewport = Viewport(image, center=-0.747-0.1168171j, width=0.001)
paint(mandelbrot_set, viewport, palette, True)
image.show()

