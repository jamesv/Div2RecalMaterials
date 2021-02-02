import sys
from helpers import *

import argparse, sys

parser=argparse.ArgumentParser()

parser.add_argument('--credits', help='Qty of ECredits', type= int, default= 0)
parser.add_argument('--shd', help='Qty of SHD Calibratioo', type= int, default= 0)
parser.add_argument('--field', help='Qty of Field Recon Data', type= int, default= 0)

args=parser.parse_args()
materials_to_scavenge = []

if args.credits > 0:
    materials_to_scavenge.append(['credits', args.credits])
if args.shd > 0:
    materials_to_scavenge.append(['shd', args.shd])
if args.field > 0:
    materials_to_scavenge.append(['field', args.field])

ScavengeMaterials(materials_to_scavenge)

ProcessQueue(key_queue)
