# EchoPainting

Convert pixel art Excel templates into ECHO liquid handler worklists for creating art on microwell plates.

## Overview

EchoPainting takes an Excel spreadsheet containing pixel art (with numeric color codes) and generates a CSV worklist file for the ECHO liquid handler. The tool maps colors from a 6-well source plate to a 1536-well destination plate.

## Features

- Simple drag-and-drop GUI interface
- Converts .xlsx pixel art templates to ECHO-compatible CSV files
- Supports 6 colors mapped to a 6-well source plate (A1-B3)
- Outputs to 1536-well destination plate (32 rows × 48 columns)
- Transfer volume: 250 µL per well

## Installation

1. **Clone this repository**
   ```bash
   git clone https://github.com/ljm176/EchoPainting.git
   cd EchoPainting
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the application**
   ```bash
   python make_paint_csv.py
   ```

2. **Create your worklist**
   - Drag and drop your .xlsx pixel art template into the window
   - Choose where to save the output CSV file
   - The file will be saved with "_ECHO.csv" appended to the original filename

## Excel Template Format

- Maximum template size: 32 rows × 48 columns
- Use numeric codes (1-6) to represent different colors:
  - 1 → Source well A1
  - 2 → Source well A2
  - 3 → Source well A3
  - 4 → Source well B1
  - 5 → Source well B2
  - 6 → Source well B3
- Empty cells are skipped (no transfer)
- Template is read column-by-column from left to right

## Source Plate Setup (6-well plate)

```
   1    2    3
A  1    2    3
B  4    5    6
```

Load your paint/dye colors into these wells before running the ECHO protocol.

## Output Format

The generated CSV contains three columns:
- **Source Well**: Well position in the 6-well source plate
- **Destination Well**: Well position in the 1536-well destination plate
- **Transfer Volume**: Volume to transfer (250 µL)

## Requirements

- Python 3.7+
- openpyxl
- tkinterdnd2

## Troubleshooting

- **Drag-and-drop not working**: Ensure `tkinterdnd2` is properly installed
- **Offset/misaligned output**: Make sure your Excel template doesn't exceed 32 rows
- **Missing transfers**: Verify your Excel cells contain numeric values 1-6 
