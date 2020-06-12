#In the name of God

import sys
import os



MAP = os.getcwd()

if MAP.find(u'\\') > 0:
    SLASH = u'\\'
else:
    SLASH = u'/'
    
#print MAP+SLASH
DATABASE_PATH = u'Database'
ICONS_PATH    = u'Icons'
GUI_PATH      = u'GUI'

UTILITY_PATH  = u'Utility'
CONFIG_PATH   = u'Config'
LOGS_PATH     = u'Logs'

