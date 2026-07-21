# Census Statistics

A Python automation project that reads a 2010 US Census Excel spreadsheet and calculates population statistics for each county.

This project demonstrates how Python can automate repetitive spreadsheet data processing.

## Project Overview

The original task was to manually analyze thousands of census tract records and calculate:

- The number of census tracts in each county
- The total population of each county

Instead of manually processing thousands of rows, this Python script automatically reads the spreadsheet and generates the statistics in seconds.

## Features

- Reads Excel files using `openpyxl`
- Processes thousands of spreadsheet rows automatically
- Groups data by:
  - State
  - County
- Calculates:
  - Census tract counts
  - County population totals
- Generates a reusable Python data file using `pprint`

## Technologies Used

- Python 3
- openpyxl
- pprint

## Project Files

```
census-statistics/
│
├── readCensusExcel.py       # Main script that processes the census spreadsheet
├── censuspopdata.xlsx       # Source census data spreadsheet
├── census2010.py            # Generated file containing processed census data
└── README.md                # Project documentation
```

## How It Works

The program:

1. Opens the census Excel workbook.

2. Reads the worksheet:

```
Population by Census Tract
```

3. Loops through every census tract row.

4. Builds a nested dictionary:

```python
county_data[state][county]["tracts"]
county_data[state][county]["pop"]
```

Example:

```python
{
    "AL": {
        "Autauga": {
            "tracts": 12,
            "pop": 54571
        }
    }
}
```

5. Saves the completed dataset into:

```
census2010.py
```

which can later be imported into another Python program.

## Installation

Clone the repository:

```bash
git clone git@github.com:Joshua-2333/census-statistics.git
```

Navigate into the project:

```bash
cd census-statistics
```

Install the required dependency:

```bash
pip install openpyxl
```

## Running the Program

Run:

```bash
python readCensusExcel.py
```

Example output:

```
Opening workbook...
Worksheet: Population by Census Tract
Rows: 72865
Columns: 4
Reading rows...
Processed 72864 census tracts
{'tracts': 12, 'pop': 54571}
Writing results...
Done.
```

## Example Usage

After generating `census2010.py`, the data can be imported:

```python
import census2010

print(census2010.allData["AL"]["Autauga"])
```

Output:

```python
{'tracts': 12, 'pop': 54571}
```

## What I Learned

Through this project I practiced:

- Reading and processing Excel spreadsheets with Python
- Working with nested dictionaries
- Automating repetitive data analysis tasks
- Using Python scripts to generate reusable data files
- Handling large datasets efficiently

## Future Improvements

Possible improvements:

- Export results to CSV or Excel
- Create a command-line interface
- Add search functionality for counties
- Generate charts and visualizations from the census data
