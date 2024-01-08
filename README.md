# FindTables
This repository contains a Python script for efficiently extracting table names and field names from various file types, including .SAS, .SQL, and .EGP. The script is designed to search within specified directories, identify files with these extensions, and parse them to extract relevant data based on defined criteria. 
Key Features:
- Supports .SAS, .SQL, and .EGP file formats.
- Modular design for easy understanding and maintenance.
- Extracts specified words or patterns from files.
- Processes .EGP files as ZIP archives to access contained .SAS files.
- Generates a consolidated CSV file with extracted data.
- Includes logging functionality to track the script's execution process, successful completions, warnings, and errors.
- Ideal for data analysis, migration projects, or automated documentation of database schemas.

How to Use:
1. Update the script with the path to the source directory.
2. Define the file extensions and search terms as per your requirements.
3. Run the script to process the files and generate a CSV output.
4. Check the log file for detailed execution logs.

This script is beneficial for developers, data analysts, and database administrators who regularly work with SQL and SAS-based environments and need an automated way to document or analyze database structures.

Contributions and suggestions for enhancements are welcome!
