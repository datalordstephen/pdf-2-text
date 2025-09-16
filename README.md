# PDF to Text Extractor
A powerful FastAPI-based service that extracts text from PDF documents using OCR (Optical Character Recognition). Built with `pytesseract` and `pdf2image`, this API can handle both text-based and image-based PDFs (coming soon).

## Features
- Extract raw or structured text from PDF pages
- Works with scanned PDFs (coming soon) as well as normal ones
- Supports integration with cloud-stored files (e.g., GitHub raw links, S3, etc.) and local files (coming soon)

## Example Usage (Online)

Using Python requests:

```python
import requests

# Upload and extract text from PDF
API_URL = "https://pdf-to-text-api-gu6m.onrender.com/to-text/"
file_url = <url-of-your-pdf>

payload = {"url": file_url}

response = requests.post(API_URL, json = payload)
result = response.json()

print("Extracted text:", result["data"])
```

## Local Setup

### Prerequisites

* Python 3.8+
* Tesseract OCR engine
* Poppler utilities

It’s recommended to use a Python virtual environment.

### 1. Clone the repository
```bash
git clone https://github.com/datalordstephen/pdf-2-text.git
cd pdf-2-text
```

### 2. Install dependencies

#### Linux
```bash
sudo apt-get update
sudo apt-get install tesseract-ocr tesseract-ocr-eng poppler-utils
```

#### macOS
```bash
brew install tesseract poppler
```

#### Windows
* Install [TesseractOCR](https://pypi.org/project/pytesseract/)
* Install [Poppler/pdf2image](https://pypi.org/project/pdf2image/)

```bash
python -m venv venv
```

### 3. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 4. Run Locally
```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Local URL: `http://127.0.0.1:8000/to-text`
