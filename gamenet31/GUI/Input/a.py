#In the name of God
# -*- coding: cp1256 -*-
# -*- coding: utf-8 -*-
#!usr/bin/env python

import wx
import auiconsol2 as a


class gimframe(wx.Frame):
    def __init__(self,parent):
        wx.Frame.__init__(self,parent,style=wx.FRAME_FLOAT_ON_PARENT|wx.DEFAULT_FRAME_STYLE)
        
        self.parent = parent

                
        
        panel = a.MyPanel1(self,u'دستگاه')
        
    def closeit(self):
        self.Close(True)    
        
def size():
    return (160,300)

def main(panel=None ):
    locale = wx.Locale(wx.LANGUAGE_ENGLISH)
    
    parent =  panel.GetParent()
    
    frame = gimframe(parent )
    frame.SetTitle(u'کنسول')
    frame.SetSize((160,300))
    frame.Show()        



if __name__ == '__main__':
    main()
    
