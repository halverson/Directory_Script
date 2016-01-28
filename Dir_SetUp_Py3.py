#!/usr/local/bin/python3

import os

x = ["01_WorkingFiles", "02_Inspiration", "03_Source", "04_SendOff", "05_FA"]

for i in x:
    os.mkdir(i, mode=0o777)

print("Folders Created")
