# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
#import Database.DBase as DB
###########################################################################
## Class MyPanel1
###########################################################################

class MyPanel1 ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 350,380 ), style = wx.TAB_TRAVERSAL )

		self.SetLayoutDirection(2)
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"نام", wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
		self.m_staticText1.Wrap( -1 )
		bSizer2.Add( self.m_staticText1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_textCtrl1, 1, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"فامیل", wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
		self.m_staticText2.Wrap( -1 )
		bSizer2.Add( self.m_staticText2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_textCtrl2, 1, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"تلفن", wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
		self.m_staticText3.Wrap( -1 )
		bSizer3.Add( self.m_staticText3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_textCtrl3, 1, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )
		
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"آدرس", wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
		self.m_staticText4.Wrap( -1 )
		bSizer4.Add( self.m_staticText4, 0, wx.ALL, 5 )
		
		self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_textCtrl4, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer1.Add( bSizer4, 2, wx.EXPAND, 5 )
		
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_textCtrl5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_textCtrl5, 1, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Email", wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
		self.m_staticText5.Wrap( -1 )
		bSizer5.Add( self.m_staticText5, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer5, 1, wx.EXPAND, 5 )
		
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"کد عضویت", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		self.m_staticText6.Wrap( -1 )
		bSizer6.Add( self.m_staticText6, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_textCtrl6 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_textCtrl6, 1, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_button1 = wx.Button( self, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		bSizer6.Add( self.m_button1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer6, 1, wx.EXPAND, 5 )
		
		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"کد ملی", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		self.m_staticText7.Wrap( -1 )
		bSizer7.Add( self.m_staticText7, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_textCtrl7 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_textCtrl7, 1, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer7, 1, wx.EXPAND, 5 )
		
		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button2 = wx.Button( self, wx.ID_ANY, u"انصراف", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.m_button2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_button3 = wx.Button( self, wx.ID_ANY, u"ثبت شود", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.m_button3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer8, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		# Connect Events
		self.m_button2.Bind( wx.EVT_BUTTON, self.Oncancel )
		self.m_button3.Bind( wx.EVT_BUTTON, self.Onapply )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def Oncancel( self, event ):
		q = self.GetParent()
		q.Close()
		return -1
	
	def Onapply( self, event ):
                data = ()
                f1 = self.m_textCtrl1.GetValue()
            	f2 = self.m_textCtrl2.GetValue()
		f3 = self.m_textCtrl3.GetValue()
		f4 = self.m_textCtrl4.GetValue()
		f5 = self.m_textCtrl5.GetValue()
		f6 = self.m_textCtrl6.GetValue()
		f7 = self.m_textCtrl7.GetValue()
		data = (f1,f2,f3,f4,f5,f6,f7)
		
		#a=DB.WXDB("..\gamenet2\Database\gamenet.db")
                #a.insert('member','(name,family,phone,Address,Mail,Code,Meli)',data)    
                #a.close()

                q = self.GetParent()
		q.Close()
		return -1
	

