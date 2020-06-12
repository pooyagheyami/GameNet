#In the name of God
# -*- coding: cp1256 -*-
# -*- coding: utf-8 -*-
#!usr/bin/env python


#import os
#import sys
import wx


def size():
    return (-1,-1)

def main(panel=None):
    
    q= wx.GetActiveWindow()
    #print q
    if str(q) == 'None':
        quit()
    else:
        q.Destroy()
    #quit()
    
if __name__ == '__main__':
    main(None)
