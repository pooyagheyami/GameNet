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
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 360,310 ), style = wx.TAB_TRAVERSAL )

		self.SetLayoutDirection(2)
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.Text1 = wx.StaticText( self, wx.ID_ANY, u"نام بازی", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_CENTRE )
		self.Text1.Wrap( -1 )
		bSizer2.Add( self.Text1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.Ctrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.Ctrl1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.Text2 = wx.StaticText( self, wx.ID_ANY, u"کد بازی", wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
		self.Text2.Wrap( -1 )
		bSizer2.Add( self.Text2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.Ctrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		bSizer2.Add( self.Ctrl2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.button1 = wx.Button( self, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		bSizer2.Add( self.button1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.Text3 = wx.StaticText( self, wx.ID_ANY, u"سال ساخت", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_CENTRE )
		self.Text3.Wrap( -1 )
		bSizer3.Add( self.Text3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.Ctrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		bSizer3.Add( self.Ctrl3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.Text4 = wx.StaticText( self, wx.ID_ANY, u"ورژن", wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		self.Text4.Wrap( -1 )
		bSizer3.Add( self.Text4, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.Ctrl4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		bSizer3.Add( self.Ctrl4, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.Text5 = wx.StaticText( self, wx.ID_ANY, u"ریجن", wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		self.Text5.Wrap( -1 )
		bSizer3.Add( self.Text5, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.Ctrl5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		bSizer3.Add( self.Ctrl5, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )
		
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_checkBox1 = wx.CheckBox( self, wx.ID_ANY, u"آنلاین؟", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_checkBox1, 1, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_checkBox2 = wx.CheckBox( self, wx.ID_ANY, u"شبکه؟", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_checkBox2, 1, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.Text6 = wx.StaticText( self, wx.ID_ANY, u"تعداد بازیکنها", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Text6.Wrap( -1 )
		bSizer4.Add( self.Text6, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.spinCtrl1 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS, 1, 10, 1 )
		bSizer4.Add( self.spinCtrl1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer4, 1, wx.EXPAND, 5 )
		
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.Text7 = wx.StaticText( self, wx.ID_ANY, u"قیمت", wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
		self.Text7.Wrap( -1 )
		bSizer5.Add( self.Text7, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.Ctrl6 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.Ctrl6, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		choice1Choices = [ u"ریال", u"تومان" ]
		self.choice1 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choice1Choices, 0 )
		self.choice1.SetSelection( 0 )
		bSizer5.Add( self.choice1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer5, 1, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.button2 = wx.Button( self, wx.ID_ANY, u"انصراف", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.button2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.button3 = wx.Button( self, wx.ID_ANY, u"خریداری شد", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.button3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer6, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		# Connect Events
		self.button1.Bind( wx.EVT_BUTTON, self.Onlist )
		self.button2.Bind( wx.EVT_BUTTON, self.Oncancel )
		self.button3.Bind( wx.EVT_BUTTON, self.Onbuy )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def Onlist( self, event ):
		event.Skip()
	
	def Oncancel( self, event ):
		q = self.GetParent()
		q.Close()
		return -1
	
	def Onbuy( self, event ):
                data = ()
                f1 = self.Ctrl1.GetValue()
                f2 = self.Ctrl2.GetValue()
                f3 = self.Ctrl3.GetValue()
                f4 = self.Ctrl4.GetValue()
                f5 = self.Ctrl5.GetValue()
                f6 = self.m_checkBox1.GetValue()
                f7 = self.m_checkBox2.GetValue()
                f8 = self.spinCtrl1.GetValue()
                f9 = self.Ctrl6.GetValue()

                data = (f1,int(f2),int(f3),f4,f5,f6,f7,f8,int(f9))
                                
		#a=DB.WXDB("..\gamenet2\Database\gamenet.db")
                #a.insert('Games','(Game,Code,year,ver,Rg,online,lan,User,price)',data)    
                #a.close()

                q = self.GetParent()
		q.Close()
		return -1
	

