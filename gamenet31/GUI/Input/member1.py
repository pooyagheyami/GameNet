# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from wx.lib import masked
from datetime import date,datetime
import os
from khayyam import *


###########################################################################
## Class MyPanel1
###########################################################################
class DatePicker(wx.DatePickerCtrl):
    def __init__(self,parent,dt,style=wx.DP_DEFAULT):
        super(DatePicker,self).__init__(parent, dt=dt,style=style)
        self.SetInitialSize((20,-1))

class MyPanel1 ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 364,312 ), style = wx.TAB_TRAVERSAL )

		self.SetLayoutDirection(2)

		now = wx.DateTime.Now()
                now1 = JalaliDate.today()
                
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"کد اشتراک", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		bSizer2.Add( self.m_staticText1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		bSizer2.Add( self.m_textCtrl1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_button1 = wx.Button( self, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		bSizer2.Add( self.m_button1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"<نام>", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		bSizer2.Add( self.m_staticText2, 1, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"<نام خانوادگی>", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		bSizer2.Add( self.m_staticText3, 1, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )
		
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"نوع عضویت", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		bSizer4.Add( self.m_staticText5, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		m_choice2Choices = []
		self.m_choice2 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice2Choices, 0 )
		self.m_choice2.SetSelection( 0 )
		bSizer4.Add( self.m_choice2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"کد تخفیف", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		bSizer4.Add( self.m_staticText6, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		bSizer4.Add( self.m_textCtrl3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_button4 = wx.Button( self, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		bSizer4.Add( self.m_button4, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer4, 1, wx.EXPAND, 5 )
		
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"ازتاریخ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		bSizer5.Add( self.m_staticText7, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_datePicker1 = wx.DatePickerCtrl( self, wx.ID_ANY, now, wx.DefaultPosition, wx.DefaultSize, wx.DP_DROPDOWN )
		bSizer5.Add( self.m_datePicker1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"تا تاریخ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		bSizer5.Add( self.m_staticText8, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_datePicker2 = wx.DatePickerCtrl( self, wx.ID_ANY, now, wx.DefaultPosition, wx.DefaultSize, wx.DP_DROPDOWN )
		bSizer5.Add( self.m_datePicker2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"<مدت>", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		bSizer5.Add( self.m_staticText10, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer5, 1, wx.EXPAND, 5 )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"حق عضویت مبلغ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		bSizer3.Add( self.m_staticText4, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		#self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl2 = masked.NumCtrl(self,wx.ID_ANY,name="target control")
		self.m_textCtrl2.SetParameters(integerWidth = 12)

		bSizer3.Add( self.m_textCtrl2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		m_choice1Choices = [ u"ریال", u"تومان" ]
		self.m_choice1 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1Choices, 0 )
		self.m_choice1.SetSelection( 0 )
		bSizer3.Add( self.m_choice1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )
		
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"مبلغ شارژ دریافتی", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		bSizer6.Add( self.m_staticText9, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		#self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl4 = masked.NumCtrl(self,wx.ID_ANY,name="target control")
		self.m_textCtrl4.SetParameters(integerWidth = 12)
		
		bSizer6.Add( self.m_textCtrl4, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		m_choice11Choices = [ u"ریال", u"تومان" ]
		self.m_choice11 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice11Choices, 0 )
		self.m_choice11.SetSelection( 0 )
		bSizer6.Add( self.m_choice11, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer6, 1, wx.EXPAND, 5 )
		
		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button2 = wx.Button( self, wx.ID_ANY, u"انصراف", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_button2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_button3 = wx.Button( self, wx.ID_ANY, u"دریافت گردید", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_button3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer7, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.OnSearch )
		self.m_datePicker2.Bind( wx.EVT_DATE_CHANGED, self.Ondays )
		self.m_button2.Bind( wx.EVT_BUTTON, self.OnCancel )
		self.m_button3.Bind( wx.EVT_BUTTON, self.Oninput )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnSearch( self, event ):
		event.Skip()

	def Ondays( self, event ):
            m = 0 
            D1 =  self.m_datePicker1.GetValue()
            D2 =  event.GetDate()
            D = (D2-D1).days
            if D >= 29 :
                m = D // 30
                s= u'ماه'
            else:
                m = D
                s = u'روز'
                
                

            self.m_staticText10.SetLabel(str(m)+s)
            self.Layout()
		
	def OnCancel( self, event ):
		q = self.GetParent()
		q.Close()
		
	
	def Oninput( self, event ):
            
		q = self.GetParent()
		q.Close()



		
	

