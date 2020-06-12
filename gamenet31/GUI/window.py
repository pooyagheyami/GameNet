# -*- coding: cp1256 -*-
# In the name of God
# Main Program Start
#!/usr/bin/env python
# -*- codnig: utf-8 -*-

import wx
import wx.aui

import GUI.MainMenu as MM

import GUI.AuiPanel.Rev as RP
import GUI.AuiPanel.Stat as SP

import GUI.proman as pro
  
class MainWin(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,title=u'اصلي',size=(800,600))

        self.SetLayoutDirection(2)

        #Check config for show or hide aui panels=========
        rps = 1
        sps = 1

        #Menu of Program============== 
        menu = MM.MainMenu()
        statusBar = self.CreateStatusBar()
        imenu=menu.createMenuBar()
        self.SetMenuBar(imenu)
        h= menu.GetItemId()
        h1 = menu.mid
        self.Bind(wx.EVT_MENU_RANGE,self.OnMenu,id =h1, id2=h.GetId())

        #Show aui panels============== 

        #Aui Panels of Program==================
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        self.m_mgr = wx.aui.AuiManager()
        self.m_mgr.SetManagedWindow( self )
        self.m_mgr.SetFlags(wx.aui.AUI_MGR_DEFAULT)

        #panel revnue======================

        self.Rpanel = RP.MyPanel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_mgr.AddPane( self.Rpanel, wx.aui.AuiPaneInfo() .Left() .PinButton( True ).Dock().Resizable().FloatingSize( wx.Size( 37,54 ) ).Layer( 1 ) )
        #self.m_mgr.Bind(wx.EVT_BUTTON,self.OnBtn)
        if rps == 1 :
            self.m_mgr.GetPane(self.Rpanel).Show()
        elif rps == 0:
            self.m_mgr.GetPane(self.Rpanel).Hide()

        #Panel report=======================
           

        self.Stap = SP.MyPanel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,100 ), wx.TAB_TRAVERSAL, )
        self.m_mgr.AddPane( self.Stap, wx.aui.AuiPaneInfo() .Bottom() .PinButton( True ).Dock().Resizable().FloatingSize( wx.Size( 37,54 ) ).Layer( 2 ) )
        #self.m_mgr.Bind(wx.dataview.EVT_DATAVIEW_ITEM_ACTIVATED,self.OnShow)
        if sps == 1 :
            self.m_mgr.GetPane(self.Stap).Show()
        elif sps == 0:
            self.m_mgr.GetPane(self.Stap).Hide()

        
        self.m_mgr.Update()
        self.Centre( wx.BOTH )

        #Show other win in main windows==============
        


    def OnMenu(self,event):
        self.mid = event.GetId()
        #print self.mid
        a = pro.DoProgram(self.mid)
        #print dir(a)
        s = a.size() if 'size' in dir(a) else ()
        
        win1 = wx.Frame(self,-1)
        win1.SetSize(s)
        a.main(win1)

    def OnBtn(self,evt):
        self.mid = evt.GetId()
        #print self.mid
        a = pro.DoProgram(self.mid)
        #print dir(a)
        s = a.size() if 'size' in dir(a) else ()
        
        win2 = wx.Frame(self,-1)
        win2.SetSize(s)
        a.main(win2)
        
    def OnShow(self,event):
        self.Stap.refresh()
        self.Stap.showitem() 
        #self.Stap.Layout()
        #self.m_mgr.Update()
	#self.Centre( wx.BOTH )
             

    
