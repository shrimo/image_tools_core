import json, random, os, numpy
from PIL import Image, ImageDraw, ImageFilter
from threading import Thread
from image_tool import *
from image_th import *

# read data file
print 'Image tools (core) v03a'
print 'read data file\n'
with open('node.json') as jdf:
    data_io = json.load(jdf)

# node select
G = graph

sorted_names=sorted(data_io, key=lambda x : data_io[x]['id'])
for name in sorted_names:
    node = G(data_io[name])
    print node.node_name

    if (node.node_type=='view'):
        print 'view->'
        ix=Image.open(node.file_in).show()

    if (node.node_type=='blur'):
        print 'blure->'
        blur_(node.file_in, node.file_out, node.size)
        print 'Write ',node.file_out,'\n'

    if (node.node_type=='bright'):
        print 'bright->'
        multi_crop_(node.file_in)
        multi_bright_('cache_b1.jpg','cache_b2.jpg',node.size)
        merge_('cache_b1.jpg','cache_b2.jpg',node.file_out)

        print 'Write ',node.file_out,'\n'
        os.system('del cache*.jpg')

    if (node.node_type=='noise'):
        print 'noise->'
        multi_crop_(node.file_in)
        multi_noise('cache_b1.jpg','cache_b2.jpg',node.size)
        merge_('cache_b1.jpg','cache_b2.jpg',node.file_out)

        print 'Write ',node.file_out,'\n'
        os.system('del cache*.jpg')

    if (node.node_type=='size'):
        print 'size->'
        size_(node.file_in, node.file_out, node.size)
        print 'Write ',node.file_out,'\n'

    if (node.node_type=='composite'):
        print 'composite->'
        composite_(node.file_a, node.file_b, node.file_out, node.mask)
        print 'Write ',node.file_out,'\n'

print 'end'
