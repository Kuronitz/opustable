import os
import glob
import sys
import numpy as np
import pandas as pd
from brukeropus import read_opus

def main():
    if len(sys.argv) < 2:
        print("Usage: python convert.py <opus_folder> [output_csv]")
        print("Example: python convert.py ./opus spectra.csv")
        sys.exit(1)

    opus_folder = sys.argv[1]
    output_csv = sys.argv[2] if len(sys.argv) > 2 else os.path.join(opus_folder, "spectra.csv")

    files = sorted(glob.glob(os.path.join(opus_folder, '*.0')))
    if not files:
        print(f"No .0 files found in {opus_folder}")
        sys.exit(1)

    # Get wavenumbers from first file and round to integers
    first_opus = read_opus(files[0])
    wavenums = first_opus.a.x
    wavenums_int = np.round(wavenums).astype(int)

    # Collect absorbance for each sample
    data = {}
    for file_path in files:
        name = os.path.basename(file_path).replace('.0', '')
        opus = read_opus(file_path)
        data[name] = opus.a.y

    # Build DataFrame: rows = samples, columns = rounded wavenumbers
    df = pd.DataFrame(data).T
    df.columns = wavenums_int
    df = df.reindex(sorted(df.columns, reverse=True), axis=1)  # high to low
    df.reset_index(inplace=True)
    df.rename(columns={'index': 'Sample'}, inplace=True)

    df.to_csv(output_csv, index=False, float_format='%.10f')
    print(f"Saved {df.shape[0]} samples × {df.shape[1]-1} wavenumbers to {output_csv}")

if __name__ == "__main__":
    main()