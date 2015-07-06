# -*- coding: utf-8 -*-
import cv2
import glob, random, os


size = 50

# clean
os.remove('model/info.dat') if os.path.exists('model/info.dat') else None
os.remove('model/bg.dat') if os.path.exists('model/bg.dat') else None

os.system("rm data/learning_images/positive/*") if os.path.exists("rm data/learning_images/positive/*") else None
os.system("rm data/learning_images/negative/*") if os.path.exists("rm data/learning_images/negative/*") else None


# positive images
info = open("model/info.dat", "w")
for filename in glob.glob("data/positives/*.jpg"):
    try:
        img = cv2.imread(filename)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #height,width,channel  = img.shape
        resized_image = cv2.resize(gray, (size, size)) 
        elements = filename.split("/")
        new_filename = "data/learning_images/positive/" + elements[-1].split(".")[0] + ".pgm"
        new_filename_bis = "../" + new_filename # TO CHANGE
        cv2.imwrite(new_filename, resized_image)

        info.write("%s 1 0 0 %d %d\n" % (new_filename_bis, size, size))
    except:
        print "Error file : %s" % (filename)

info.close()
print "Number of files in positive: %s" % str(len(glob.glob("data/learning_images/positive/*.pgm")))



# negative image
bg = open("model/bg.dat", "w")
i = 0
for filename in glob.glob("data/negatives/*.jpg"):
    img = cv2.imread(filename)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    height,width,channel  = img.shape
    #elements = filename.split("\\")
    for j in range(2000):
        try:
            random_size = random.randint(size/2, size + (size/2))
            x = random.randint(0,height-random_size)
            y = random.randint(0,width-random_size)
            croped = gray[x:x+random_size, y:y+random_size]
            croped_filename = "data/learning_images/negative/" + str(i) + "_" + str(j) +".pgm" 
            croped_filename_bis = "../" + croped_filename
            cv2.imwrite(croped_filename, croped)
            bg.write("%s\n" % (croped_filename_bis))
            #bg.write("%s 1 0 0 %d %d\n" % (croped_filename_bis, size, size))
        except:
            print "Error file : %s : %d" % (filename, j)
    i+= 1

bg.close()

print "Number of files in negative: %s" % str(len(glob.glob("data/learning_images/negative/*.pgm"))) 


