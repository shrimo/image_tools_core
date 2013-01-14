import Image
import ImageDraw

def gradient_(width,height):
    im = Image.new("L", (10, height))
    draw = ImageDraw.Draw(im)
    for l in xrange(height):
        G=255 * l/height
        colour = (G)
        draw.line((0, l, height, l), fill=colour)
    im.show()
    del draw

gradient_(1280,720)
