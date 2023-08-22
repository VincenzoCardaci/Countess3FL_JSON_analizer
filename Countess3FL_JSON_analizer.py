import os
import json
import pandas as pd

# Variables to keep track of the number of analyzed folders and files
num_folders_analyzed = 0
num_files_analyzed = 0

# Extract information from JSON files from viability reading
def extract_info_type1(data):
    info_list = []
    for entry in data:
        for cell in entry["Cells"]:
            info_list.append({
                "CellType": entry["CellType"],
                "Size": cell["Size"],
                "Circularity": cell["Circularity"],
                "FluorescentBrightness": None,
                "LightIntensity": None,
                "NormalizedLightIntensity": None,
            })
    return info_list

# Extract information from JSON files in Fluorescent reading
def extract_info_type2(data):
    info_list = []
    for entry in data:
        for cell in entry["Cells"]:
            info_list.append({
                "CellType": entry["CellType"],
                "Size": cell["Size"],
                "Circularity": cell["Circularity"],
                "FluorescentBrightness": cell["FluorescentBrightness"][0],
                "IsFluorescent": cell["IsFluorescent"][0],
                "LightIntensity": entry["LightIntensity"],
                "NormalizedLightIntensity": entry["NormalizedLightIntensity"],
            })
    return info_list

# Analyze a single JSON file
def analyze_single_json(file_path):
    global num_files_analyzed
    with open(file_path, "r") as file:
        data = json.load(file)
        if "CellType" in data[0]:
            num_files_analyzed += 1
            if data[0]["CellType"] == "Live":
                return extract_info_type1(data)
            elif data[0]["CellType"] in ["Brightfield", "Epi1"]:
                return extract_info_type2(data)
    return None

# Analyze all JSON files within folders and subfolders
def analyze_all_jsons(folder_path):
    global num_folders_analyzed
    all_info = {}
    for root, _, files in os.walk(folder_path):
        num_folders_analyzed += 1
        for file in files:
            if file.endswith(".json"):
                file_path = os.path.join(root, file)
                info_list = analyze_single_json(file_path)
                if info_list:
                    all_info[file] = info_list
    return all_info

# Create an Excel file with extracted data
def create_excel_file(data, output_path):
    with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
        for file, info_list in data.items():
            df = pd.DataFrame(info_list)
            df.to_excel(writer, sheet_name=file, index=False)

def main():
    global num_folders_analyzed, num_files_analyzed
    while True:
        choice = input("Do you want to analyze a single JSON file or all JSON files in folders and subfolders? (single/all): ")

        if choice.lower() == "single":
            file_path = input("Enter the path of the JSON file: ")
            info = analyze_single_json(file_path)
            if info:
                folder_path, file_name = os.path.split(file_path)
                output_file = f"{os.path.splitext(file_name)[0]}.xlsx"
                output_path = os.path.join(folder_path, output_file)
                create_excel_file({file_name: info}, output_path)
                print(f"The data has been saved to the file {output_file}.")
            else:
                print("Invalid JSON file or unsupported type.")
        elif choice.lower() == "all":
            folder_path = input("Enter the folder path: ")
            info = analyze_all_jsons(folder_path)
            if info:
                folder_name = os.path.basename(folder_path)
                output_file = f"{folder_name}.xlsx"
                output_path = os.path.join(folder_path, output_file)
                create_excel_file(info, output_path)
                print(f"The data has been saved to the file {output_file}.")
            else:
                print("No valid JSON files found in the folder.")
        else:
            print("Invalid choice. You must type 'single' or 'all'.")

        print(f"Number of analyzed folders: {num_folders_analyzed}")
        print(f"Number of analyzed files: {num_files_analyzed}")

        continue_choice = input("Do you want to perform another analysis? (yes/no): ")
        if continue_choice.lower() != "yes":
            break

if __name__ == "__main__":
    main()
