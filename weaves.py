import sys
from helpers import *

item_pos = int(sys.argv[1])
item_type = sys.argv[2]
item_qty = int(sys.argv[3])

num_items_to_process_at_once = 100

# Acquire Funds
LogStep("Acquire Funds")
LogStep("-------------")
EnterSHDMenu()
for x in range(item_qty):
    KeyPress('X', press_length='long')
ExitSHDMenu()

# Buy Items
LogStep("Buy & Deconstruct Items")
LogStep("-----------------------")

total_remaining_items_to_process = item_qty
while total_remaining_items_to_process > 0:
    # Check for qty to run in this batch
    if(total_remaining_items_to_process > num_items_to_process_at_once):
        num_items_to_process_now = num_items_to_process_at_once
    else:
        num_items_to_process_now = total_remaining_items_to_process

    # Buy Batch of Items
    LogStep("Buy Batch of Items")
    EnterShopMenu()
    # Move to item in shop
    for x in range(item_pos - 1):
        KeyPress('down')
    # repeatedly buy item from shop
    for x in range(num_items_to_process_now):
        KeyPress('X X')
    ExitShopMenu()


    # Deconstruct Batch of Items
    thrown_error = False
    LogStep("Junk & Deconstruct Batch of Items")
    EnterInventory()
    # Move to proper inventory bucket
    LogStep(item_type)
    if (item_type == "weapon"):
        KeyPress('down')
    elif (item_type == "pistol"):
        KeyPress('down right right')
    elif (item_type == "mask"):
        KeyPress('down down')
    elif (item_type == "chest"):
        KeyPress('down down down')
    elif (item_type == "holster"):
        KeyPress('down down down down')
    elif (item_type == "backpack"):
        KeyPress('down down right')
    elif (item_type == "gloves"):
        KeyPress('down down down right')
    elif (item_type == "kneepads"):
        KeyPress('down down down down right')
    else:
        thrown_error = "bad type"

    if not thrown_error:
        KeyPress('X')

        # Select items and mark as Junk
        KeyPress('down')
        if (item_type == "weapon") :
            KeyPress('down')
        for x in range(num_items_to_process_now):
            KeyPress('L2')

        # Deconstruct Junk
        KeyPress('R3', press_length='v_long', dwell_length='long')
        KeyPress('X X', dwell_length='long')
    else:
        LogStep("ERROR: bad item_type")
    ExitInventory()

    # Decriment and move to next batch
    total_remaining_items_to_process -= num_items_to_process_now


ProcessQueue(key_queue)
