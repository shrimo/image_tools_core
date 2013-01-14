import json
from node_lib import *
from PIL import Image, ImageDraw, ImageFilter, ImageFont
import numpy
from scipy import misc


file_node='node.json'

with open(file_node) as jdf:
    data_io = json.load(jdf)

G = graph
sorted_names=sorted(data_io, key=lambda x : data_io[x]['id'])

cached={}

for _name in sorted_names:
    node = G(data_io[_name])

    if (node.type=='read'):
        img = Image.open(node.file)
        width, height = img.size
        cached[node.name] = numpy.array(img)
        print 'cached->', node.file,'(',width, height,')'

    if (node.type=='size'):
        cached[node.name]=size_(cached[node.link],node.size,width,height)

    if (node.type=='blur'):
        cached[node.name]=blur_(cached[node.link],node.size)

    if (node.type=='sharpen'):
        cached[node.name]=sharpen_(cached[node.link],node.size)

    if (node.type=='write'):
        out_img = Image.fromarray(cached[node.link])
        out_img.save(node.file)
        print 'write->', node.file
