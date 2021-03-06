# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 15:44:11 2016

@author: prassanna
"""

import argparse
import threading
import pyscreenshot
from datetime import datetime

parser = argparse.ArgumentParser(description = 'Screenshot App')
parser.add_argument('--folder', help='Folder to dump',default="/home/prassanna/Pictures/")
parser.add_argument('--time', type=int, help='Take screenshot after "T" seconds', default=0, nargs='?')
parser.add_argument('--repeat', type=bool, help='Repeat Screenshot every T seconds', default=0, nargs='?')
args=parser.parse_args();



filename_prefix = "Screenshot_"

words=["one", "two", "three", "four", "five", "six", "seven", "eight","nine", 
       "ten", "eleven", "twelve", "thirteen", "fourteen", "quarter", "sixteen",
       "seventeen", "eighteen", "nineteen", "twenty", "twenty one", 
       "twenty two", "twenty three", "twenty four", "twenty five", 
       "twenty six", "twenty seven", "twenty eight", "twenty nine", "half"]
         
 
         
 
def caltime(header= "It is "):
    dd=datetime.now()    
    msg = header+str(dd.year)+"-"+str(dd.month)+"-"+str(dd.day)+"_"+str(dd.hour)+":"+str(dd.minute)+":"+str(dd.second)
    return msg;
        

def take_screenshot():
    img = pyscreenshot.grab();
    img.save(caltime(args.folder+filename_prefix)+".png")    
    print "Screenshot Taken"


t = threading.Timer(args.time,take_screenshot)    
if(args.repeat==True):
    while(True):        
        t.start();
        import time
        time.sleep(args.time)
        t = threading.Timer(args.time,take_screenshot)    
        
else:
    t.start();
    
