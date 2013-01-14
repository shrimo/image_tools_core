from threading import Thread
import os,image_tool,numpy
from PIL import Image,ImageFilter

def multi_crop_ (file_in):
    image_tool.crop_mp_(file_in,"cache_m1.jpg",1)
    image_tool.crop_mp_(file_in,"cache_m2.jpg",2)

def multi_bright_ (file_out1, file_out2,size):
    t1 = Thread(target=image_tool.bright_, args=('cache_m1.jpg',file_out1,size))
    t2 = Thread(target=image_tool.bright_, args=('cache_m2.jpg',file_out2,size))
    t1.start()
    print 't1 start'
    t2.start()
    print 't2 start'
    t1.join()
    t2.join()

def multi_noise (file_out1, file_out2,size):
    t1 = Thread(target=image_tool.numpy_noise_, args=('cache_m1.jpg',file_out1,size))
    t2 = Thread(target=image_tool.numpy_noise_, args=('cache_m2.jpg',file_out2,size))
    t1.start()
    print 't1 start'
    t2.start()
    print 't2 start'
    t1.join()
    t2.join()
