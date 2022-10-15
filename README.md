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
| :heavy_check_mark: | Verified |

### Universities

| Logo | ICPC ID | Name | Status |
|---|---|---|---|
| <img src="./universities/logos/U-1.svg" width="32" height="32"> | U-1 |  Lappeenranta University of Technology | :heavy_check_mark: |
| <img src="./universities/logos/U-16.svg" width="32" height="32"> | U-16 |  Aarhus University | :heavy_check_mark: |
| <img src="./universities/logos/U-471.svg" width="32" height="32"> | U-471 |  Bonn University | :heavy_check_mark: |
| <img src="./universities/logos/U-635.svg" width="32" height="32"> | U-635 |  Delft University of Technology | :heavy_check_mark: |
| <img src="./universities/logos/U-676.svg" width="32" height="32"> | U-676 |  Dublin City University | :heavy_check_mark: |
| <img src="./universities/logos/U-711.svg" width="32" height="32"> | U-711 |  Eindhoven University of Technology | :heavy_check_mark: |
| <img src="./universities/logos/U-798.svg" width="32" height="32"> | U-798 |  Friedrich-Alexander-University Erlangen-Nuremberg | :heavy_check_mark: |
| <img src="./universities/logos/U-998.svg" width="32" height="32"> | U-998 |  Jacobs University | :heavy_check_mark: |
| <img src="./universities/logos/U-1133.svg" width="32" height="32"> | U-1133 |  KTH - Royal Institute of Technology | :heavy_check_mark: |
| <img src="./universities/logos/U-1172.svg" width="32" height="32"> | U-1172 |  Leiden University | :heavy_check_mark: |
| <img src="./universities/logos/U-1180.svg" width="32" height="32"> | U-1180 |  Linköping University | :heavy_check_mark: |
| <img src="./universities/logos/U-1192.svg" width="32" height="32"> | U-1192 |  Lund University | :heavy_check_mark: |
| <img src="./universities/logos/U-1227.svg" width="32" height="32"> | U-1227 |  Universität zu Lübeck | :heavy_check_mark: |
| <img src="./universities/logos/U-1393.svg" width="32" height="32"> | U-1393 |  Norwegian University of Science and Technology | :heavy_check_mark: |
| <img src="./universities/logos/U-1833.svg" width="32" height="32"> | U-1833 |  Technische Universität München | :heavy_check_mark: |
| <img src="./universities/logos/U-1936.svg" width="32" height="32"> | U-1936 |  Umeå University | :heavy_check_mark: |
| <img src="./universities/logos/U-2086.svg" width="32" height="32"> | U-2086 |  Karlsruhe Institute of Technology | :heavy_check_mark: |
| <img src="./universities/logos/U-2088.svg" width="32" height="32"> | U-2088 |  Universität Rostock | :heavy_check_mark: |
| <img src="./universities/logos/U-2096.svg" width="32" height="32"> | U-2096 |  Universiteit Utrecht | :heavy_check_mark: |
| <img src="./universities/logos/U-2134.svg" width="32" height="32"> | U-2134 |  University of Cambridge | :heavy_check_mark: |
| <img src="./universities/logos/U-2145.svg" width="32" height="32"> | U-2145 |  University of Copenhagen | :heavy_check_mark: |
| <img src="./universities/logos/U-2233.svg" width="32" height="32"> | U-2233 |  University of Oslo | :heavy_check_mark: |
| <img src="./universities/logos/U-2307.svg" width="32" height="32"> | U-2307 |  University of Twente | :heavy_check_mark: |
| <img src="./universities/logos/U-2338.svg" width="32" height="32"> | U-2338 |  Uppsala University | :heavy_check_mark: |
| <img src="./universities/logos/U-2381.svg" width="32" height="32"> | U-2381 |  Vrije Universiteit | :heavy_check_mark: |
| <img src="./universities/logos/U-2986.svg" width="32" height="32"> | U-2986 |  University of Helsinki | :heavy_check_mark: |
| <img src="./universities/logos/U-3052.svg" width="32" height="32"> | U-3052 |  Reykjavik University | :heavy_check_mark: |
| <img src="./universities/logos/U-3088.svg" width="32" height="32"> | U-3088 |  Avans Hogeschool's - Hertogenbosch | :heavy_check_mark: |
| <img src="./universities/logos/U-3179.svg" width="32" height="32"> | U-3179 |  Katholieke Universiteit Leuven | :heavy_check_mark: |
| <img src="./universities/logos/U-3264.svg" width="32" height="32"> | U-3264 |  University of Oxford | :heavy_check_mark: |
| <img src="./universities/logos/U-3316.svg" width="32" height="32"> | U-3316 |  Imperial College London | :heavy_check_mark: |
| <img src="./universities/logos/U-3317.svg" width="32" height="32"> | U-3317 |  University College Dublin | :heavy_check_mark: |
| <img src="./universities/logos/U-3386.svg" width="32" height="32"> | U-3386 |  University of Nottingham | :heavy_check_mark: |
| <img src="./universities/logos/U-4257.svg" width="32" height="32"> | U-4257 |  Johannes Gutenberg Universität Mainz | :heavy_check_mark: |
| <img src="./universities/logos/U-5077.svg" width="32" height="32"> | U-5077 |  University of Bath | :heavy_check_mark: |
| <img src="./universities/logos/U-5267.svg" width="32" height="32"> | U-5267 |  University of Manchester | :heavy_check_mark: |
| <img src="./universities/logos/U-5313.svg" width="32" height="32"> | U-5313 |  University of Edinburgh | :heavy_check_mark: |
| <img src="./universities/logos/U-6062.svg" width="32" height="32"> | U-6062 |  University of Liverpool | :heavy_check_mark: |
| <img src="./universities/logos/U-6104.svg" width="32" height="32"> | U-6104 |  University of Southampton | :heavy_check_mark: |
| <img src="./universities/logos/U-6175.svg" width="32" height="32"> | U-6175 |  University of Warwick | :heavy_check_mark: |
| <img src="./universities/logos/U-6253.svg" width="32" height="32"> | U-6253 |  University College London | :heavy_check_mark: |
| <img src="./universities/logos/U-7250.svg" width="32" height="32"> | U-7250 |  Radboud University | :heavy_check_mark: |
| <img src="./universities/logos/U-18628.svg" width="32" height="32"> | U-18628 |  Frankfurt am Main University of Applied Sciences | :heavy_check_mark: |
| <img src="./universities/logos/U-18717.svg" width="32" height="32"> | U-18717 |  Universitaet des Saarlandes | :heavy_check_mark: |
| <img src="./universities/logos/U-18720.svg" width="32" height="32"> | U-18720 |  University of Bergen | :heavy_check_mark: |
| <img src="./universities/logos/U-19555.svg" width="32" height="32"> | U-19555 |  Université Catholique de Louvain | :heavy_check_mark: |

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

### Studies

| Icon 1 | Icon 2 | Icon 3 | ID | Name | Status |
|---|---|---|---|---|---|
| <img src="./studies/logos/CSE.svg" width="16" height="16"> |   |   | S-1 |  Computer Science & Engineering | :heavy_check_mark: |
| <img src="./studies/logos/CSE.svg" width="16" height="16"> | <img src="./studies/logos/NB.svg" width="16" height="16"> |   | S-2 |  Computer Science & Engineering + Nanobiology | :heavy_check_mark: |
| <img src="./studies/logos/CSE.svg" width="16" height="16"> | <img src="./studies/logos/TW.svg" width="16" height="16"> |   | S-3 |  Computer Science & Engineering + Applied Mathematics | :heavy_check_mark: |
| <img src="./studies/logos/TW.svg" width="16" height="16"> |   |   | S-4 |  Applied Mathematics | :heavy_check_mark: |
| <img src="./studies/logos/TW.svg" width="16" height="16"> | <img src="./studies/logos/WB.svg" width="16" height="16"> | <img src="./studies/logos/AE.svg" width="16" height="16"> | S-5 |  Applied Mathematics + Mechanical Engineering + Aerospace Engineering | :heavy_check_mark: |
| <img src="./studies/logos/EE.svg" width="16" height="16"> |   |   | S-6 |  Electrical Engineering | :heavy_check_mark: |