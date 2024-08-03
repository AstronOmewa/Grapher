import numpy as np
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
def flt(img,kernel):
    kerSum=1/sum(flat(kernel))
    return convolve(arr_img,np.multiply(kernel,kerSum))


with Image.open(file) as img:
    img.load()

n=2
f="1 "*n
s=[([[1]+[0]*(n-1)])*(n-1)]
kernel=[
    [1,1],
    [1,0]
]
# kernel=[[1]*n]*n
# r,g,b=img.split()[0],img.split()[1],img.split()[2]
# zero_band=r.point(lambda _:0)
# print(r)
gray=img.convert("L")

# img=flt(gray,kernel)

arr_img=np.array(gray)

convolved=flt(arr_img,kernel)

img=Image.fromarray(convolved)

img.show()
