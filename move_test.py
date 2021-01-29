import sys
from helpers import *

LogStep("Move Around")
LogStep("-----------")
KeyPress('down')
KeyPress('down')
KeyPress('down')
KeyPress('right')
KeyPress('up')
KeyPress('up')
KeyPress('up')
KeyPress('left')
ProcessQueue(key_queue)
