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

### Universities

| Logo | ICPC ID | Name | Status |
|---|---|---|---|
| <img src="./universities/logos/7.svg" width="32" height="32"> | 7 |  Aarhus University | :heavy_check_mark: |
| <img src="./universities/logos/33.svg" width="32" height="32"> | 33 |  Ulm University | :heavy_check_mark: |
| <img src="./universities/logos/131.svg" width="32" height="32"> | 131 |  Jagiellonian University in Krakow | :heavy_check_mark: |
| <img src="./universities/logos/175.svg" width="32" height="32"> | 175 |  Bonn University | :heavy_check_mark: |
| <img src="./universities/logos/290.svg" width="32" height="32"> | 290 |  Christian-Albrechts-Universitaet zu Kiel | :heavy_check_mark: |
| <img src="./universities/logos/362.svg" width="32" height="32"> | 362 |  Darmstadt University of Technology | :heavy_check_mark: |
| <img src="./universities/logos/367.svg" width="32" height="32"> | 367 |  Delft University of Technology | :heavy_check_mark: |
| <img src="./universities/logos/452.svg" width="32" height="32"> | 452 |  Eindhoven University of Technology | :heavy_check_mark: |
| <img src="./universities/logos/573.svg" width="32" height="32"> | 573 |  Friedrich-Alexander-University Erlangen-Nuremberg | :heavy_check_mark: |
| <img src="./universities/logos/980.svg" width="32" height="32"> | 980 |  Kaunas University of Technology | :heavy_check_mark: |
| <img src="./universities/logos/1039.svg" width="32" height="32"> | 1039 |  KTH - Royal Institute of Technology | :heavy_check_mark: |
| <img src="./universities/logos/1088.svg" width="32" height="32"> | 1088 |  Leiden University | :heavy_check_mark: |
| <img src="./universities/logos/1097.svg" width="32" height="32"> | 1097 |  Linköping University | :heavy_check_mark: |
| <img src="./universities/logos/1112.svg" width="32" height="32"> | 1112 |  Lund University | :heavy_check_mark: |
| <img src="./universities/logos/1154.svg" width="32" height="32"> | 1154 |  Universität zu Lübeck | :heavy_check_mark: |
| <img src="./universities/logos/1362.svg" width="32" height="32"> | 1362 |  Norwegian University of Science and Technology | :heavy_check_mark: |
| <img src="./universities/logos/1534.svg" width="32" height="32"> | 1534 |  Rijksuniversiteit Groningen | :heavy_check_mark: |
| <img src="./universities/logos/1917.svg" width="32" height="32"> | 1917 |  Technische Universität München | :heavy_check_mark: |
| <img src="./universities/logos/2061.svg" width="32" height="32"> | 2061 |  Umeå University | :heavy_check_mark: |
| <img src="./universities/logos/2267.svg" width="32" height="32"> | 2267 |  Saarland University | :heavy_check_mark: |
| <img src="./universities/logos/2272.svg" width="32" height="32"> | 2272 |  Karlsruhe Institute of Technology | :heavy_check_mark: |
| <img src="./universities/logos/2274.svg" width="32" height="32"> | 2274 |  Universität Rostock | :heavy_check_mark: |
| <img src="./universities/logos/2275.svg" width="32" height="32"> | 2275 |  Universität Ulm | :heavy_check_mark: |
| <img src="./universities/logos/2282.svg" width="32" height="32"> | 2282 |  Leiden University | :heavy_check_mark: |
| <img src="./universities/logos/2284.svg" width="32" height="32"> | 2284 |  Universiteit van Amsterdam | :heavy_check_mark: |
| <img src="./universities/logos/2292.svg" width="32" height="32"> | 2292 |  University College Cork | :heavy_check_mark: |
| <img src="./universities/logos/2320.svg" width="32" height="32"> | 2320 |  University of Bergen | :heavy_check_mark: |
| <img src="./universities/logos/2343.svg" width="32" height="32"> | 2343 |  University of Cambridge | :heavy_check_mark: |
| <img src="./universities/logos/2357.svg" width="32" height="32"> | 2357 |  University of Copenhagen | :heavy_check_mark: |
| <img src="./universities/logos/2467.svg" width="32" height="32"> | 2467 |  University of Oslo | :heavy_check_mark: |
| <img src="./universities/logos/2523.svg" width="32" height="32"> | 2523 |  University of Sussex | :heavy_check_mark: |
| <img src="./universities/logos/2526.svg" width="32" height="32"> | 2526 |  University of Tartu | :heavy_check_mark: |
| <img src="./universities/logos/2561.svg" width="32" height="32"> | 2561 |  University of Twente | :heavy_check_mark: |
| <img src="./universities/logos/2625.svg" width="32" height="32"> | 2625 |  Utrecht University | :heavy_check_mark: |
| <img src="./universities/logos/2643.svg" width="32" height="32"> | 2643 |  Vilnius University | :heavy_check_mark: |
| <img src="./universities/logos/2664.svg" width="32" height="32"> | 2664 |  Vrije Universiteit | :heavy_check_mark: |
| <img src="./universities/logos/3330.svg" width="32" height="32"> | 3330 |  University of Helsinki | :heavy_check_mark: |
| <img src="./universities/logos/3397.svg" width="32" height="32"> | 3397 |  Chalmers University of Technology | :heavy_check_mark: |
| <img src="./universities/logos/3403.svg" width="32" height="32"> | 3403 |  Reykjavik University | :heavy_check_mark: |
| <img src="./universities/logos/3546.svg" width="32" height="32"> | 3546 |  Ghent University | :heavy_check_mark: |
| <img src="./universities/logos/3620.svg" width="32" height="32"> | 3620 |  University of Oxford | :heavy_check_mark: |
| <img src="./universities/logos/3678.svg" width="32" height="32"> | 3678 |  Imperial College London | :heavy_check_mark: |
| <img src="./universities/logos/3749.svg" width="32" height="32"> | 3749 |  University of Nottingham | :heavy_check_mark: |
| <img src="./universities/logos/3758.svg" width="32" height="32"> | 3758 |  King's College London | :heavy_check_mark: |
| <img src="./universities/logos/3787.svg" width="32" height="32"> | 3787 |  RWTH Aachen University | :heavy_check_mark: |
| <img src="./universities/logos/4278.svg" width="32" height="32"> | 4278 |  Technical University of Denmark | :heavy_check_mark: |
| <img src="./universities/logos/4711.svg" width="32" height="32"> | 4711 |  Johannes Gutenberg Universität Mainz | :heavy_check_mark: |
| <img src="./universities/logos/4786.svg" width="32" height="32"> | 4786 |  Aalto University | :heavy_check_mark: |
| <img src="./universities/logos/5541.svg" width="32" height="32"> | 5541 |  University of Bath | :heavy_check_mark: |
| <img src="./universities/logos/5737.svg" width="32" height="32"> | 5737 |  University of Manchester | :heavy_check_mark: |
| <img src="./universities/logos/5784.svg" width="32" height="32"> | 5784 |  University of Edinburgh | :heavy_check_mark: |
| <img src="./universities/logos/6026.svg" width="32" height="32"> | 6026 |  Molde University College | :heavy_check_mark: |
| <img src="./universities/logos/6557.svg" width="32" height="32"> | 6557 |  Frankfurt University of Applied Sciences | :heavy_check_mark: |
| <img src="./universities/logos/6817.svg" width="32" height="32"> | 6817 |  University of Liverpool | :heavy_check_mark: |
| <img src="./universities/logos/6638.svg" width="32" height="32"> | 6638 |  German University of Technology in Oman | :heavy_check_mark: |
| <img src="./universities/logos/6859.svg" width="32" height="32"> | 6859 |  University of Southampton | :heavy_check_mark: |
| <img src="./universities/logos/6864.svg" width="32" height="32"> | 6864 |  IT University of Copenhagen | :heavy_check_mark: |
| <img src="./universities/logos/6929.svg" width="32" height="32"> | 6929 |  University of Warwick | :heavy_check_mark: |
| <img src="./universities/logos/6940.svg" width="32" height="32"> | 6940 |  University of Glasgow | :heavy_check_mark: |
| <img src="./universities/logos/7006.svg" width="32" height="32"> | 7006 |  University College London | :heavy_check_mark: |
| <img src="./universities/logos/7019.svg" width="32" height="32"> | 7019 |  Hogeschool Leiden | :heavy_check_mark: |
| <img src="./universities/logos/7264.svg" width="32" height="32"> | 7264 |  University of Göttingen | :heavy_check_mark: |
| <img src="./universities/logos/7431.svg" width="32" height="32"> | 7431 |  Aalborg University | :heavy_check_mark: |
| <img src="./universities/logos/7464.svg" width="32" height="32"> | 7464 |  Brunel University London | :heavy_check_mark: |
| <img src="./universities/logos/7477.svg" width="32" height="32"> | 7477 |  Vilnius Gediminas Technical University | :heavy_check_mark: |
| <img src="./universities/logos/7488.svg" width="32" height="32"> | 7488 |  Maynooth University | :heavy_check_mark: |
| <img src="./universities/logos/7887.svg" width="32" height="32"> | 7887 |  University of Iceland | :heavy_check_mark: |
| <img src="./universities/logos/7918.svg" width="32" height="32"> | 7918 |  University of St Andrews | :heavy_check_mark: |
| <img src="./universities/logos/7950.svg" width="32" height="32"> | 7950 |  University of Birmingham | :heavy_check_mark: |
| <img src="./universities/logos/8002.svg" width="32" height="32"> | 8002 |  Radboud University | :heavy_check_mark: |
| <img src="./universities/logos/8102.svg" width="32" height="32"> | 8102 |  University of Passau | :heavy_check_mark: |
| <img src="./universities/logos/8170.svg" width="32" height="32"> | 8170 |  Hasso Plattner Institute | :heavy_check_mark: |
| <img src="./universities/logos/8311.svg" width="32" height="32"> | 8311 |  Université de Mons | :heavy_check_mark: |
| <img src="./universities/logos/8317.svg" width="32" height="32"> | 8317 |  University of Bristol | :heavy_check_mark: |
| <img src="./universities/logos/9858.svg" width="32" height="32"> | 9858 |  Université Catholique de Louvain | :heavy_check_mark: |
| <img src="./universities/logos/10500.svg" width="32" height="32"> | 10500 |  Maastricht University | :heavy_check_mark: |
| <img src="./universities/logos/11054.svg" width="32" height="32"> | 11054 |  Tallinn University of Technology | :heavy_check_mark: |
| <img src="./universities/logos/11103.svg" width="32" height="32"> | 11103 |  KU Leuven | :heavy_check_mark: |
| <img src="./universities/logos/11352.svg" width="32" height="32"> | 11352 |  Ruhr University Bochum | :heavy_check_mark: |
| <img src="./universities/logos/13859.svg" width="32" height="32"> | 13859 |  University of Luxembourg | :heavy_check_mark: |
| <img src="./universities/logos/14148.svg" width="32" height="32"> | 14148 |  University of Leeds | :heavy_check_mark: |
| <img src="./universities/logos/14277.svg" width="32" height="32"> | 14277 |  Hochschule für angewandte Wissenschaften Würzburg-Schweinfurt | :heavy_check_mark: |
| <img src="./universities/logos/18106.svg" width="32" height="32"> | 18106 |  Jacobs University in Bremen | :heavy_check_mark: |
| <img src="./universities/logos/18633.svg" width="32" height="32"> | 18633 |  University of Augsburg | :heavy_check_mark: |
| <img src="./universities/logos/20052.svg" width="32" height="32"> | 20052 |  Heinrich-Heine-Universität Düsseldorf | :heavy_check_mark: |
| <img src="./universities/logos/21966.svg" width="32" height="32"> | 21966 |  Anglia Ruskin University | :heavy_check_mark: |
| <img src="./universities/logos/21967.svg" width="32" height="32"> | 21967 |  Constructor University Bremen | :heavy_check_mark: |
| <img src="./universities/logos/23885.svg" width="32" height="32"> | 23885 |  Jönköping University | :heavy_check_mark: |
| <img src="./universities/logos/26092.svg" width="32" height="32"> | 26092 |  Liverpool Hope University | :heavy_check_mark: |

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
| <img src="./companies/logos/C-25.svg" width="32" height="32"> | C-25 |  Jump Trading | :heavy_check_mark: |

### Studies

| Icon 1 | Icon 2 | Icon 3 | Icon 4 | ID | Name | Status |
|---|---|---|---|---|---|---|
| <img src="./studies/logos/CSE.svg" width="16" height="16"> |   |   |   | S-1 |  Computer Science & Engineering | :heavy_check_mark: |
| <img src="./studies/logos/CSE.svg" width="16" height="16"> | <img src="./studies/logos/NB.svg" width="16" height="16"> |   |   | S-2 |  Computer Science & Eng. + Nanobiology | :heavy_check_mark: |
| <img src="./studies/logos/CSE.svg" width="16" height="16"> | <img src="./studies/logos/AM.svg" width="16" height="16"> |   |   | S-3 |  Computer Science & Eng. + A. Mathematics | :heavy_check_mark: |
| <img src="./studies/logos/AM.svg" width="16" height="16"> |   |   |   | S-4 |  Applied Mathematics | :heavy_check_mark: |
| <img src="./studies/logos/AM.svg" width="16" height="16"> | <img src="./studies/logos/ME.svg" width="16" height="16"> | <img src="./studies/logos/AE.svg" width="16" height="16"> |   | S-5 |  A. Mathematics + Mechanical Eng. + Aerospace Eng. | :heavy_check_mark: |
| <img src="./studies/logos/EE.svg" width="16" height="16"> |   |   |   | S-6 |  Electrical Engineering | :heavy_check_mark: |
| <img src="./studies/logos/NB.svg" width="16" height="16"> |   |   |   | S-7 |  Nanobiology | :heavy_check_mark: |
| <img src="./studies/logos/CSE.svg" width="16" height="16"> | <img src="./studies/logos/AE.svg" width="16" height="16"> |   |   | S-8 |  Computer Science & Eng. + Aerospace Eng. | :heavy_check_mark: |
| <img src="./studies/logos/CSE.svg" width="16" height="16"> | <img src="./studies/logos/AM.svg" width="16" height="16"> | <img src="./studies/logos/AP.svg" width="16" height="16"> | <img src="./studies/logos/AE.svg" width="16" height="16"> | S-9 |  CSE + A. Mathematics + A. Physics + Aerospace Eng. | :heavy_check_mark: |
| <img src="./studies/logos/CSE.svg" width="16" height="16"> | <img src="./studies/logos/AM.svg" width="16" height="16"> | <img src="./studies/logos/AP.svg" width="16" height="16"> |   | S-10 |  CSE + A. Mathematics + A. Physics | :heavy_check_mark: |

### Others

| Logo | ID | Name | Status |
|---|---|---|---|
| <img src="./others/logos/O-1.svg" width="32" height="32"> | O-1 |  OBJECTION! | :heavy_check_mark: |
| <img src="./others/logos/O-2.svg" width="32" height="32"> | O-2 |  The Wise Owl | :heavy_check_mark: |
| <img src="./others/logos/O-3.svg" width="32" height="32"> | O-3 |  Elektrichiens Vakbond | :heavy_check_mark: |
