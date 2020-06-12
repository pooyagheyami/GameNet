#In the name of God
# -*- coding: cp1256 -*-
# -*- coding: utf-8 -*-
#!usr/bin/env python

import wx
import security1 as sc


class dial():
    def __init__(self):
        #wx.Frame.__init__(self,parent)
        #self.parent = parent
               
        
        self.dlg = sc.Secret(None)
        self.s = self.dlg.ShowModal()
        print self.s
        self.dlg.Destroy()

    def getback(self):
        print self.dlg.back()
        if self.s==5100:
            return 'OK'
        else:
            return 'No'



if __name__ == '__main__':
    app = wx.App(False)
    locale = wx.Locale(wx.LANGUAGE_ENGLISH)
    #frame = gimframe(None)
    #frame.SetTitle(u'عضويت')
    #frame.SetSize((271,151))
    #frame.Show()
    a=dial()
    s=a.getback()
    print s
    
    app.MainLoop()
