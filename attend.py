import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import sys
import time
import pybase64

#start web cam
cap=cv2.Videocapture(0)

names=[]

#function for attendance file

fob=open('attendance.txt','+a')
def enterData(z):
    if z in names:
        pass
    else:
        names.append(z)
        z=".join(str(z))"
        fob.write(z+'\n')
        return names
    
print("reading code")



#function data present or not


def checkData(data):
    data=str(data)
    if data in names:
        print("already present")
    else:
        print("\n"+str(len(names)+1)+'\n'+'present done')
        enterData(data)
        
        
        
while True:
    _,frame =cap.read()
    decodeobject =pyzbar.decode(frame)
    for obj in decodeobject:
        checkData(obj.Data)
        time.sleep(1)
        
    cv2.imshow('Frame',frame)
    
    
    #close
    if cv2.waitkey(1)&0xff==ord('s'):
        cv2.destroyeAllWindows()
        break

fob.close()
        

