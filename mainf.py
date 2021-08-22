import time
import os
import typing
import cv2
import sys

if(len(sys.argv)==1):
    sys.exit("No filename specified")

filename = sys.argv[1]
if(filename[-3:]!='mp4'):
    exitstr = filename[-3:]+' not supported'
    sys.exit(exitstr)

def asciify_pixel(p):
    return gradient[int((((int(p[0]) + int(p[1]) + int(p[2])) / 3)*(gradient_len-1))/255)]
    #return gradient[int(((.2126*p[2] + .587*p[1] + .114*p[0])/255)*gradient_len)]

def asciify_row(row):
    return map(asciify_pixel, row)

def asciify_img(img):
    rlist = []
    for row in map(asciify_row, img):
        rlist.append("".join(row))
    return rlist

filnum = 34
w_scale = 2
gap = 0.7 #any faster causes trouble with windows
fname = 'folder'

#gradient = ' `-~+#@'
gradient = '⠀⢀⣀⣠⣤⣴⣶⣾⣿'

video = cv2.VideoCapture(filename)
frames = []
gradient = tuple([c for c in gradient])
gradient_len = len(gradient)

fps = video.get(cv2.CAP_PROP_FPS)
width = video.get(3)
height = video.get(4)

scale = filnum/height


scaled_width = int(width*scale*w_scale)
scaled_height = int(height*scale)


print(f'Dimensions: {width}x{height}')
print(f'Scale Factor: {scale}')
print(f'Scaled Dims: {scaled_width}x{scaled_height}')
print(f'Gradient: \'{"".join(gradient)}\'')
print(f'FPS: {fps}')
print('Converting...')

start_time = time.time()
while True:
    end, img = video.read()
    if not end: break
    img = cv2.resize(img, (scaled_width, scaled_height,))
    frames.append(asciify_img(img))

print("--- %s seconds ---" % (time.time() - start_time))

frames = tuple(frames)
a = 0
print('Done.',len(frames))
input("Start?")

start_time = time.time()
for frame in frames:
    for f in os.listdir(fname):
        os.remove(os.path.join(fname, f))
    cnt = 0
    for strn in list(frame):
        print(strn)
        cnt+=1
        sa = '0'+str(cnt) if cnt<10 else str(cnt)
        sa = sa+'-'
        stringe = fname+'/'+sa+strn+'.txt'
        f = open(stringe, 'w')
        f.close()
    print('fromos binted: ',a)
    a += 1
    time.sleep(gap)
print("--- %s seconds ---" % (time.time() - start_time))
