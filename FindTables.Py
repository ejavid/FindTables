import os
import zipfile
import pandas as pd
import logging


def setup_logging():
    """
    Sets up the logging configuration.
    """
    logging.basicConfig(filename='script_log.log', level=logging.INFO,
                        format='%(asctime)s:%(levelname)s:%(message)s')

def log_message(message, level="info"):
    """
    Logs a message at the specified level.

    Parameters:
    message (str): Message to log.
    level (str): Logging level ('info', 'warning', or 'error').
    """
    if level == "info":
        logging.info(message)
    elif level == "warning":
        logging.warning(message)
    elif level == "error":
        logging.error(message)

def extract_files(source_directory, extensions):
    """
    Extracts file paths for files with specified extensions.

    Parameters:
    source_directory (str): Directory to search for files.
    extensions (list of str): List of file extensions to search for.

    Returns:
    list of str: List of file paths.
    """
    file_paths = []
    for root, dirs, files in os.walk(source_directory):
        for file in files:
            if any(file.upper().endswith(ext.upper()) for ext in extensions):
                file_paths.append(os.path.join(root, file))
    return file_paths

def extract_words_from_file(file_path, match_words):
    """
    Extracts words that match criteria from a given file.

    Parameters:
    file_path (str): Path to the file.
    match_words (list of str): Words to match in the file.

    Returns:
    list of [str, str]: List containing file path and matched word.
    """
    extracted_data = []
    with open(file_path, "r") as f:
        for line in f:
            for word in line.split():
                if any(word.upper().startswith(mw.upper()) for mw in match_words):
                    extracted_data.append([file_path, word])
    return extracted_data

def process_egp_files(source_directory, destination_directory):
    """
    Extracts contents of .EGP files to a destination directory.

    Parameters:
    source_directory (str): Directory to search for .EGP files.
    destination_directory (str): Directory to store extracted files.
    """
    for root, dirs, files in os.walk(source_directory):
        for file in files:
            if file.upper().endswith(".EGP"):
                path = os.path.join(root, file)
                with zipfile.ZipFile(path) as zf:
                    zf.extractall(destination_directory)    
                       
# Main execution
if __name__ == "__main__":
    setup_logging()
    log_message("Script execution started.")

    source_dir = "C:/Users/Ehsan/Desktop/python-oo-practice"
    destination_dir = "C:/Users/Ehsan/Desktop/python-oo-practice"
    extensions = [".SAS", ".SQL", ".EGP"]
    match_words = ["Matchwords", "Other words"]

    try:
        process_egp_files(source_dir, destination_dir)
        file_paths = extract_files(source_dir, extensions)
        file_paths += extract_files(destination_dir, [".SAS"])

        if not file_paths:
            log_message("No files found matching the specified extensions.", "warning")

        all_extracted_data = []
        for file_path in file_paths:
            extracted_data = extract_words_from_file(file_path, match_words)
            if extracted_data:
                all_extracted_data += extracted_data

        if all_extracted_data:
            df = pd.DataFrame(all_extracted_data, columns=["Path", "Source"])
            df.to_csv("Output.csv", index=False)
        else:
            log_message("No matching words found in the files.", "warning")

        log_message("Script execution completed successfully.")
    except Exception as e:
        log_message(f"Error occurred: {e}", "error")
