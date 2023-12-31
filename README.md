# Countess3FL_JSON_analizer
 The Countess3FL_JSON_Analyzer is a Python program designed to extract and analyze information from JSON files generated by the Countess™ 3 FL Automated Cell Counter (Invitrogen™).

## Description
 The Countess3FL_JSON_Analyzer is a Python program designed to extract and analyze information from JSON files generated by the Countess™ 3 FL Automated Cell Counter (Invitrogen™). The program supports two types of JSON files derived from the analysis of readings in either brightfield or fluorescence modes. It provides functionality to process both individual JSON files and all JSON files within a specified directory and its subdirectories. The extracted data is then organized and saved into an Excel file for easy access and further analysis.

## Features
- **Extract Information:** The program can extract relevant data (Viability, Size, Circularity, FluorescentBrightness, LightIntensity,NormalizedLightIntensity) from two types of JSON files derived from the Countess™ 3 FL Automated Cell Counter (Invitrogen™) instrument's analysis of readings in brightfield and fluorescence modes.

- **Single File Analysis:** Users can analyze a single JSON file by providing its path. The program determines the type of the JSON data based on the "CellType" field and extracts the relevant information accordingly.

- **Batch Analysis:** The program can analyze all JSON files within a specified directory and its subdirectories. It processes each file, identifies its type, extracts the appropriate data, and compiles it into an Excel file.

- **Output Excel File:** Extracted data is stored in an Excel file (.xlsx), with each JSON file's data placed on a separate sheet named after the file. This allows users to conveniently view and manipulate the collected data.

## How to Use
1. Run the program using a Python interpreter (Python 3.6 or higher is recommended).
2. Choose whether to analyze a single JSON file or all JSON files in a directory.
3. Depending on your choice:
   - For single file analysis, provide the path to the JSON file without the quotation marks.
   - For batch analysis, provide the path to the directory containing JSON files without quotation marks.
4. The program will process the JSON files, determine their type, extract relevant data, and create an output Excel file in the same location.

## Dependencies
The program relies on the following libraries, which should be installed using `pip` if not already present:
- `os`: For working with file and directory paths.
- `json`: For loading and parsing JSON data.
- `pandas`: For creating and managing data structures (DataFrames) and Excel output.

## Note
- Ensure that the JSON files are generated by the Countess™ 3 FL Automated Cell Counter instrument and contain the necessary data fields.
- The program automatically categorizes JSON files into two types based on the presence of the "CellType" field.

## Author
This program was developed by Vincenzo Cardaci ([vincenzocardaci.com](https://www.vincenzocardaci.com)).

## License
This program is provided under the MIT License. Please refer to the LICENSE file for more details.

Feel free to modify and enhance the program to match your requirements.

## Disclaimer
This program is provided as-is and without any warranties. The author is not responsible for any issues arising from its use. Always review and test the program before using it on critical data.
