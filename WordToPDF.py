"""
docx_to_pdf.py

Batch convert .docx files to .pdf format using docx2pdf.
"""

import os
from docx2pdf import convert

# Define the folder path containing .docx files
FOLDER_PATH = r"Your Path"

def batch_convert():
    """
    Loop through all .docx files in the folder
    and convert them to .pdf format.
    """
    for file_name in os.listdir(FOLDER_PATH):
        if file_name.lower().endswith(".docx"):
            input_path = os.path.join(FOLDER_PATH, file_name)
            output_path = os.path.splitext(input_path)[0] + ".pdf"

            try:
                convert(input_path, output_path)
                print(f"[OK] Converted: {file_name} -> {os.path.basename(output_path)}")
            except Exception as e:
                print(f"[ERROR] Failed to convert {file_name}: {e}")

    print("All Word documents converted successfully.")

if __name__ == "__main__":
    batch_convert()
