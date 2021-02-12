import sys
from helpers import *

import argparse, sys

num_bundles_to_process_at_once = 5

parser=argparse.ArgumentParser()

parser.add_argument('--blacktusk', help='Qty of Black Tusk bundles', type= int, default= 0)
parser.add_argument('--cleaners', help='Qty of Cleaner bundles', type= int, default= 0)
parser.add_argument('--hyenas', help='Qty of Hyena bundles', type= int, default= 0)
parser.add_argument('--outcasts', help='Qty of Outcast bundles', type= int, default= 0)
parser.add_argument('--rikers', help='Qty of Rikers bundles', type= int, default= 0)
parser.add_argument('--truesons', help='Qty of True Sons bundles', type= int, default= 0)

args=parser.parse_args()

faction_resources = {
    'blacktusk' : [['polycarbonate', 18],['carbon', 25],['filament', 25]],
    'cleaners' : [['ceramics', 18],['titanium', 25],['filament', 25]],
    'hyenas' : [['polycarbonate', 18],['electronics', 25],['filament', 25]],
    'outcasts' : [['steel', 18],['carbon', 25],['filament', 25]],
    'rikers' : [['ceramics', 18],['electronics', 25],['filament', 25]],
    'truesons' : [['steel', 18],['titanium', 25],['filament', 25]]
}

def CreateFactionResources(faction, qty):

    total_remaining_bundles_to_process = qty
    while total_remaining_bundles_to_process > 0:
        # Check for qty to run in this batch
        if(total_remaining_bundles_to_process > num_bundles_to_process_at_once):
            num_bundles_to_process_now = num_bundles_to_process_at_once
        else:
            num_bundles_to_process_now = total_remaining_bundles_to_process

        # NOTE - all values hardcoded for stacks of 5
        LogStep("Faction: %s - %s" % (faction, num_bundles_to_process_now))
        ScavengeMaterials(faction_resources[faction])

        # Move to faction
        EnterFactionMenu()

        if faction == "blacktusk":
            KeyPress('') # Correct position
        elif faction == "cleaners":
            KeyPress('down', press_length='short')
        elif faction == "hyenas":
            KeyPress('down down', press_length='short')
        elif faction == "outcasts":
            KeyPress('down down down', press_length='short')
        elif faction == "rikers":
            KeyPress('down down down down', press_length='short')
        elif faction == "truesons":
            KeyPress('down down down down down', press_length='short')

        for i in range(num_bundles_to_process_now):
            LogStep("Buy %s bundle" % faction)
            KeyPress('square', press_length='v_long')

        KeyPress('circle', press_length='short')
        ExitFactionMenu()

        # Decriment and move to next batch
        total_remaining_bundles_to_process -= num_bundles_to_process_now

if args.blacktusk > 0:
    CreateFactionResources("blacktusk", args.blacktusk)
if args.cleaners > 0:
    CreateFactionResources("cleaners", args.cleaners)
if args.hyenas > 0:
    CreateFactionResources("hyenas", args.hyenas)
if args.outcasts > 0:
    CreateFactionResources("outcasts", args.outcasts)
if args.rikers > 0:
    CreateFactionResources("rikers", args.rikers)
if args.truesons > 0:
    CreateFactionResources("truesons", args.truesons)

ProcessQueue(key_queue)
