import cv2
import csv
image=cv2.imread(r"src/test_pic_v2_2.jpg")
with open("src/coords.csv") as csvCoords:
    coords=list(csv.reader(csvCoords))

a=0
b=0

while (a < 24):
    print(a)

    while (b < 8):
        read_x=(coords[b][a])
        read_y=(coords[b][a+1])

        x=int(read_x)
        y=int(read_y)

        h=y+47
        w=x+47
        

        print(x,y,w,h)

        crop_image=image[y:h, x:w].copy()
        img_name_calc=(round(a/2),b)        
        img_name=("src/" + str(img_name_calc) + ".png")
        print(img_name)
        cv2.imwrite(img_name, crop_image)
        cv2.imshow("Cropped", crop_image)
        cv2.waitKey(0)

        b+=1
  
    a+=2
    b=0

