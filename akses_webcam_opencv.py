# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 06:45:37 2020

@author: wedus
"""

import cv2

cap = cv2.VideoCapture(0)

while(True):
    ret,frame = cap.read()
    print (ret)
    cv2.imshow("Gambar",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()