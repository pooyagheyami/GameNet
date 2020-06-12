# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.aui
import wx.lib.masked  as masked
import datetime
import time

###########################################################################
## Class MyPanel1
###########################################################################

class MyPanel1 ( wx.Panel ):
	
	def __init__( self, parent , lbl ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 160,300 ), style = wx.TAB_TRAVERSAL )

		self.SetLayoutDirection(2)

		self.Cdata=[]
		self.ndata = []
		self.m_mgr = wx.aui.AuiManager()
		self.m_mgr.SetManagedWindow( self )
		self.m_mgr.SetFlags(wx.aui.AUI_MGR_DEFAULT)
		
		self.PsPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 160,300 ), wx.TAB_TRAVERSAL )
		self.m_mgr.AddPane( self.PsPanel, wx.aui.AuiPaneInfo() .Center().MaximizeButton( True ) .CloseButton( False ).Dock().Fixed().Layer( 1 ) )


		
		VSz1 = wx.BoxSizer( wx.VERTICAL )
		
		HSz1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.BMon = wx.StaticBitmap( self.PsPanel, wx.ID_ANY, wx.Bitmap( u".\Icons\ledoff.bmp", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		HSz1.Add( self.BMon, 0, wx.ALL, 5 )
		
		self.StNo = wx.StaticText( self.PsPanel, wx.ID_ANY, lbl, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.StNo.Wrap( -1 )
		HSz1.Add( self.StNo, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.BMlan = wx.StaticBitmap( self.PsPanel, wx.ID_ANY, wx.Bitmap( u".\Icons\ledoff.bmp", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		HSz1.Add( self.BMlan, 0, wx.ALL, 5 )
		
		
		VSz1.Add( HSz1, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		HSz2 = wx.BoxSizer( wx.HORIZONTAL )

		self.timse = u'00'
                self.timmi = u'00'
                self.timhr = u'00'
                self.lbltime = self.timhr+':'+self.timmi+':'+self.timse
		
		self.Txt1 = wx.StaticText( self.PsPanel, wx.ID_ANY, u"زمان جاری", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Txt1.Wrap( -1 )
		HSz2.Add( self.Txt1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.time1 = wx.TextCtrl( self.PsPanel, wx.ID_ANY, self.lbltime, wx.DefaultPosition, wx.DefaultSize, 0 )
		HSz2.Add( self.time1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		VSz1.Add( HSz2, 1, wx.EXPAND, 5 )
		
		HSz3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.Bmp3 = wx.BitmapButton( self.PsPanel, wx.ID_ANY, wx.Bitmap( u".\Icons\stop.bmp", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		HSz3.Add( self.Bmp3, 0, wx.ALL, 5 )
		
		self.Bmp2 = wx.BitmapButton( self.PsPanel, wx.ID_ANY, wx.Bitmap( u".\Icons\pase.bmp", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		HSz3.Add( self.Bmp2, 0, wx.ALL, 5 )
		
		self.Bmp1 = wx.BitmapButton( self.PsPanel, wx.ID_ANY, wx.Bitmap( u".\Icons\play.bmp", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		HSz3.Add( self.Bmp1, 0, wx.ALL, 5 )
		
		
		VSz1.Add( HSz3, 1, wx.EXPAND, 5 )
		
		HSz4 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.Txt2 = wx.StaticText( self.PsPanel, wx.ID_ANY, u"مبلغ جاری", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Txt2.Wrap( -1 )
		HSz4.Add( self.Txt2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.amont1 = wx.TextCtrl( self.PsPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		HSz4.Add( self.amont1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		VSz1.Add( HSz4, 1, wx.EXPAND, 5 )
		
		Hsz5 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.Bmp6 = wx.BitmapButton( self.PsPanel, wx.ID_ANY, wx.Bitmap( u".\Icons\option.bmp", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		Hsz5.Add( self.Bmp6, 0, wx.ALL, 5 )
		
		self.Bmp5 = wx.BitmapButton( self.PsPanel, wx.ID_ANY, wx.Bitmap( u".\Icons\gampad.bmp", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		Hsz5.Add( self.Bmp5, 0, wx.ALL, 5 )
		
		self.Bmp4 = wx.BitmapButton( self.PsPanel, wx.ID_ANY, wx.Bitmap( u".\Icons\cheng.bmp", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		Hsz5.Add( self.Bmp4, 0, wx.ALL, 5 )
		
		
		VSz1.Add( Hsz5, 1, wx.EXPAND, 5 )
		
		HSz6 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btn1 = wx.Button( self.PsPanel, wx.ID_ANY, u"دریافت", wx.DefaultPosition, wx.DefaultSize, 0 )
		HSz6.Add( self.btn1, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		

		VSz1.Add( HSz6, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.t1 = datetime.timedelta(0,0)
		
		
		self.PsPanel.SetSizer( VSz1 )
		
		
		self.m_mgr.Update()
		#self.Layout()
		
		# Connect Events
		self.Bmp3.Bind( wx.EVT_BUTTON, self.OnStop )
		self.Bmp2.Bind( wx.EVT_BUTTON, self.OnPase )
		self.Bmp1.Bind( wx.EVT_BUTTON, self.OnPlay )
		self.Bmp6.Bind( wx.EVT_BUTTON, self.OnOpt )
		self.Bmp5.Bind( wx.EVT_BUTTON, self.OnPad )
		self.Bmp4.Bind( wx.EVT_BUTTON, self.OnChng )
		self.btn1.Bind( wx.EVT_BUTTON, self.OnRcv )
	
	def __del__( self ):
		self.m_mgr.UnInit()
		
	
	
	# Virtual event handlers, overide them in your derived class
	def OnStop( self, event ):
		self.Bmp1.SetBitmap( wx.Bitmap( u".\Icons\play.bmp", wx.BITMAP_TYPE_ANY ) )
		self.Bmp2.SetBitmap( wx.Bitmap( u".\Icons\pase.bmp", wx.BITMAP_TYPE_ANY ) )
	        self.BMon.SetBitmap( wx.Bitmap( u".\Icons\ledoff.bmp", wx.BITMAP_TYPE_ANY ) )
	        
	        self.PsPanel.Layout()
	        self.m_mgr.Update()
	        self.timer.Stop()
	        
	def OnPase( self, event ):
		self.Bmp2.SetBitmap( wx.Bitmap( u".\Icons\pase2.bmp", wx.BITMAP_TYPE_ANY ) )
		self.Bmp1.SetBitmap( wx.Bitmap( u".\Icons\play.bmp", wx.BITMAP_TYPE_ANY ) )
		self.BMlan.SetBitmap( wx.Bitmap( u".\Icons\ledon.bmp", wx.BITMAP_TYPE_ANY ) )
		self.PsPanel.Layout()
		self.m_mgr.Update()
		self.timer.Stop()
	
	def OnPlay( self, event ):
		self.Bmp1.SetBitmap( wx.Bitmap( u".\Icons\\rec.bmp", wx.BITMAP_TYPE_ANY ) )
		
		self.BMon.SetBitmap( wx.Bitmap( u".\Icons\ledon.bmp", wx.BITMAP_TYPE_ANY ) )
		#self.PsPanel.Layout()
		#self.m_mgr.Update()
		
                #self.m_textCtrl9.SetValue(wx.Now()[11:19])
		self.timer=wx.Timer(self)
                self.timer.Start(1000)
                self.Bind(wx.EVT_TIMER, self.OnTimer)
                import Database.Membase as MD
                d=MD.MemDB()
                feilds="Otype text,memcode text,StNo text,Game text,Pad text,lan text,\
	        online text,start text,end text , Amount text,Spec text"
	        d.create(feilds)
                testdata="'','500000','18:35:20','17:20:25','0','1','2','COD','VIP1','111','Level1'"
                d.insert(testdata)
                self.ndata = d.viewall('test')
                #testdata="Amount ='500000',end='16:35:20',start='15:20:25',Game='COD',StNo='VIP1',memcode='141'"
                #d.update(testdata)
                
                
	
	def OnOpt( self, event ):
                opt = wx.Dialog(self)
		pnl =  MyPanel5(opt)
		opt.SetSize((280,250))
		opt.ShowModal()
	
	def OnPad( self, event ):
		opd = wx.Dialog(self)
		pnl = MyPanel4(opd)
		opd.SetSize((200,240))
		opd.ShowModal()
		
	
	def OnChng( self, event ):
                och = wx.Dialog(self)
		pnl = MyPanel3(och)
		och.SetSize((330,200))
		och.ShowModal()
	
	def OnRcv( self, event ):
		event.Skip()
	
        def OnTimer(self, evt):
                self.t1 = self.t1 + datetime.timedelta(0,1)
                self.lbltime =  unicode(self.t1)
                
                secnd=int(self.lbltime[5:7])
                minut = int(self.lbltime[2:4])
                hours = int(self.lbltime[0])

                rate = 50000
                self.amount = (hours*rate)+(minut*rate/60)+(secnd*rate/3600)
                self.time1.SetValue(self.lbltime)
                self.amont1.SetValue(str(self.amount))

       







###########################################################################
## Class MyPanel3
###########################################################################

class MyPanel3 ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 330,200 ), style = wx.TAB_TRAVERSAL )

		self.SetLayoutDirection(2)
		
		bSizer15 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer18 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"تمام حساب از کنسول", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		bSizer18.Add( self.m_staticText7, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer15.Add( bSizer18, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer19 = wx.BoxSizer( wx.HORIZONTAL )
		
		m_choice1Choices = [ u"<مقصد>", u"<مبداء>" ]
		self.m_choice1 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1Choices, 0 )
		self.m_choice1.SetSelection( 1 )
		bSizer19.Add( self.m_choice1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"به ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		bSizer19.Add( self.m_staticText8, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		m_choice2Choices = [ u"<مبداء>", u"<مقصد>" ]
		self.m_choice2 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice2Choices, 0 )
		self.m_choice2.SetSelection( 1 )
		bSizer19.Add( self.m_choice2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer15.Add( bSizer19, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer20 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button3 = wx.Button( self, wx.ID_ANY, u"انصراف", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer20.Add( self.m_button3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_button4 = wx.Button( self, wx.ID_ANY, u"جابجا شود", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer20.Add( self.m_button4, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer15.Add( bSizer20, 1, wx.ALIGN_CENTER, 5 )
		
		
		self.SetSizer( bSizer15 )
		self.Layout()

		# Connect Events
		self.m_choice1.Bind( wx.EVT_CHOICE, self.OnLast )
		self.m_choice2.Bind( wx.EVT_CHOICE, self.OnFrst )
		self.m_button3.Bind( wx.EVT_BUTTON, self.OnCancel )
		self.m_button4.Bind( wx.EVT_BUTTON, self.OnChange )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnLast( self, event ):
		event.Skip()
	
	def OnFrst( self, event ):
		event.Skip()
	
	def OnCancel( self, event ):
		q = self.GetParent()
		q.Close()
		return -1
	
	def OnChange( self, event ):
		event.Skip()
	
	

###########################################################################
## Class MyPanel4
###########################################################################

class MyPanel4 ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 200,240 ), style = wx.TAB_TRAVERSAL )

		self.SetLayoutDirection(2)
		
		bSizer16 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer21 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"بازی دستگاه", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		bSizer21.Add( self.m_staticText9, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		m_choice3Choices = []
		self.m_choice3 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice3Choices, 0 )
		self.m_choice3.SetSelection( 0 )
		bSizer21.Add( self.m_choice3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer16.Add( bSizer21, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer22 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"تعداد دسته متصل", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		bSizer22.Add( self.m_staticText10, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_spinCtrl1 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.SP_ARROW_KEYS, 0, 10, 0 )
		bSizer22.Add( self.m_spinCtrl1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer16.Add( bSizer22, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer23 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_checkBox1 = wx.CheckBox( self, wx.ID_ANY, u"آنلاین", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer23.Add( self.m_checkBox1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_checkBox2 = wx.CheckBox( self, wx.ID_ANY, u"شبکه", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer23.Add( self.m_checkBox2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer16.Add( bSizer23, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer24 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button5 = wx.Button( self, wx.ID_ANY, u"انصراف", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer24.Add( self.m_button5, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_button6 = wx.Button( self, wx.ID_ANY, u"اعمال شود", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer24.Add( self.m_button6, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer16.Add( bSizer24, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer16 )
		self.Layout()

		# Connect Events
		self.m_choice3.Bind( wx.EVT_CHOICE, self.OnSelect )
		self.m_button5.Bind( wx.EVT_BUTTON, self.OnCancel )
		self.m_button6.Bind( wx.EVT_BUTTON, self.OnApply )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnSelect( self, event ):
		event.Skip()
	
	def OnCancel( self, event ):
		q = self.GetParent()
		q.Close()
		return -1
	
	def OnApply( self, event ):
		event.Skip()
	
	
	

###########################################################################
## Class MyPanel5
###########################################################################

class MyPanel5 ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 280,250 ), style = wx.TAB_TRAVERSAL )

		self.SetLayoutDirection(2)
		
		bSizer17 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer25 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"کد عضویت", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		bSizer25.Add( self.m_staticText11, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_button9 = wx.Button( self, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		bSizer25.Add( self.m_button9, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_textCtrl5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer25.Add( self.m_textCtrl5, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer17.Add( bSizer25, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer26 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"<نام>", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		bSizer26.Add( self.m_staticText12, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"<نام خانوادگی>", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		bSizer26.Add( self.m_staticText13, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer17.Add( bSizer26, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer27 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_checkBox3 = wx.CheckBox( self, wx.ID_ANY, u"از شارژ", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer27.Add( self.m_checkBox3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"کدتخفیف", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )
		bSizer27.Add( self.m_staticText14, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_textCtrl6 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer27.Add( self.m_textCtrl6, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer17.Add( bSizer27, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer28 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button7 = wx.Button( self, wx.ID_ANY, u"انصراف", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer28.Add( self.m_button7, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_button8 = wx.Button( self, wx.ID_ANY, u"اعمال شود", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer28.Add( self.m_button8, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer17.Add( bSizer28, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer17 )
		self.Layout()

		# Connect Events
		self.m_button9.Bind( wx.EVT_BUTTON, self.OnSearch )
		self.m_button7.Bind( wx.EVT_BUTTON, self.OnCancel )
		self.m_button8.Bind( wx.EVT_BUTTON, self.OnApply )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnSearch( self, event ):
		event.Skip()
	
	def OnCancel( self, event ):
		q = self.GetParent()
		q.Close()
		return -1
	
	def OnApply( self, event ):
		event.Skip()
	
	
	

                
