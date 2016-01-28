#!/usr/bin/python

import os

p1 = "01_WorkingFiles"
p2 = "02_Inspiration"
p3 = "03_Source"
p4 = "04_SendOff"
p5 = "05_FA"

x = [p1, p2, p3, p4, p5]

for i in x:
    os.mkdir(i, 0755)

print "Folders Created"
