import cv2
import numpy as np
from PIL import Image

def getBlue(picname):
    i_min = np.array([100,43,46])#h,s,v three parameters
    i_max = np.array([124,255,255])
    img = cv2.imread(picname)  #read img
    '''
    cv2.namedWindow("Image",0)   #create a window
    cv2.resizeWindow("Image",640,480)
    cv2.imshow("Image", img)   #show img in window
    cv2.waitKey (0)
    cv2.destroyAllWindows()
    '''
    img2 = img.copy()
    img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2HSV) #BGR transfer into hsv

    #equalize the hisgram of image
    h, s, v = cv2.split(img2)
    v = cv2.equalizeHist(v)
    hsv = cv2.merge((h,s,v))

    #get the range of colour
    imgT = cv2.inRange(hsv,i_min,i_max)
    #reduce noise--like knn using median
    imgT = cv2.medianBlur(imgT,9)

    kernel = np.ones((5,5),np.uint8)
    imgT = cv2.morphologyEx(imgT,cv2.MORPH_OPEN,kernel,iterations = 10)
    imgT = cv2.medianBlur(imgT,9)

    picname = picname.split(".")[0]
    midname = picname+"-mask.jpg"
    cv2.imwrite(midname,imgT)
    return midname

#for combine more natural: seamless cloning
def seamlessClone(skyname,picname,maskname):
    src = cv2.imread(skyname)
    dst = cv2.imread(picname)

    src_mask = cv2.imread(maskname,0)
    src_mask0 = cv2.imread(maskname,)
    #find contours
    contours = cv2.findContours(src_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cnt = contours[0]

    x,y,w,h = cv2.boundingRect(cnt)
    if w == 0 or h == 0:
        return dst
    dst_x = len(dst[0])
    dst_y = len(dst[1])
    src_x = len(src[0])
    src_y = len(src[1])
    scale_x = w*1.0/src_x
    dshape = dst.shape
    #resize the sky picture to fit final picture
    src=cv2.resize(src, (dshape[1],dshape[0]), interpolation = cv2.INTER_CUBIC)

    cv2.imwrite("src_sky.jpg",src)
    centre = (int((x+w)/2),int((y+h)/2))

    #process seamless
    output = cv2.seamlessClone(src,dst,src_mask0,centre,cv2.NORMAL_CLONE)
    cv2.imwrite("sky-final.jpg",output)
    return output

def findPos(coordinate,org):
    x,y,z = coordinate
    A = y/4 + (x/32)*64
    B = z/4 + ((x%32)/4)*64
    if A>=512:
        A = 511
    if B>=512:
        B = 511
    pos = [int(A),int(B)]
    return pos

def urnameFilter(orgtable,newtable,picname):
    org = cv2.imread(orgtable)
    new = cv2.imread(newtable)
    fin = picname

    finalname = "aaa-final.jpg"
    
    for i in range(len(fin)):
        for j in range(len(fin[0])):
            pos = findPos(fin[i][j],org)
            fin[i][j] = new[pos[0]][pos[1]]

    cv2.imwrite(finalname,fin)
    return finalname


picname = "IMG_6791.jpg"
skyname = "cloud.jpg"
orgtable= "lookup-table.png"
newtable = "lookup-table-yourname.jpeg"

maskname = getBlue(picname)
skyimg = seamlessClone(skyname,picname,maskname)
finalname = urnameFilter(orgtable,newtable,skyimg)

