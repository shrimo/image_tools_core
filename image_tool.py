import random, numpy
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance

# node graph
class graph(dict):
    def __init__(self, *args, **kwds):
        super(graph, self).__init__(*args, **kwds)
        self.__dict__ = self

# Crop for multiprocessing
def crop_mp_(file_in, file_out, process_):

    iCrop_mp = Image.open(file_in)

    width = iCrop_mp.size[0]
    height = iCrop_mp.size[1]

    if (process_==1):
        box=(0,0, width, height/2);
    if (process_==2):
        box=(0,height/2, width, height);

    iCrop_mp_crop = iCrop_mp.crop(box)
    iCrop_mp_crop.save(file_out)

    return;

# Merge
def merge_(file_in_01, file_in_02, file_out):

    iMerge_01 = Image.open(file_in_01)
    iMerge_02 = Image.open(file_in_02)

    width = iMerge_01.size[0]
    height = iMerge_01.size[1]

    im = Image.new('RGB',(width, height*2),(0,0,0))

    box1=(0,0)
    box2=(0, height)
    im.paste(iMerge_01,box1)
    im.paste(iMerge_02,box2)

    im.save(file_out)
    return;

# Crop
def crop_(file_in, file_out, size):
    iCrop_in = Image.open(file_in)
    width = iCrop_in.size[0]
    height = iCrop_in.size[1]
    box=(0,0, width, height/size)
    iCrop_out = iCrop_in.crop(box)
    iCrop_out.save(file_out)
    return;

# Size
def size_(file_in, file_out, size):
    iSize_in = Image.open(file_in)
    width = iSize_in.size[0]
    height = iSize_in.size[1]
    x=int(float(width)*size)
    y=int(float(height)*size)
    print x,':',y
    iSize_out=iSize_in.resize((x, y), Image.NEAREST)
    iSize_out.save(file_out)
    return;

# Blur
def blur_(file_in, file_out, size):
    iBlur = Image.open(file_in)
    for i in range(size):
        iBlur = iBlur.filter(ImageFilter.BLUR)
    iBlur.save(file_out)
    return;

# numpy noise
def numpy_noise_(file_in,file_out, size):
    iNoise = Image.open(file_in)
    width = iNoise.size[0]
    height = iNoise.size[1]
    a = numpy.random.rand(height, width,size) * 255
    iNoise_out = Image.fromarray(a.astype('uint8')).convert('RGBA')
    iNoise_out.save(file_out)
    return;

# composite
def composite_(file_a,file_b,file_out, mask):
    aCom = Image.open(file_a)
    bCom = Image.open(file_b)
    width = aCom.size[0]
    height = aCom.size[1]
    iMask = Image.new('L', (width, height), mask)
    result = Image.composite(aCom, bCom, iMask)
    result.save(file_out)
    return;

# Noise
def noise_(file_in,file_out, size):
    iNoise = Image.open(file_in)
    width = iNoise.size[0]
    height = iNoise.size[1]
    pix = iNoise.load()
    for i in range(width):
        for j in range(height):
            randR = random.randint(-size, size)
            randG = random.randint(-size, size)
            randB = random.randint(-size, size)
            a = pix[i, j][0] + randR
            b = pix[i, j][1] + randG
            c = pix[i, j][2] + randB
            if (a < 0):
                a = 0
            if (b < 0):
                b = 0
            if (c < 0):
                c = 0
            if (a > 255):
                a = 255
            if (b > 255):
                b = 255
            if (c > 255):
                c = 255
            draw.point((i, j), (a, b, c))
    iNoise.save(file_out)
    del draw
    return;

# Brightness
def bright_(file_in,file_out, size):
    iBright = Image.open(file_in)
    enhancer = ImageEnhance.Brightness(iBright)
    iBright_out = enhancer.enhance(size)
    iBright_out.save(file_out,quality=90)
    return;
