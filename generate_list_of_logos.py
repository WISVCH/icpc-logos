#!/usr/bin/env python3
import json

print("## List of logos\n")

print("""### Legend

| Status | description |
|---|---|
| :x: | Missing |
| :question: | Present, but needs verification |
| :heavy_check_mark: | Verified
""")

print("### Universities\n")

print("| Logo | ICPC ID | Name | Status |\n|---|---|---|---|")

with open('universities/organizations.json', 'r') as f:
  oragnizations = json.load(f)

for o in oragnizations:
    print(f"| <img src=\"./universities/logos/{o['id']}.svg\" width=\"32\" height=\"32\"> | {o['id']} |  {o['formal_name']} | :heavy_check_mark: |")


print("\n### Companies\n")

print("| Logo | ID | Name | Status |\n|---|---|---|---|")

with open('companies/organizations.json', 'r') as f:
  oragnizations = json.load(f)

for o in oragnizations:
    print(f"| <img src=\"./companies/logos/{o['id']}.svg\" width=\"32\" height=\"32\"> | {o['id']} |  {o['formal_name']} | :heavy_check_mark: |")


print("\n### Studies\n")

print("| Icon 1 | Icon 2 | Icon 3 | Icon 4 | ID | Name | Status |\n|---|---|---|---|---|---|---|")

with open('studies/organizations.json', 'r') as f:
  oragnizations = json.load(f)

for o in oragnizations:
    s = ""

    if len(o["studies"]) >= 1:
        s += f"| <img src=\"./studies/logos/{o['studies'][0]}.svg\" width=\"16\" height=\"16\"> "
    else:
        s += f"|   "

    if len(o["studies"]) >= 2:
        s += f"| <img src=\"./studies/logos/{o['studies'][1]}.svg\" width=\"16\" height=\"16\"> "
    else:
        s += f"|   "

    if len(o["studies"]) >= 3:
        s += f"| <img src=\"./studies/logos/{o['studies'][2]}.svg\" width=\"16\" height=\"16\"> "
    else:
        s += f"|   "

    if len(o["studies"]) >= 4:
        s += f"| <img src=\"./studies/logos/{o['studies'][3]}.svg\" width=\"16\" height=\"16\"> "
    else:
        s += f"|   "

    s += f"| {o['id']} |  {o['formal_name']} | :heavy_check_mark: |"

    print(s)


print("\n### Others\n")

print("| Logo | ID | Name | Status |\n|---|---|---|---|")

with open('others/organizations.json', 'r') as f:
    oragnizations = json.load(f)

for o in oragnizations:
    print(f"| <img src=\"./others/logos/{o['id']}.svg\" width=\"32\" height=\"32\"> | {o['id']} |  {o['formal_name']} | :heavy_check_mark: |")
