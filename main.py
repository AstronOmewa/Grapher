import numpy as np
from scipy.ndimage import convolve
from PIL import Image, ImageFilter
file = "image.png"

def convKers(arr_img,kers=[],muls=[]):
    for ker in kers:
        kerSum=sum(flat(ker))
        if kerSum==0:
            kerSum=1
        if not isinstance(ker,ImageFilter.Filter):
            arr_img=convolve(arr_img,ker)
        else:
            arr_img=np.array(Image.fromarray(arr_img).filter(ker/kerSum))
    return arr_img

def flatten(arr2d):
    sum_=sum([x for i in arr2d for x in i])
    if sum_==0:
        sum_=1
    return [x/sum_ for i in arr2d for x in i]

def flat(arr2d):
    return [x for i in arr2d for x in i]

def flt(arr_img,kernels,muls=[1]):
    return convKers(arr_img,kernels,muls)


with Image.open(file) as img:
    img.load()

n=2
f="1 "*n
s=[([[1]+[0]*(n-1)])*(n-1)]

kernels=[
        [
            [-1,-1,-1],
            [-1,8,-1],
            [-1,-1,-1]
        ]
        
]
bordersX,bordersY=len(kernels[0]),len(kernels[0][0])
img=img.crop((bordersX,bordersY,(img.size)[0] - bordersX-1,(img.size)[1] - bordersY-1))
muls=[1,1]
repeats=5
# kernel=[[1]*n]*n
gr=img.convert("L")
# gr.show()
ch=gr
zero_band=ch.point(lambda _:0)

arr_img=np.array(ch)

convolved=flt(arr_img,kernels,muls)
for i in range(0,repeats-1):
    convolved=flt(arr_img,kernels,muls)

mask=Image.fromarray(convolved)
mask.show()

blank=img.point(lambda _:0)
res=img.filter(ImageFilter.GaussianBlur(50))
res=Image.composite(img,blank,mask)
res.show()

