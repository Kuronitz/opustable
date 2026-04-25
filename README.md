------------------------------------------------------------------------

# opustable

------------------------------------------------------------------------

**opustable** is a Python command-line tool that converts Bruker OPUS (.0) files into a single CSV table.  
It extracts absorbance spectra from all `.0` files in a folder and combines them into one CSV file with samples as rows and wavenumbers as columns.

## Table of Contents

------------------------------------------------------------------------

- [Installation](#installation)
- [Usage](#usage)
- [Options](#options)
- [Example](#example)
- [Output Format](#output-format)
- [Notes](#notes)

## Installation

------------------------------------------------------------------------

1. Clone the repository:

       git clone https://github.com/Kuronitz/opustable.git

2. Change into the project directory:

       cd opustable

3. Install the required dependencies:

       pip install brukeropus pandas numpy

## Usage

------------------------------------------------------------------------

Run:

    python convert.py -h

The usage is as follows:

    usage: convert.py opus_folder [output_csv]

    Convert Bruker OPUS (.0) files to a single CSV table.

    positional arguments:
      opus_folder    Path to the folder containing .0 files
      output_csv     Optional output CSV file name (default: spectra.csv in the same folder)

## Options

------------------------------------------------------------------------

    -h, --help       Show this help message and exit.

No additional options are required. The script reads all `.0` files from the input folder, extracts the absorbance data (`a` block), and writes a merged CSV.

## Example

------------------------------------------------------------------------

To convert all `.0` files in `./opus_data` and save the result as `spectra.csv`:

    python convert.py ./opus_data spectra.csv

If you omit the output file name:

    python convert.py ./opus_data

The script will create `spectra.csv` inside `./opus_data`.

## Output Format

------------------------------------------------------------------------

The generated CSV has the following structure:

| Sample | 11542 | 11538 | 11534 | ... |
|--------|-------|-------|-------|-----|
| A11    | 0.32125017 | 0.32163080 | 0.32191235 | ... |
| M11    | 0.32126479 | 0.32163347 | 0.32190182 | ... |

- The `Sample` column contains the file name without the `.0` extension.
- Wavenumber columns are rounded to integers and sorted from high to low.
- Absorbance values are preserved with full original precision (no interpolation or smoothing).

## Notes

------------------------------------------------------------------------

- The script assumes all `.0` files share the same wavenumber axis (typical for measurements from the same instrument with identical settings).
- Only the `a` (absorbance) block is used. For other blocks (e.g., `sm`, `rf`), modify the script accordingly.
- No external data transformation is applied; the output is exactly as stored in the OPUS files.

------------------------------------------------------------------------
