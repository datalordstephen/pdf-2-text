# PDF to Text Extractor

This project demonstrates how to extract text from PDF files using Python.  
It combines `pdf2image` to convert PDF pages into images and OCR libraries like `pytesseract` and `easyocr` (coming soon) to extract text from those images.  

## Features
- Extract raw or structured text from PDF pages
- Works with scanned PDFs (coming soon) as well as normal ones
- Supports integration with cloud-stored files (e.g., GitHub raw links, S3, etc.) and local files (coming soon)

## Setup

It’s recommended to use a Python virtual environment.

```bash
# 1. Clone the repository
git clone https://github.com/datalordstephen/pdf-2-text.git
cd pdf-2-text

# 2. Create a virtual environment
python -m venv venv

# 3. Activate the environment
# On Linux/Mac:
source venv/bin/activate
# On Windows (PowerShell):
venv\Scripts\Activate.ps1

# 4. Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
