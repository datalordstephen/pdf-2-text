from fastapi import FastAPI
from pydantic import BaseModel 
from extract import url_to_text

app = FastAPI()

class PDF(BaseModel):
    url: str

@app.get("/to-text")
def convert_pdf_to_text(pdf: PDF):
    response = url_to_text(pdf.url)
    res = {"status-code": 200, "data": response}
    return res
