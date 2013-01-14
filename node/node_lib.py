from PIL import Image, ImageDraw, ImageFilter, ImageFont
import numpy
from scipy import misc

# node graph
class graph(dict):
    def __init__(self, *args, **kwds):
        super(graph, self).__init__(*args, **kwds)
        self.__dict__ = self

# node size
def size_(cached,size,w,h):
    out=misc.imresize(cached,(h/size,w/size),'bilinear','RGB')
    print '->size'
    return out;

# node blur
def blur_(cached,size):
    out=cached
    for k in range(size):
        out=misc.imfilter(out,'blur')
        print '.',
    print '->blur'
    return out;

# node sharpen
def sharpen_(cached,size):
    out=cached
    for k in range(size):
        out=misc.imfilter(out,'sharpen')
        print '.',
    print '->sharpen'
    return out;

