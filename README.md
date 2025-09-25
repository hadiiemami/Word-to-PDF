# DOCX to PDF Converter

A simple Python tool for batch converting `.docx` Word documents into `.pdf` format using [docx2pdf](https://github.com/AlJohri/docx2pdf).

---

## Features
- Batch convert all `.docx` files in a folder to `.pdf`.
- Output files are saved in the same folder with the same name.
- Minimal and easy to use.

---

## Requirements

- Python 3.8+
- Install required library:
```bash
pip install docx2pdf
```
- On Windows, Microsoft Word must be installed because `docx2pdf` uses it for conversion.

---

## Usage

1. Edit the script `docx_to_pdf.py` and set your folder path:

```python
FOLDER_PATH = r"Your Path"
```

2. Run the script:

```bash
python docx_to_pdf.py
```

3. Each `.docx` file will be converted to `.pdf` with the same name in the same folder.

---

## Notes
- This script only processes `.docx` files, not `.doc` or other formats.
- Conversion requires Microsoft Word installed on the system (Windows only).
- Tested on Windows with Python 3.10+.

---

## License
This project is licensed under the MIT License.
