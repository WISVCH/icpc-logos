# icpc-logos

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
  - Inkscape should be installed for this.

## List of logos

### Legend

| Status | description |
|---|---|
| :x: | Missing |
| :question: | Present, but needs verification |
| :heavy_check_mark: | Verified

### Universities

| Logo | ICPC ID | Name | Status             |
|---|---|---|--------------------|
| <img src="./universities/logos/U-7.svg" width="32" height="32"> | U-7 |  Aarhus University | :heavy_check_mark: |
| <img src="./universities/logos/U-290.svg" width="32" height="32"> | U-290 |  Christian-Albrechts-Universitaet zu Kiel | :heavy_check_mark: |
| <img src="./universities/logos/U-362.svg" width="32" height="32"> | U-362 |  Darmstadt University of Technology | :heavy_check_mark: |
| <img src="./universities/logos/U-367.svg" width="32" height="32"> | U-367 |  Delft University of Technology | :heavy_check_mark: |
| <img src="./universities/logos/U-452.svg" width="32" height="32"> | U-452 |  Eindhoven University of Technology | :heavy_check_mark: |
| <img src="./universities/logos/U-573.svg" width="32" height="32"> | U-573 |  Friedrich-Alexander-University Erlangen-Nuremberg | :heavy_check_mark: |
| <img src="./universities/logos/U-980.svg" width="32" height="32"> | U-980 |  Kaunas University of Technology | :heavy_check_mark: |
| <img src="./universities/logos/U-1039.svg" width="32" height="32"> | U-1039 |  KTH - Royal Institute of Technology | :heavy_check_mark: |
| <img src="./universities/logos/U-1088.svg" width="32" height="32"> | U-1088 |  Leiden University | :heavy_check_mark: |
| <img src="./universities/logos/U-1097.svg" width="32" height="32"> | U-1097 |  Linköping University | :heavy_check_mark: |
| <img src="./universities/logos/U-1112.svg" width="32" height="32"> | U-1112 |  Lund University | :heavy_check_mark: |
| <img src="./universities/logos/U-1154.svg" width="32" height="32"> | U-1154 |  Universität zu Lübeck | :heavy_check_mark: |
| <img src="./universities/logos/U-1362.svg" width="32" height="32"> | U-1362 |  Norwegian University of Science and Technology | :heavy_check_mark: |
| <img src="./universities/logos/U-1534.svg" width="32" height="32"> | U-1534 |  Rijksuniversiteit Groningen | :heavy_check_mark: |
| <img src="./universities/logos/U-1917.svg" width="32" height="32"> | U-1917 |  Technische Universität München | :heavy_check_mark: |
| <img src="./universities/logos/U-2061.svg" width="32" height="32"> | U-2061 |  Umeå University | :heavy_check_mark: |
| <img src="./universities/logos/U-2267.svg" width="32" height="32"> | U-2267 |  Saarland University | :heavy_check_mark: |
| <img src="./universities/logos/U-2272.svg" width="32" height="32"> | U-2272 |  Karlsruhe Institute of Technology | :heavy_check_mark: |
| <img src="./universities/logos/U-2274.svg" width="32" height="32"> | U-2274 |  Universität Rostock | :heavy_check_mark: |
| <img src="./universities/logos/U-2275.svg" width="32" height="32"> | U-2275 |  Universität Ulm | :heavy_check_mark: |
| <img src="./universities/logos/U-2284.svg" width="32" height="32"> | U-2284 |  Universiteit van Amsterdam | :heavy_check_mark: |
| <img src="./universities/logos/U-2320.svg" width="32" height="32"> | U-2320 |  University of Bergen | :heavy_check_mark: |
| <img src="./universities/logos/U-2343.svg" width="32" height="32"> | U-2343 |  University of Cambridge | :heavy_check_mark: |
| <img src="./universities/logos/U-2357.svg" width="32" height="32"> | U-2357 |  University of Copenhagen | :heavy_check_mark: |
| <img src="./universities/logos/U-2467.svg" width="32" height="32"> | U-2467 |  University of Oslo | :heavy_check_mark: |
| <img src="./universities/logos/U-2526.svg" width="32" height="32"> | U-2526 |  University of Tartu | :heavy_check_mark: |
| <img src="./universities/logos/U-2625.svg" width="32" height="32"> | U-2625 |  Utrecht University | :heavy_check_mark: |
| <img src="./universities/logos/U-2643.svg" width="32" height="32"> | U-2643 |  Vilnius University | :heavy_check_mark: |
| <img src="./universities/logos/U-2664.svg" width="32" height="32"> | U-2664 |  Vrije Universiteit | :heavy_check_mark: |
| <img src="./universities/logos/U-3330.svg" width="32" height="32"> | U-3330 |  University of Helsinki | :heavy_check_mark: |
| <img src="./universities/logos/U-3397.svg" width="32" height="32"> | U-3397 |  Chalmers University of Technology | :heavy_check_mark: |
| <img src="./universities/logos/U-3403.svg" width="32" height="32"> | U-3403 |  Reykjavik University | :heavy_check_mark: |
| <img src="./universities/logos/U-3546.svg" width="32" height="32"> | U-3546 |  Ghent University | :heavy_check_mark: |
| <img src="./universities/logos/U-3620.svg" width="32" height="32"> | U-3620 |  University of Oxford | :heavy_check_mark: |
| <img src="./universities/logos/U-3678.svg" width="32" height="32"> | U-3678 |  Imperial College London | :heavy_check_mark: |
| <img src="./universities/logos/U-3749.svg" width="32" height="32"> | U-3749 |  University of Nottingham | :heavy_check_mark: |
| <img src="./universities/logos/U-3758.svg" width="32" height="32"> | U-3758 |  King's College London | :heavy_check_mark: |
| <img src="./universities/logos/U-3787.svg" width="32" height="32"> | U-3787 |  RWTH Aachen University | :heavy_check_mark: |
| <img src="./universities/logos/U-4278.svg" width="32" height="32"> | U-4278 |  Technical University of Denmark | :heavy_check_mark: |
| <img src="./universities/logos/U-4786.svg" width="32" height="32"> | U-4786 |  Aalto University | :heavy_check_mark: |
| <img src="./universities/logos/U-5541.svg" width="32" height="32"> | U-5541 |  University of Bath | :heavy_check_mark: |
| <img src="./universities/logos/U-5737.svg" width="32" height="32"> | U-5737 |  University of Manchester | :heavy_check_mark: |
| <img src="./universities/logos/U-5784.svg" width="32" height="32"> | U-5784 |  University of Edinburgh | :heavy_check_mark: |
| <img src="./universities/logos/U-6026.svg" width="32" height="32"> | U-6026 |  Molde University College | :heavy_check_mark: |
| <img src="./universities/logos/U-6557.svg" width="32" height="32"> | U-6557 |  Frankfurt University of Applied Sciences | :heavy_check_mark: |
| <img src="./universities/logos/U-6638.svg" width="32" height="32"> | U-6638 |  German University of Technology in Oman | :heavy_check_mark: |
| <img src="./universities/logos/U-6859.svg" width="32" height="32"> | U-6859 |  University of Southampton | :heavy_check_mark: |
| <img src="./universities/logos/U-6864.svg" width="32" height="32"> | U-6864 |  IT University of Copenhagen | :heavy_check_mark: |
| <img src="./universities/logos/U-6929.svg" width="32" height="32"> | U-6929 |  University of Warwick | :heavy_check_mark: |
| <img src="./universities/logos/U-6940.svg" width="32" height="32"> | U-6940 |  University of Glasgow | :heavy_check_mark: |
| <img src="./universities/logos/U-7019.svg" width="32" height="32"> | U-7019 |  Hogeschool Leiden | :heavy_check_mark: |
| <img src="./universities/logos/U-7264.svg" width="32" height="32"> | U-7264 |  University of Göttingen | :heavy_check_mark: |
| <img src="./universities/logos/U-7464.svg" width="32" height="32"> | U-7464 |  Brunel University London | :heavy_check_mark: |
| <img src="./universities/logos/U-7477.svg" width="32" height="32"> | U-7477 |  Vilnius Gediminas Technical University | :heavy_check_mark: |
| <img src="./universities/logos/U-7887.svg" width="32" height="32"> | U-7887 |  University of Iceland | :heavy_check_mark: |
| <img src="./universities/logos/U-7950.svg" width="32" height="32"> | U-7950 |  University of Birmingham | :heavy_check_mark: |
| <img src="./universities/logos/U-8002.svg" width="32" height="32"> | U-8002 |  Radboud University | :heavy_check_mark: |
| <img src="./universities/logos/U-8102.svg" width="32" height="32"> | U-8102 |  University of Passau | :heavy_check_mark: |
| <img src="./universities/logos/U-8170.svg" width="32" height="32"> | U-8170 |  Hasso Plattner Institute | :heavy_check_mark: |
| <img src="./universities/logos/U-8311.svg" width="32" height="32"> | U-8311 |  Université de Mons | :heavy_check_mark: |
| <img src="./universities/logos/U-8317.svg" width="32" height="32"> | U-8317 |  University of Bristol | :heavy_check_mark: |
| <img src="./universities/logos/U-9858.svg" width="32" height="32"> | U-9858 |  Université Catholique de Louvain | :heavy_check_mark: |
| <img src="./universities/logos/U-11054.svg" width="32" height="32"> | U-11054 |  Tallinn University of Technology | :heavy_check_mark: |
| <img src="./universities/logos/U-13859.svg" width="32" height="32"> | U-13859 |  University of Luxembourg | :heavy_check_mark: |
| <img src="./universities/logos/U-14277.svg" width="32" height="32"> | U-14277 |  Hochschule für angewandte Wissenschaften Würzburg-Schweinfurt | :heavy_check_mark: |
| <img src="./universities/logos/U-18106.svg" width="32" height="32"> | U-18106 |  Jacobs University in Bremen | :heavy_check_mark: |
| <img src="./universities/logos/U-18633.svg" width="32" height="32"> | U-18633 |  University of Augsburg | :heavy_check_mark: |
| <img src="./universities/logos/U-20052.svg" width="32" height="32"> | U-20052 |  Heinrich-Heine-Universität Düsseldorf | :heavy_check_mark:                |

### Companies

| Logo | ID | Name | Status |
|---|---|---|---|
| <img src="./companies/logos/C-2.svg" width="32" height="32"> | C-2 |  ASML | :heavy_check_mark: |
| <img src="./companies/logos/C-3.svg" width="32" height="32"> | C-3 |  BetterBe B.V. | :heavy_check_mark: |
| <img src="./companies/logos/C-4.svg" width="32" height="32"> | C-4 |  Booking.com | :heavy_check_mark: |
| <img src="./companies/logos/C-5.svg" width="32" height="32"> | C-5 |  Centrum Wiskunde & Informatica | :heavy_check_mark: |
| <img src="./companies/logos/C-6.svg" width="32" height="32"> | C-6 |  Dassault Systèmes | :heavy_check_mark: |
| <img src="./companies/logos/C-7.svg" width="32" height="32"> | C-7 |  IMC Trading B.V. | :heavy_check_mark: |
| <img src="./companies/logos/C-8.svg" width="32" height="32"> | C-8 |  Ortec International B.V. | :heavy_check_mark: |
| <img src="./companies/logos/C-10.svg" width="32" height="32"> | C-10 |  Sioux Technologies B.V. | :heavy_check_mark: |
| <img src="./companies/logos/C-11.svg" width="32" height="32"> | C-11 |  bol.com | :heavy_check_mark: |
| <img src="./companies/logos/C-12.svg" width="32" height="32"> | C-12 |  OrangeMason B.V. | :heavy_check_mark: |
| <img src="./companies/logos/C-13.svg" width="32" height="32"> | C-13 |  Picnic | :heavy_check_mark: |
| <img src="./companies/logos/C-14.svg" width="32" height="32"> | C-14 |  ING | :heavy_check_mark: |
| <img src="./companies/logos/C-15.svg" width="32" height="32"> | C-15 |  Flow Traders | :heavy_check_mark: |
| <img src="./companies/logos/C-16.svg" width="32" height="32"> | C-16 |  Prodrive Technologies | :heavy_check_mark: |
| <img src="./companies/logos/C-17.svg" width="32" height="32"> | C-17 |  Quintiq | :heavy_check_mark: |
| <img src="./companies/logos/C-18.svg" width="32" height="32"> | C-18 |  OVSoftware | :heavy_check_mark: |
| <img src="./companies/logos/C-19.svg" width="32" height="32"> | C-19 |  Jane Street Capital | :heavy_check_mark: |
| <img src="./companies/logos/C-20.svg" width="32" height="32"> | C-20 |  Fox-IT | :heavy_check_mark: |
| <img src="./companies/logos/C-21.svg" width="32" height="32"> | C-21 |  Huawei | :heavy_check_mark: |
| <img src="./companies/logos/C-22.svg" width="32" height="32"> | C-22 |  Netcompany | :heavy_check_mark: |
| <img src="./companies/logos/C-23.svg" width="32" height="32"> | C-23 |  JetBrains | :heavy_check_mark: |
| <img src="./companies/logos/C-24.svg" width="32" height="32"> | C-24 |  International Collegiate Programming Contest | :heavy_check_mark: |

### Studies

| Icon 1 | Icon 2 | Icon 3 | ID | Name | Status |
|---|---|---|---|---|---|
| <img src="./studies/logos/CSE.svg" width="16" height="16"> |   |   | S-1 |  Computer Science & Engineering | :heavy_check_mark: |
| <img src="./studies/logos/CSE.svg" width="16" height="16"> | <img src="./studies/logos/NB.svg" width="16" height="16"> |   | S-2 |  Computer Science & Engineering + Nanobiology | :heavy_check_mark: |
| <img src="./studies/logos/CSE.svg" width="16" height="16"> | <img src="./studies/logos/TW.svg" width="16" height="16"> |   | S-3 |  Computer Science & Engineering + Applied Mathematics | :heavy_check_mark: |
| <img src="./studies/logos/TW.svg" width="16" height="16"> |   |   | S-4 |  Applied Mathematics | :heavy_check_mark: |
| <img src="./studies/logos/TW.svg" width="16" height="16"> | <img src="./studies/logos/WB.svg" width="16" height="16"> | <img src="./studies/logos/AE.svg" width="16" height="16"> | S-5 |  Applied Mathematics + Mechanical Engineering + Aerospace Engineering | :heavy_check_mark: |
| <img src="./studies/logos/EE.svg" width="16" height="16"> |   |   | S-6 |  Electrical Engineering | :heavy_check_mark: |
