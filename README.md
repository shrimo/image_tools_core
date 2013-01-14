Image processing on instructions from the data file

Implemented: Blur, Merge, Brightness, Crop, Size, Noise, Composite

Python 2.7 http://python.org/download/

PIL, the Python Image Library, provides image processing functionality and supports many file formats. http://www.pythonware.com/products/pil/

Numpy/Scipy – http://www.numpy.org/

sample data files:

"node1":{

"node_name" : "blur_01",

"node_type" : "blur",

"file_in" : "test.jpg",

"file_out": "out.jpg",

"size" : 30,

"id": 1

}


image_core.py - execute file

node.json - data file