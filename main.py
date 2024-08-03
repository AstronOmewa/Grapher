import numpy as np
<<<<<<< HEAD:sirius.py
from scipy.ndimage import convolve
from PIL import Image, ImageFilter
file = "image.png"

def flatten(arr2d):
    sum_=sum([x for i in arr2d for x in i])
    if sum_==0:
        sum_=1
    return [x/sum_ for i in arr2d for x in i]
def flat(arr2d):
    return [x for i in arr2d for x in i]
def flt(arr_img,kernel):
    kerSum=sum(flat(kernel))
    if kerSum==0:
        kerSum=1
    return convolve(arr_img,np.multiply(kernel,1/kerSum))


with Image.open(file) as img:
    img.load()

n=2
f="1 "*n
s=[([[1]+[0]*(n-1)])*(n-1)]
kernel=[
    [1,1,1,1,1],
    [1,1,1,1,1],
    [1,1,1,1,1],
    [1,1,1,1,1],
    [1,1,1,1,1],
]

repeats=1
# kernel=[[1]*n]*n
ch=[im for im in img.split()]
zero_band=ch[0].point(lambda _:0)

# img=flt(gray,kernel)

arr_img=[np.array(i) for i in ch]

convolved=[flt(i,kernel) for i in arr_img]

for i in range(0,repeats-1):
    convolved=[flt(c,kernel) for c in convolved]

img=[Image.fromarray(c) for c in convolved] 
# img=[Image.merge(
#     "RGB",(img[0],zero_band,zero_band)
# ),Image.merge(
#     "RGB",(zero_band,img[1],zero_band)
# ),Image.merge(
#     "RGB",(zero_band,zero_band,img[2])
# )]
img=Image.merge("RGB",(img[0],img[1],img[2]))
img.show()
=======
from PIL import Image
from scipy.ndimage import convolve
img = "graph.jpg"
>>>>>>> origin/writingRDME:main.py
