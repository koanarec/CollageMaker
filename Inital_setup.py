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
import ast
import glob
import cv2
import numpy as np
import os.path
from os import path
from PIL import Image, ExifTags
import csv
from subprocess import Popen, PIPE
import subprocess

name_of_image = "money.jpg"


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


list2 = len(os.listdir(str(pathlib.Path().resolve()) + "\\images"))
list1 = len(os.listdir(str(pathlib.Path().resolve()) + "\\patch_sized_photos"))
try:
    paste,pasta= ImageOps.exif_transpose(Image.open(str(pathlib.Path().resolve()) + "\\patch_sized_photos\\0.png")).size
except:
    paste = 1
    pasta = 9
if min(paste,pasta) != patch or list1 != list2 or True:
    print("Removing old patch sized photos")
    files = glob.glob(str(pathlib.Path().resolve()) + "\\patch_sized_photos\\*.*")
    for f in files:
        os.remove(f)

    lcv = 0
    files = glob.glob(str(pathlib.Path().resolve()) + "\\images\\*.*")
    print("Renaming all of images with a unique identifier, and converting to png")
    for f in files:
        os.rename(f, str(pathlib.Path().resolve()) +"\\images\\"+str(lcv)+"bad"+str(random.randint(0,10000)) +".png")
        lcv += 1

    hold = "Downscaling all images in images to the resolution of patch: " + str(patch)
    hold.ljust(150)
    lcv = 0
    files = glob.glob(str(pathlib.Path().resolve()) + "\\images\\*.*")
    files_progressbar = tqdm(files, desc = hold)
    for f in files_progressbar:
        try:
            img = cv2.imread(f)
            heightzz, widthzz, sss = img.shape
            if widthzz > heightzz * 2 * 0.8:
                res = cv2.resize(img, dsize=(patch*2, patch), interpolation=cv2.INTER_AREA)
            elif widthzz * 2 * 0.8 < heightzz:
                res = cv2.resize(img, dsize=(patch, patch * 2), interpolation=cv2.INTER_AREA)
            else:
                res = cv2.resize(img, dsize=(patch, patch), interpolation=cv2.INTER_AREA)
            cv2.imwrite(str(pathlib.Path().resolve()) + "\\patch_sized_photos\\"+ str(lcv)+ ".png", res)
            os.rename(f, str(pathlib.Path().resolve()) + "\\images\\"+ str(lcv)+ ".png")
        except:
            print("something went wrong with", f)
        lcv += 1

word = "Downscaling images and storing them in downwcaled_data"
word.ljust(150)

files = glob.glob(str(pathlib.Path().resolve()) + "\\patch_sized_photos\\*.*")
alls = []
with open('downscaled_patches_data.csv', 'w', encoding='UTF8', newline='') as csvfile:
    writer = csv.writer(csvfile)

    for f in tqdm(files, desc = word):
        img =  cv2.imread(f)
        acurrh, acurrw,dd = img.shape
        data = []
        lcv = str(str(f).split("\\")[-1].rstrip(".png"))
        shape = "square"
        if acurrw > acurrh * 2 * 0.8:
            shape = "landscape"
            img = cv2.resize(img, dsize=(16, 8), interpolation=cv2.INTER_AREA )
            data = [lcv,shape]
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
            data = [lcv,shape]
            for currw in range(0,8):
                for currh in range(0,8):
                    data.append(img[currw, currh][0])
                    data.append(img[currw, currh][1])
                    data.append(img[currw, currh][2])
            for currw in range(0,8):
                for currh in range(0,8):
                    data.append(img[currw + 8, currh][0])
                    data.append(img[currw + 8, currh ][1])
                    data.append(img[currw + 8, currh][2])
        else:
            img = cv2.resize(img, dsize=(8, 8), interpolation=cv2.INTER_AREA )
            data = [lcv,shape]
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
                h1 = math.floor((b-1) * patch) -1 
                h2 = math.floor((b) * patch) -1 
            if w2 > main_w:
                w1 = math.floor((a-1) * patch)-1
                w2 = math.floor((a) * patch) -1
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

subprocess.check_call([str(pathlib.Path().resolve()) +"\\collagemaths\\x64\\Debug\\collagemaths.exe"])
end = time.time()
print("Finished maths, in " + str(end-start) + " seconds.")


def bestphot(aim):
    file = open("answer.csv")
    csvreader = csv.reader(file)
    a = aim.split("\\")[-1].rstrip(".png").split("_")[0]
    b = aim.split("\\")[-1].rstrip(".png").split("_")[1]
    for row in csvreader:
        if row[0] == a and row[1] == b:
            best_now = row[2]
            score = row[3]
    
    file.close()
    return [str(pathlib.Path().resolve()) +"\\images\\"+best_now+ ".png", score]

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

#Stores all of the images provided in a dictionary in RAM allowing for quick access. 
keys = []
datas = []
files = glob.glob(str(pathlib.Path().resolve()) + "\\downscaled_images\\*.*")
for f in files:
    keys.append(int(str(f).split("\\")[-1].rstrip(".png")))
    col_info = []
    picture = Image.open(f)
    pixels = picture.load()
    for x in range(0,8):
        for y in range(0,8):
            col_info.append(copy.deepcopy(pixels[x,y]))
    datas.append(copy.deepcopy(col_info))
lines = dict(zip(keys, datas))

print("startnig paste")
start = time.time()
done = []
lcv = 0
l_img = cv2.imread("final.png")
holdr = tqdm(range(0,number_of_patches_width), desc= "Pasting the patches onto the collage")
for a in holdr:
    for b in range(0, number_of_patches_height):
        if (a,b) not in done:
            newpath = str(pathlib.Path().resolve()) +"\\cut_and_downscaled_money_patches\\"+str(a)+"_"+ str(b)+".png"
            best_photo_name, score  = bestphot(newpath)
            naems= str(glob.glob(str(pathlib.Path().resolve()))[0]) + "\\patch_sized_photos\\" + str(best_photo_name.split("\\")[-1])
            s_img = cv2.imread(naems)
            x_offset= a * patch
            y_offset= b * patch
            height, width,ss = s_img.shape
            
            newname = str(pathlib.Path().resolve()) + "\\temp_storage\\img" + str(lcv) + ".png"
            
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
        lcv += 1
    
    path_of_the_directory= str(pathlib.Path().resolve()) + "\\temp_storage"
    for filename in os.listdir(path_of_the_directory):
        f = filename[3:-4]
        if int(f) < lcv -4:
            os.remove(path_of_the_directory + "\\"+filename)

cv2.imwrite(newname, l_img)
naems= str(glob.glob(str(pathlib.Path().resolve()))[0]) + "\\final.png"
cv2.imwrite(naems, l_img)
end = time.time()
print(end-start)
end = time.time()
print(end - totalstart)