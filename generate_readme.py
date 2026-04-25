#!/usr/bin/env python3
import json

print("""# icpc-logos

## Usage

Download the logos and the `organizations.json` from the releases.
For DOMJudge use the `background_64.zip`.

## Contribution

### University
- Add a university by duplicating one of the existing logos in `universities/logos`, and change the content of the logos group.
  - It is important the logos group still exists, and contains the logo.
  - The logo might already be in the `no_orginazations_yet` directory. Look there first.
- Add the organization to `universities/organizations.json`.
  - As `id`, use the ICPC id, starting with a `U-`.
- Test the export by running `./export.sh`.
  - Inkscape should be installed for this.

### Company
- Add a company by duplicating one of the existing logos in `companies/logos`, and change the content of the logos group.
  - It is important the logos group still exists, and contains the logo.
  - The logo might already be in the `no_orginazations_yet` directory. Look there first.
- Add the organization to `company/organizations.json`.
  - As `id`, use the next free id, starting with a `C-`.
- Test the export by running `./export.sh`.
  - Inkscape should be installed for this.

### Study
- Add a new study combination by adding it to `studies/organizations.json`
  - As `id`, use the next free id, starting with an `S-`.
- Add a new study by getting an svg icon from [materialdesignicons.com](https://materialdesignicons.com)
  - Put it in `studies/logos`.
  - Add the study to `studies/organizations.json`.
- Test the export by running `./export.sh`.
  - Inkscape should be installed for this, as well as the Python module `svgutils`.

### Other
- Add a other logo by duplicating one of the existing logos in `others/logos`, and change the content of the logos group.
  - It is important the logos group still exists, and contains the logo.
- Add the organization to `others/organizations.json`.
  - As `id`, use the next free id, starting with a `O-`.
- Test the export by running `./export.sh`.
  - Inkscape should be installed for this.

## List of logos

### Legend

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
    s = f"| <img src=\"./studies/logos/{o['studies'][0]}.svg\" width=\"16\" height=\"16\" style=\"background-color: white;\"> "

    if len(o["studies"]) >= 2:
        s += f"| <img src=\"./studies/logos/{o['studies'][1]}.svg\" width=\"16\" height=\"16\" style=\"background-color: white;\"> "
    else:
        s += f"|   "

    if len(o["studies"]) >= 3:
        s += f"| <img src=\"./studies/logos/{o['studies'][2]}.svg\" width=\"16\" height=\"16\" style=\"background-color: white;\"> "
    else:
        s += f"|   "

    if len(o["studies"]) >= 4:
        s += f"| <img src=\"./studies/logos/{o['studies'][3]}.svg\" width=\"16\" height=\"16\" style=\"background-color: white;\"> "
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
