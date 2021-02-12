from time import sleep, time
import datetime

start_time = time()

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
    'L1': 30,           # 1
    'L2': 31,           # 2
    'L3': 32,           # 3
    'R1': 20,           # q
    'R2': 26,           # w
    'R3': 8,            # e
    'arrowl': 80,
    'arrowr': 79,
    'arrowu': 82,
    'arrowd': 81,
    'options': 18       # o
}

key_press_short = 250
key_press_default = 500
key_press_long = 2000
key_press_v_long = 4000
key_dwell_default = 1000
key_dwell_long = 2000

key_queue = []

def LogStep(txt):
    key_queue.append(['log', txt])

def KeyPress(keys, press_length='default', dwell_length='default'):
    if press_length == 'v_long':
        press_duration = key_press_v_long
    elif press_length == 'long':
        press_duration = key_press_long
    elif press_length == 'short':
        press_duration = key_press_short
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
    KeyPress('circle circle', press_length='short')

def EnterSHDMenu():
    LogStep("Enter SHD Menu")
    EnterInventory()
    KeyPress('down down down down down right right', press_length='short')
    KeyPress('X')
    KeyPress('down right', press_length='short')
    KeyPress('X')

def ExitSHDMenu():
    LogStep("Exit SHD Menu")
    KeyPress('circle circle', press_length='short')
    ExitInventory()

def EnterShopMenu():
    LogStep("Enter Shop Menu")
    KeyPress('square', press_length='long')

def ExitShopMenu():
    LogStep("Exit Shop Menu")
    KeyPress('circle', press_length='short')

def EnterFactionMenu():
    LogStep("Enter Faction Menu")
    KeyPress('square', press_length='long')
    KeyPress('down down down down X')
    KeyPress('R2 down down down R2')

def ExitFactionMenu():
    LogStep("Exit Shop Menu")
    KeyPress('circle circle circle', press_length='short')


def ScavengeMaterials(materials):
    EnterSHDMenu()
    for material in materials:
        thrown_error = False

        if material[0] == "credits":
            KeyPress('') # Correct position
        elif material[0] == "ceramics":
            KeyPress('down', press_length='short')
        elif material[0] == "polycarbonate":
            KeyPress('down down', press_length='short')
        elif material[0] == "steel":
            KeyPress('down down down', press_length='short')
        elif material[0] == "carbon":
            KeyPress('down down down down', press_length='short')
        elif material[0] == "electronics":
            KeyPress('down down down down down', press_length='short')
        elif material[0] == "titanium":
            KeyPress('down down down down down down', press_length='short')
        elif material[0] == "filament":
            KeyPress('down down down down down down down', press_length='short')
        elif material[0] == "shd":
            KeyPress('down down down down down down down down', press_length='short')
        elif material[0] == "field":
            KeyPress('down down down down down down down down down', press_length='short')
        else:
            thrown_error = "INVALID TYPE"

        try:
            material_item_qty = int(material[1])
        except:
            thrown_error = "INVALID QTY"

        if not thrown_error:
            LogStep("Buying %s - %s" % (material[0], material[1]))
            for x in range(material_item_qty):
                KeyPress('X', press_length='long')
        else:
            LogStep(thrown_error)

        # Soft Reset SHDMenu
        KeyPress('circle', press_length='short')
        KeyPress('X')

    ExitSHDMenu()

def WriteReport(report):
    True
    # with open('/dev/hidg0', 'rb+') as fd:
    #     fd.write(report.encode())

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
            print "\n"
            print k[1]

    print "Runtime:", str(datetime.timedelta(seconds=(int(time() - start_time))))
