# In the name of God
# -*- coding: utf-8 -*-
# Windows and Panels main Frame File
#! /usr/bin/env python
# -*- codnig: utf-8 -*-
import wx
#mport wx.dataview
#import Database.Membase as MD

    
class MyPanel(wx.Panel):
    def __init__(self,parent,id,pos,siz,style,ndata=[]):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 142,396 ), style = wx.TAB_TRAVERSAL )

        self.parent = parent
        self.ndata=ndata
        bSizer2 = wx.BoxSizer( wx.VERTICAL )


        self.SetSizer( bSizer2 )
        self.Layout()

    
