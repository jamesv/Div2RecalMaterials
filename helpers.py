from time import sleep

NULL_CHAR = chr(0)

key_map = {
    'X': 27,            # x
    'square': 22,       # s
    'triangle': 23,     # t
    'circle': 6,        # c
    'up': 24,           # u
    'down': 7,          # d
    'left': 15,         # l
    'right': 21,        # r
    'L2': 31,           # 2
    'R3': 8,            # e
    'arrowl': 80,
    'arrowr': 79,
    'arrowu': 82,
    'arrowd': 81,
    'options': 18       # o
}

key_press_default = 300
key_press_long = 2000
key_press_v_long = 4000
key_dwell_default = 700
key_dwell_long = 2000

key_queue = []

def LogStep(txt):
    key_queue.append(['log', txt])

def KeyPress(keys, press_length='default', dwell_length='default'):
    if press_length == 'v_long':
        press_duration = key_press_v_long
    elif press_length == 'long':
        press_duration = key_press_long
    else:
        press_duration = key_press_default

    if dwell_length == 'long':
        dwell_duration = key_dwell_long
    else:
        dwell_duration = key_dwell_default
    keys = keys.split()
    for key in keys:
        key_queue.append(['key', key, press_duration, dwell_duration])

def EnterInventory():
    LogStep("Enter Inventory")
    KeyPress('options', press_length='long')

def ExitInventory():
    LogStep("Exit Inventory")
    KeyPress('circle circle')

def EnterSHDMenu():
    LogStep("Enter SHD Menu")
    EnterInventory()
    KeyPress('down down down down down right right X')
    KeyPress('down right X')

def ExitSHDMenu():
    LogStep("Exit SHD Menu")
    KeyPress('circle circle')
    ExitInventory()

def EnterShopMenu():
    LogStep("Enter Shop Menu")
    KeyPress('square', press_length='long')

def ExitShopMenu():
    LogStep("Exit Shop Menu")
    KeyPress('circle')

def WriteReport(report):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report.encode())

def ProcessQueue(key_queue):
    # Press those buttons
    for k in key_queue:
        if k[0] == "key":
            print "%s - %s, %s" % (k[1], k[2], k[3])
            #press
            WriteReport(NULL_CHAR*2+chr(key_map[k[1]])+NULL_CHAR*5)
            sleep(float(k[2])/1000)

            #release
            WriteReport(NULL_CHAR*8)
            sleep(float(k[3])/1000)

        elif k[0] == "log":
            print k[1]
