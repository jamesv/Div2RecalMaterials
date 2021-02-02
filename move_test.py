import sys
from helpers import *

LogStep("Move Around")
LogStep("-----------")
KeyPress('down', press_length='short')
KeyPress('down', press_length='short')
KeyPress('down', press_length='short')
KeyPress('right', press_length='short')
KeyPress('up', press_length='short')
KeyPress('up', press_length='short')
KeyPress('up', press_length='short')
KeyPress('left', press_length='short')
ProcessQueue(key_queue)
