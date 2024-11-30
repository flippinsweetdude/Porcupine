#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd2in7_V2
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

import subprocess


logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("epd2in7 Demo")   
    epd = epd2in7_V2.EPD()
    
    '''2Gray(Black and white) display'''
    logging.info("init and Clear")
    epd.init()
    epd.Clear()
    font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
    font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)
    font35 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 35)
    
    #epd.init_Fast()
    
    # Drawing on the Horizontal image
    logging.info("4.Drawing on the Horizontal image...")
    Himage = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
    draw = ImageDraw.Draw(Himage)
    
    draw.text((10, 0), 'hello world', font = font24, fill = 0)
    draw.text((150, 0), u'微雪电子', font = font24, fill = 0)   

    draw.line((2, 32,264, 32), fill=0)  # horizontal line top
    
    #bottom section segments
    draw.line((2,156,264,156), fill=0)  # horizontal line bottom
    draw.line((50,156,50,175), fill=0)  # leftmost bottom seperator
    draw.line((100,156,100,175), fill=0) # middle bottom seperator
    draw.line((188,156,188,175), fill=0) #time line ( right )
    

    draw.line((20, 50, 70, 100), fill = 0)
    draw.line((70, 50, 20, 100), fill = 0)
    draw.rectangle((20, 50, 70, 100), outline = 0)
    
    draw.line((165, 50, 165, 100), fill = 0)
    draw.line((140, 75, 190, 75), fill = 0)
    draw.arc((140, 50, 190, 100), 0, 360, fill = 0)
    
    #draw.rectangle((80, 50, 130, 100), fill = 0)  #  make a filled in rectangle
    #draw.chord((200, 50, 250, 100), 0, 360, fill = 0)  # make a filled in circle

    epd.display_Base(epd.getbuffer(Himage))
    
    #time.sleep(2)

    dbWidth = 50
    dbHeight = 30
    dbXoffset = 10
    dbYoffset = 157

    # update the time in bottom right 
    timeWidth = 100
    timeHeight = 30
    timeXoffset = 192
    timeYoffset = 157
    num = 0
    while (True):
        iwlistCommand = "iwlist wlan0 scan | grep -oP 'Signal level=\K.* ' "
        ps = subprocess.Popen(iwlistCommand, shell=True,stdout=subprocess.PIPE)
        dBLevel = ps.communicate()[0].decode('ASCII').replace('\n','').strip()
        print (dBLevel)
        
        draw.rectangle((dbXoffset, dbYoffset, dbWidth + dbXoffset, dbHeight + dbYoffset), fill = 255)
        draw.text((dbXoffset, dbYoffset), dBLevel, font = font18, fill = 0)
        dbImage = Himage.crop([dbXoffset, dbYoffset, dbWidth + dbXoffset, dbHeight + dbYoffset])
        Himage.paste(dbImage, (dbXoffset, dbYoffset))
        epd.display_Partial(epd.getbuffer(Himage), dbYoffset, epd.height - (dbWidth + dbXoffset), dbYoffset + dbHeight, epd.height - 10)

        draw.rectangle((timeXoffset, timeYoffset, timeWidth + timeXoffset, timeHeight + timeYoffset), fill = 255)
        draw.text((timeXoffset, timeYoffset), time.strftime('%H:%M:%S'), font = font18, fill = 0)
        newimage = Himage.crop([timeXoffset, timeYoffset, timeWidth + timeXoffset, timeHeight + timeYoffset])
        Himage.paste(newimage, (timeXoffset, timeYoffset)) 
        epd.display_Partial(epd.getbuffer(Himage), timeYoffset, epd.height - (timeWidth + timeXoffset), timeYoffset + timeHeight, epd.height - 10)
        

        num = num + 1
        if(num == 5):
            break

    
    #logging.info("Clear...")
    #epd.init()   
    #epd.Clear()
    #logging.info("Goto Sleep...")
    epd.sleep()
        
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd2in7_V2.epdconfig.module_exit(cleanup=True)
    exit()
