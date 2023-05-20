#!/usr/bin/env python3

import argparse
import svgutils.transform as sg
import sys
from pathlib import Path
import tempfile

def required_length(nmin,nmax):
    class RequiredLength(argparse.Action):
        def __call__(self, parser, args, values, option_string=None):
            if not nmin<=len(values)<=nmax:
                msg='argument "{f}" requires between {nmin} and {nmax} arguments'.format(
                    f=self.dest,nmin=nmin,nmax=nmax)
                raise argparse.ArgumentTypeError(msg)
            setattr(args, self.dest, values)
    return RequiredLength

def move_center_to(figure: sg.FigureElement, x: int, y: int, scale: float=1.0, org_size: int=24):
    new_size = org_size * scale
    figure.moveto(x-new_size/2, y-new_size/2, scale)



parser = argparse.ArgumentParser()
parser.add_argument('studies', nargs='+', action=required_length(1,4))
parser.add_argument('-o', '--output', help='Output file name', default='stdout')

try:
    args=parser.parse_args()
except argparse.ArgumentTypeError as err:
    print(err)


svgs = []
for s in args.studies:
    path = Path(__file__).parent / "logos" / f"{s}.svg"
    svgs.append(sg.fromfile(path))

template = sg.fromfile(Path(__file__).parent / "template.svg")

logo = template.find_id("logo")

if len(args.studies) == 1:
    icon = svgs[0].getroot()
    move_center_to(icon, 128, 128, scale = 9)
    logo.root.append(icon.root)
elif len(args.studies) == 2:
    icon0 = svgs[0].getroot()
    icon1 = svgs[1].getroot()
    move_center_to(icon0, 90, 90, scale = 6)
    move_center_to(icon1, 256-90, 256-70, scale = 6)
    logo.root.append(icon0.root)
    logo.root.append(icon1.root)
elif len(args.studies) == 3:
    icon0 = svgs[0].getroot()
    icon1 = svgs[1].getroot()
    icon2 = svgs[2].getroot()
    move_center_to(icon0, 128, 70, scale = 5)
    move_center_to(icon1, 70, 180, scale = 5)
    move_center_to(icon2, 256-70, 180, scale = 5)
    logo.root.append(icon0.root)
    logo.root.append(icon1.root)
    logo.root.append(icon2.root)
elif len(args.studies) == 4:
    icon0 = svgs[0].getroot()
    icon1 = svgs[1].getroot()
    icon2 = svgs[2].getroot()
    icon3 = svgs[3].getroot()
    move_center_to(icon0, 75, 75, scale = 4.8)
    move_center_to(icon1, 256-75, 75, scale = 4.8)
    move_center_to(icon2, 75, 256-75, scale = 4.8)
    move_center_to(icon3, 256-75, 256-75, scale = 4.8)
    logo.root.append(icon0.root)
    logo.root.append(icon1.root)
    logo.root.append(icon2.root)
    logo.root.append(icon3.root)

if args.output == "stdout":
    with tempfile.NamedTemporaryFile() as fp:
        template.save(fp.name)
        print(fp.read())
else:
    template.save(args.output)
