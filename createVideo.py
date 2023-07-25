import os
import cv2


path = "Images"

images = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)
print(images)        
print(len(images))
count = len(images)
frame = cv2.imread(images[0])
height,width,channel = frame.shape
size = (width,height)
out = cv2.VideoWriter("friends.mp4",cv2.VideoWriter_fourcc(*"DIVX"),5,size)
for i in range (0,count-1):
    frame = cv2.imread(images[i])
    out.write(frame)

out.release()
print("done")    
