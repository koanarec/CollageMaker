from PIL import Image, ImageOps
import PIL
import pathlib
import time
from os import execv, walk
import copy
import random
import math
import os
from time import gmtime, strftime
from tqdm import tqdm
import glob
import cv2
import numpy as np
import os.path
from os import path
from PIL import Image, ExifTags
import csv
from subprocess import Popen, PIPE
import subprocess
import uuid
from inputimeout import inputimeout, TimeoutOccurred

from os.path import exists
#You should check if images exists or not too. 

#The first number in setup is the number of pixels in the finial image
#The second number is the resolution of each patch                              Recommended ~100

filenamespng = [f for f in glob.glob("*.png")]
filenames = [f for f in glob.glob("*.jpg")]
name_of_image = "idk"
if  exists("money.jpg"):
    name_of_image = "money.jpg"
elif exists("money.png"):
    name_of_image = "money.png"
elif len(filenames) > 0:
    name_of_image = filenames[0]
elif len(filenamespng) > 0:
    for x in filenamespng:
        if x != "final.png":
            name_of_image = x
    if name_of_image == "idk":
        print("Image to create not supplied, please add it to folder undre the name money.png")
        exit()
else:
    print("Image to create not supplied, please add it to folder undre the name money.png")
    exit()
    
totalstart = time.time()

try:
    f = open("setup.txt", "r")
    data = f.readlines()
    res_of_comp = int(data[0].rstrip("\n"))
    patch = int(data[1].rstrip("\n"))
    f.close()
except:
    res_of_comp = 40
    patch = 40


print("Removing old patch sized photos")
files = glob.glob(str(pathlib.Path().resolve()) + "\\patch_sized_photos\\*.*")
for f in files:
    os.remove(f)
patch_name = 0


print("Converting all images to PNG")
[os.rename(f, str(pathlib.Path().resolve()) +"\\images\\"+str(uuid.uuid4()) +".png") for f in glob.glob(str(pathlib.Path().resolve()) + "\\images\\*.*") if f.split("//")[-1][-4:] != ".png"]

#This takes a patch image and decreases its resolution to the desired size. Saves it in patch_sized_photos
def downscale_to_patch(image_name):
    if image_name not in os.listdir(str(pathlib.Path().resolve()) + "\\patch_sized_photos"):
        f = image_name
        try:
            img = cv2.imread(str(pathlib.Path().resolve()) + "\\images\\"+f)
            heightzz, widthzz, sss = img.shape
            if widthzz > heightzz * 2 * 0.8:
                res = cv2.resize(img, dsize=(patch*2, patch), interpolation=cv2.INTER_AREA)
            elif widthzz * 2 * 0.8 < heightzz:
                res = cv2.resize(img, dsize=(patch, patch * 2), interpolation=cv2.INTER_AREA)
            else:
                res = cv2.resize(img, dsize=(patch, patch), interpolation=cv2.INTER_AREA)
            cv2.imwrite(str(pathlib.Path().resolve()) + "\\patch_sized_photos\\"+ image_name.split("\\")[-1], res)
        except:
            print('problem with: ', image_name)

            try:
                dels = inputimeout(prompt='Do you want to delete it? (y/n)\n', timeout=5)
            except TimeoutOccurred:
                dels = 'timeout'
            if dels == "y":
                try:
                    os.remove(str(pathlib.Path().resolve()) + "\\images\\" + image_name)
                except:
                    print("couln't delete")

downscaled = []
patch64data = {}
try:
    with open('downscaled_patches_data.csv', 'r', encoding='UTF8', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for x in spamreader:
            downscaled.append(x[0])
            patch64data.update({x[0]: x})
except:
    downscaled = []
    patch64data = {}

print("Downscaling patches to 8*8px, and writing data to \"downscaled_patches_data.csv\"")
with open('downscaled_patches_data.csv', 'w', encoding='UTF8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for f in tqdm(glob.glob(str(pathlib.Path().resolve()) + "\\images\\*.*")):
        working = False
        if f.split("\\")[-1] not in downscaled:
            try:
                img =  cv2.imread(f)
                acurrh, acurrw,dd = img.shape
                working = True
            except:
                working = False
                print("There is something wrong with picture:", f)
        else:
            writer.writerow(patch64data[f.split("\\")[-1]])
        
        if working:
            data = []
            patch_name = str(str(f).split("\\")[-1])
            shape = "square"
            if acurrw > acurrh * 2 * 0.8:
                shape = "landscape"
                img = cv2.resize(img, dsize=(16, 8), interpolation=cv2.INTER_AREA )
                data = [patch_name,shape]
                for currw in range(0,8):
                    for currh in range(0,8):
                        data.append(img[currw, currh][0])
                        data.append(img[currw, currh][1])
                        data.append(img[currw, currh][2])
                for currw in range(0,8):
                    for currh in range(0,8):
                        data.append(img[currw, currh + 8][0])
                        data.append(img[currw, currh + 8][1])
                        data.append(img[currw, currh + 8][2])
            elif acurrw * 2 * 0.8 < acurrh:
                shape = "portrait"
                img = cv2.resize(img, dsize=(8, 16), interpolation=cv2.INTER_AREA )
                data = [patch_name,shape]
                for currw in range(0,8):
                    for currh in range(0,8):
                        data.append(img[currw, currh][0])
                        data.append(img[currw, currh][1])
                        data.append(img[currw, currh][2])
                for currw in range(0,8):
                    for currh in range(0,8):
                        data.append(img[currw + 8, currh][0])
                        data.append(img[currw + 8, currh][1])
                        data.append(img[currw + 8, currh][2])
            else:
                img = cv2.resize(img, dsize=(8, 8), interpolation=cv2.INTER_AREA )
                data = [patch_name,shape]
                for currw in range(0,8):
                    for currh in range(0,8):
                        pixel = [img[currw, currh][0],img[currw, currh][1],img[currw, currh][2]]
                        data = data +  pixel
            writer.writerow(data)
    
#Loading the starting image for dimentions. 
money = Image.open(name_of_image)
money = ImageOps.exif_transpose(money)
money = money.convert("RGB")
pixels = money.load()
money_width, money_height = money.size
money.close()



#Calculates the final dimentions of collage and makes the actual png
money_ratio = money_width/(money_width + money_height)
number_of_patches_width = round(money_ratio * res_of_comp)
number_of_patches_height = round((1-money_ratio) * res_of_comp)
collage_width = patch * number_of_patches_width
collage_height = patch * number_of_patches_height

f = open("num_patches_height.txt", "w")
f.writelines([str(number_of_patches_height)])
f.close()

with open('num_patches_height.csv', 'w', encoding='UTF8', newline='') as csvfile:
    writer =  csv.writer(csvfile)
    writer.writerow([number_of_patches_height])

b_max = number_of_patches_height
with open('cut_and_downscaled_money_patches.csv', 'w', encoding='UTF8', newline='') as csvfile:
    writer =  csv.writer(csvfile)
    files = glob.glob(str(pathlib.Path().resolve()) +"\\cut_and_downscaled_money_patches\\*.*")
    for f in files:
        os.remove(f)
    img =  cv2.imread(name_of_image)
    main_h, main_w ,sssss= img.shape
    patch = (main_w/number_of_patches_width)
    holdr = tqdm(range(0,number_of_patches_width), desc = "Cutting the final image into squares and downscaling to 8*8")
    for a in holdr:
        for b in range(0,b_max):
            addw = 0
            addh = 0
            if a == number_of_patches_width:
                a = number_of_patches_width -1
                addw = 1
            if b == b_max:
                b = b_max -1
                addh = 1
            w1 = math.floor(a * patch)
            w2 = math.floor((a+ 1) * patch)
            h1 = math.floor(b * patch)
            h2 = math.floor((b + 1) * patch) 
            if h2 > main_h:
                h1 = math.floor((b-1) * patch) - 1 
                h2 = math.floor((b) *   patch) - 1 
            if w2 > main_w:
                w1 = math.floor((a-1) * patch) - 1
                w2 = math.floor((a) * patch)   - 1
            cropped_image = img[h1:h2,w1:w2]
            cropped_image = cv2.resize(cropped_image, dsize=(8, 8), interpolation=cv2.INTER_AREA)
            img_list  = [a,b]
            for eightw in range(0,8):
                for eighth in range(0,8):
                    img_list += [cropped_image[eightw,eighth][0],cropped_image[eightw,eighth][1],cropped_image[eightw,eighth][2]]
            writer.writerow(img_list)
            newpath = str(pathlib.Path().resolve()) +"\\cut_and_downscaled_money_patches\\"+str(a+addw)+"_"+ str(b+addh)+".png"
            cv2.imwrite(newpath, cropped_image)

print("Starting C++ code to do the maths")
start = time.time()

subprocess.check_call([str(pathlib.Path().resolve()) +"\\collagemaths\\collagemaths\\collagemaths.exe"])
end = time.time()
print("Finished maths, in " + str(end-start) + " seconds.")

def bestphot(a,b):
    file = open("answer.csv")
    csvreader = csv.reader(file)
    for row in csvreader:
        if int(row[0]) == int(a) and int(row[1]) == int(b):
            best_now = row[2]
    
    file.close()
    return best_now

try:
    f = open("setup.txt", "r")
    data = f.readlines()
    res_of_comp = int(data[0].rstrip("\n"))
    patch = int(data[1].rstrip("\n"))
    f.close()
except:
    res_of_comp = 40
    patch = 40

path_of_the_directory = glob.glob(str(pathlib.Path().resolve()) + "\\temp_storage\\*.*" )
for x in path_of_the_directory:
    os.remove(x)

#Loading the starting image for dimentions. 
money = Image.open(name_of_image)
money = ImageOps.exif_transpose(money)
money = money.convert("RGB")
pixels = money.load()
money_width, money_height = money.size
money.close()

#Calculates the final dimentions of collage and makes the actual png
money_ratio = money_width/(money_width + money_height)
number_of_patches_width = round(money_ratio * res_of_comp)
number_of_patches_height = round((1-money_ratio) * res_of_comp)
collage_width = patch * number_of_patches_width
collage_height = patch * number_of_patches_height
im = PIL.Image.new(mode="RGB", size=(collage_width, collage_height))
fresh_image = im.load()
im.save("final.png")

print("Pasting patches onto final image")
start = time.time()
done = []
patch_name = 0
l_img = cv2.imread("final.png")
for a in range(0,number_of_patches_width):
    for b in range(0, number_of_patches_height):
        if (a,b) not in done:
            newpath = str(pathlib.Path().resolve()) +"\\cut_and_downscaled_money_patches\\"+str(a)+"_"+ str(b)+".png"
            best_photo_name  = bestphot(a,b)
            downscale_to_patch(best_photo_name)
            naems= str(glob.glob(str(pathlib.Path().resolve()))[0]) + "\\patch_sized_photos\\" + str(best_photo_name.split("\\")[-1])
            s_img = cv2.imread(naems)
            x_offset= a * patch
            y_offset= b * patch
            height, width,ss = s_img.shape
            
            newname = str(pathlib.Path().resolve()) + "\\temp_storage\\img" + str(patch_name) + ".png"
            
            if height > 0.8 * width * 2:
                if y_offset+s_img.shape[0] < l_img.shape[0]:
                    done.append((a,b+1))
                    l_img[y_offset:y_offset+s_img.shape[0], x_offset:x_offset+s_img.shape[1]] = s_img
                else:
                    x_offset= a * patch
                    y_offset= (b-1) * patch
                    done.append((a ,(b-1)))
                    l_img[y_offset:y_offset+s_img.shape[0], x_offset:x_offset+s_img.shape[1]] = s_img
                    
            elif width > 0.8 * 2 * height:
                if x_offset+s_img.shape[1] < l_img.shape[1]:
                    done.append((a + 1,b))
                    l_img[y_offset:y_offset+s_img.shape[0], x_offset:x_offset+s_img.shape[1]] = s_img
                else:
                    x_offset= (a-1) * patch
                    y_offset= b * patch
                    done.append(((a-1),b))
                    l_img[y_offset:y_offset+s_img.shape[0], x_offset:x_offset+s_img.shape[1]] = s_img
            else:
                l_img[y_offset:y_offset+s_img.shape[0], x_offset:x_offset+s_img.shape[1]] = s_img
            done.append((a,b))
        patch_name += 1
    
    path_of_the_directory= str(pathlib.Path().resolve()) + "\\temp_storage"
    for filename in os.listdir(path_of_the_directory):
        f = filename[3:-4]
        if int(f) < patch_name -4:
            os.remove(path_of_the_directory + "\\"+filename)

cv2.imwrite(newname, l_img)
naems= str(glob.glob(str(pathlib.Path().resolve()))[0]) + "\\final.png"
cv2.imwrite(naems, l_img)
end = time.time()
print(end-start)
end = time.time()
print(end - totalstart)