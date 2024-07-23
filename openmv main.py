# Black Grayscale Line Following Example
#
# Making a line following robot requires a lot of effort. This example script
# shows how to do the machine vision part of the line following robot. You
# can use the output from this script to drive a differential drive robot to
# follow a line. This script just generates a single turn value that tells
# your robot to go left or right.
#
# For this script to work properly you should point the camera at a line at a
# 45 or so degree angle. Please make sure that only the line is within the
# camera's field of view.

import sensor, image, time, math,pyb
from pyb import UART

# Tracks a black line. Use [(128, 255)] for a tracking a white line.
GRAYSCALE_THRESHOLD = [(0, 64)]
#uart = UART(3, 19200)

# Each roi is (x, y, w, h). The line detection algorithm will try to find the
# centroid of trhe largest blob in each roi. The x position of the centroids
# will then be averaged with different weights where the most weight is assigned
# to the roi near the bottom of the image and less to the next roi and so on.
L_max =10
thresholds = [(0, 32, -128, 127, -128, 127)]#line threshold
thresholds2 = [(32, 58, -128, -16, -128, 127)] #green threshold
thresholds3 = [(0, 100, 20, 127, -128, 117)]#red threshold
ROIS = [ # [ROI, weight]
        (0, 0, 160, 30, 0.7), # You'll need to tweak the weights for your app
        (0, 30, 160,45, 0.3), # depending on how your robot is setup.
        (0, 75, 160, 35, 0.1)
       ]
ROI = [(0, 0,160 ,120,0.3)]
greenROI = [(0, 20, 160,105, 0.3)]
mainROI = (0,0,160,120)

        #(15, 15, 155, 30, 0.7), # You'll need to tweak the weights for your app
        #(15, 50, 155, 30, 0.3),
        #(15, 85, 155,30, 0.1)
        #(0, 49, -128, 12, -128, 43) thresholds
#print(sensor.get_exposure_us())
#sensor.set_auto_exposure(1)
led = pyb.LED(3)
uart = UART(1, 19200)
red_flag = False#red line flag
refrence_flag = True
green_flag = False #normal green flag
area_firstblob =0
area_middleblob =0
area_lastblob =0
width_firstblob =0
width_middleblob =0
width_lastblob =0
green_flag2 = False #flag of evacuatio green
# Compute the weight divisor (we're computing this so you don't have to make weights add to 1).
weight_sum = 0
counter =0
weight_sum2 = 0.3
flag_anon = False
no_green =0 # number of green blobs
green_y =0
green_pos=0 #position of green
relative_pos =0
intersection_flag = False
y=0
gap_flag2 = False
greenturn_flag = False #flag to turn in green
gap_flag = False #flag to use in gap
selected_green =0 # green blobs to select
green =False
forward_gap_flag = False
double_green = False #flag of two green so they dont send commands while there are 2 green
EXPOSURE_TIME_SCALE =1

for r in ROIS: weight_sum += r[4] # r[4] is the roi weight.
# Camera setup...
sensor.reset() # Initialize the camera sensor.
sensor.set_pixformat(sensor.RGB565) # use grayscale.
sensor.set_framesize(sensor.QQVGA) # use QQVGA for speed.
sensor.set_auto_gain(False) # must be turned off for color tracking
sensor.set_auto_whitebal(False) # must be turned off for color tracking
sensor.skip_frames(time = 500) # Let new settings take affect.
current_exposure_time_in_microsecond  = sensor.get_exposure_us()
clock = time.clock() # Tracks FPS.
sensor.set_auto_exposure(False,  exposure_us=int(current_exposure_time_in_microsecond * EXPOSURE_TIME_SCALE))
#sensor.set_brightness(-1)
while(True):

    clock.tick() # Track elapsed milliseconds between snapshots().
    img = sensor.snapshot() # Take a picture and return the image.
    # print(clock.fps())              # Note: OpenMV Cam runs about half as fast when connected
    #img.draw_rectangle(0, 75, 150, 35, color = (0, 255, 0), thickness = 2, fill = False)
    #img.draw_rectangle(0, 30, 160, 45, color = (0, 255, 0), thickness = 2, fill = False)
    #img.draw_rectangle(0, 0, 160, 30, color = (0, 0, 255), thickness = 2, fill = False)
    #img.drcraw_rectangle(0, 20, 160,105, color = (255, 255, 255), thickness =2, fill =False)
    #img.draw_rectangle(0,0,160,120,color = (255,255,255), thickness = 2, fill=False)
    #img.crop(1, 1, mainROI,copy_to_fb = True)
    centroid_sum = 0
    center_green =0
    y=0
    for m in mainROI:
        red_blob = img.find_blobs(thresholds3,pixels_threshold=200, area_threshold=300,merge=True)

        try:
            if red_blob[0].area()>2500:
                    print(red_blob[0].area())
                    red_flag = True

        except IndexError:
             red_flag = False
#             print("no red")


    for g in greenROI:
        green_blob = img.find_blobs(thresholds2,pixels_threshold=200, area_threshold=300,merge=True)
        try:
              if green_blob :
                    green = True
              else:
                    green = False
              if green_blob[0].area()>2500:
                    green_flag2 = True
                   # print("area of green blob %f" % green_blob[0].area())
              else:
                   green_flag2 = False
                   no_green = len(green_blob)#no. of green blobs
                   if no_green == 2 :
                        green_y = green_blob[0].cy() - green_blob[1].cy()#position between 2 green
                        #print("position between 2 green : %f" % green_y)
                        img.draw_cross(green_blob[1].cx(),green_blob[1].cy())
                        img.draw_rectangle(green_blob[1].rect())
                        if -20<green_y<20:
                           # print("position between 2 green: %f"%green_y)
                           y=2

                        else:

                            selected_green = max(green_blob, key=lambda b:b.cy())
                            img.draw_rectangle(selected_green.rect(), (0, 0,255))
                   elif no_green ==1:
                        selected_green = green_blob[0]
                       # print("no. of pixels %f" % selected_green.pixels())

                   #print("green center of y :%f"%green_blob[0].cy())
                   green_flag =True
                   img.draw_rectangle(green_blob[0].rect())
                   img.draw_cross(green_blob[0].cx(),green_blob[0].cy())



        except IndexError:
                green_flag =False
                no_green =0
    for r in ROIS:

        blobs = img.find_blobs(thresholds, roi=r[0:4], merge=True, pixel_threshold=400) # r[0:4] is roi tuple.
       # print(blobs[0].area())
        if r[4] == 0.7:
            if blobs:
                 counter=0
                 area_firstblob = blobs[0].area()
                 width_firstblob = blobs[0].w()
                 #print("area of first blob %f" % area_firstblob)
                 # if len(blobs)==2 and area_of_middleblob <=1100:
            else:
                 counter =1                   #print("gap")
        if r[4] ==0.3:

             if blobs:
                  if blobs[0].w() >= 75:
                        gap_flag2 = False
                  else:
                        gap_flag2 =True
                  area_middleblob = blobs[0].area()
                  width_middleblob = blobs[0].w()
                #  print("area of middle blob %f" % area_middleblob)


             else:
                  if counter == 1:
                       counter = 2
                #print("area of middle blob %f" % area_of_middleblob)
        if r[4] == 0.1:
              if blobs:
                   area_lastblob = blobs[0].area()
                   width_lastblob = blobs[0].w()
               #    print("area of last blob %f "%area_lastblob)
              else:
                   if counter == 2 :
                       counter = 3



        if counter ==3:
            gap_flag = True
        if area_firstblob >=3000 and width_firstblob >=120 and green == False or area_middleblob >=3000 and width_middleblob >=120 and green == False or area_lastblob >=3000 and width_lastblob >=120 and green == False:
                intersection_flag = True
                print("intersection ahead")
        else:
            intersection_flag = False
        if blobs:
            # Find the blob with the most pixels.
            largest_blob = max(blobs, key=lambda b: b.pixels())
            #print("area of largest blob: %f"% largest_blob.area())
            if r[4] == 0.3:
                #print("width of middle blob %f " % largest_blob.w())
                blob_width = largest_blob.w()
            if green_flag:
                if r[4] == 0.3:
                    middle_blob = largest_blob.area() #area of center line
                   # print("middle blob %f" % middle_blob)
                    if middle_blob >=1400:
                        greenturn_flag = True
                    elif middle_blob <1400:
                        greenturn_flag = False
                    middle_y = largest_blob.cy()#center y of the middle ROI
                    if selected_green:
                        green_pos = middle_y - selected_green.cy()
                if r[4] == 0.1:
                    bottom_x = largest_blob.cx()
                    if selected_green:
                        relative_pos = selected_green.cx()-bottom_x
#                    print("relative position of green: %f"%relative_pos)
            # Draw a rect around the blob.
            img.draw_rectangle(largest_blob.rect())
            img.draw_cross(largest_blob.cx(), largest_blob.cy())
            centroid_sum += largest_blob.cx() * r[4] # r[4] is the roi weight.

    center_pos = (centroid_sum / weight_sum) # Determine center of line.
    refrence_val = (area_firstblob+area_middleblob+area_lastblob) / 3
    print(refrence_val)
    if refrence_val <1000 and refrence_flag == True:
         L_max = L_max +1
        # print("l_max %f" % L_max)
    else :
         refrence_flag = False
        # print("l_max %f" % L_max)
    print("l max %f" % L_max)
    #green_pos = 0
    #green_pos = (largest_blob2.cx(), largest_blob2.cy())
    # Convert the center_pos to a deflection angle. We're using a non-linear
    # operation so that the response gets stronger the farther off the line we
    # are. Non-linear operations are good to use on the output of algorithms
    # like this to cause a response "trigger".
    deflection_angle = 0
    # The 80 is from half the X res, the 60 is from half the Y res. The
    # equation below is just computing the angle of a triangle where the
    # opposite side of the triangle is the deviation of the center position
    # from the center and the adjacent side is half the Y res. This limits
    # the angle output to around -45 to 45. (It's not quite -45 and 45).
    deflection_angle = -math.atan((center_pos-80)/60)
    # Convert angle in radians to degrees.
    deflection_angle = math.degrees(deflection_angle)
    #relative_pos = (center_pos - green_pos)
    # Now you have an angle telling you how much to turn the robot by which
    # incorporates the part of the line nearest to the robot and parts of
    # the line farther away from the robot for a better predictio
    if intersection_flag == True and green == False:
        uart.write('F')
        print("forward intersection")
    if counter >0 and gap_flag2 == True :
        uart.write('F')
        print("Forward gap")
    else:
        if red_flag == True:
            uart.write('S')
            print("red")
            #led.on()
        elif green_flag2 == True:
            print("exit evacuation")
        elif no_green == 2 and -20<green_y<20 :
            uart.write('T')
            print("turn around")
            double_green = True
            time.sleep(2)
        elif green_flag == True :
            #print("green flag %f" % green_flag)
            #print("green turn flag %f" % greenturn_flag)
            print("green position: %f"%green_pos)
            if green_pos <0:
                print("relative position: %f"%relative_pos)
                if 40>=relative_pos >=0 and greenturn_flag == True or 40>=relative_pos >=0 and greenturn_flag == 1 :
                    print("green right")
                    uart.write('R')
                elif -55<=relative_pos<=-15 and greenturn_flag == True or -55<=relative_pos<=-15 and greenturn_flag == 1:
                    print("green left")
                    uart.write('L')
                else:
                    uart.write('F')
                    print("forward")
            elif green_pos>0:
               # print("position of green %f" % green_pos)
                print("forward")
                uart.write('F')
        elif green_flag == False:
            if 17<deflection_angle:
                    uart.write('L')
                    print("L")
            elif -20<=deflection_angle<-10:
                    uart.write('r')
                    print("RS")
            elif -10>deflection_angle  :
                    uart.write('R')
                    print("R")
            elif -10<=deflection_angle<=10 :
                    uart.write('F')
                    print("F")
            elif 17>=deflection_angle>10:
                    uart.write('l')
                    print("ls")


    #elif 5>deflection_angle<45:
      #  uart.write("RS")
     #   print("RS")
    #elif -5>deflection_angle<-45:
        #uart.write("LS")
        #print("LS")
    #-53 -45 l
    #53 45 r
    #-5 5 f
    # 5>angle<45 rs
    # -5>angle<-45 ls;

    print("Turn Angle: %f" % deflection_angle)
    #print(clock.fps()%"fps %f") # Note: Your OpenMV Cam runs about half as fast while
    # connected to your computer. The FPS should increase once disconnected.
