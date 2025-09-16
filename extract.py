import pytesseract
from pdf2image import convert_from_bytes
import requests
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def read_bytes(url):
    """
    Read a pdf from the cloud as bytes
    """
    # Handle GitHub URLs to get raw content
    if 'github.com' in url:
        url = url.replace('github.com', 'raw.githubusercontent.com').replace('/blob/', '/')
    
    response = requests.get(url)
    return response.content

def pdf_to_images(pdf_bytes):
    """
    Convert pdf bytes to a list of images
    """
    images = convert_from_bytes(pdf_bytes)
    return images

def clean_res(text):
    # Normalize Windows/Mac newlines to "\n"
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    
    # Replace tabs with spaces (optional)
    text = text.replace("\t", "    ")
    
    # Strip trailing spaces on each line
    lines = [line.strip() for line in text.split("\n")]
    
    # Rejoin into a clean multiline string
    return "\n".join(lines).strip()

def url_to_text(URL):
    """
    Extract text from a pdf url and return payload
    """
    logger.info(f"Processing PDF: {URL}")
    
    pdf_bytes = read_bytes(URL) 
    logger.info(f"Downloaded PDF of size: {len(pdf_bytes)} bytes")
    
    images = pdf_to_images(pdf_bytes)
    logger.info(f"Converted PDF to {len(images)} images")

    res = {}

    for i, image in enumerate(images):
        text = pytesseract.image_to_string(image)
        res[i] = clean_res(text)
        # res[i] = text
    return res 

if __name__ == "__main__":
    # test pdf url
    URL = 'https://s3.us-east-005.backblazeb2.com/itccims/site/assets/media/students/Adegbokun_Obaloluwa_fae2977b-f84b-4502-a4f0-698942a4c483/230875/2024-2025/IT-UI-014_job_reporting_form_2025-09-04_16-24-01-722740_def08017-5b4d-49ed-b620-f37d3096807c.pdf'
    response = url_to_text(URL)
    print(response)