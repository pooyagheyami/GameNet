#In the name of God
# -*- coding: cp1256 -*-
# -*- coding: utf-8 -*-
#!usr/bin/env python

import wx
import newmem


class memframe(wx.Frame):
    def __init__(self,parent):
        wx.Frame.__init__(self,parent,style=wx.FRAME_FLOAT_ON_PARENT|wx.DEFAULT_FRAME_STYLE)
        self.parent = parent

                
        
        panel = newmem.MyPanel1(self)
        
        
        
    def closeit(self):
        self.Close(True)

        
def size():
    return (350,380)

def main(panel=None ):
    locale = wx.Locale(wx.LANGUAGE_ENGLISH)
    
    parent =  panel.GetParent()
    
    frame = memframe(parent )
    frame.SetTitle(u'اعلان')
    frame.SetSize((350,380))
    frame.Show()
    


if __name__ == '__main__':
    main()
