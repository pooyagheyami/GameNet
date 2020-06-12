#In the name of God
# -*- coding: cp1256 -*-
# -*- coding: utf-8 -*-
#!usr/bin/env python

import wx
import newmem


class memframe(wx.Frame):
    def __init__(self,parent):
        wx.Frame.__init__(self,parent)
        #self.parent = parent

                
        
        panel = newmem.MyPanel1(self)
        
        
        
        return None



if __name__ == '__main__':
    app = wx.App(False)
    locale = wx.Locale(wx.LANGUAGE_ENGLISH)
    frame = memframe(None)
    frame.SetTitle(u'کاربر')
    frame.SetSize((350,380))
    frame.Show()
    app.MainLoop()
