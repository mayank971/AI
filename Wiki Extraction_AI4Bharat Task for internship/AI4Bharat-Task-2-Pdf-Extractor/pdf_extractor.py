import pandas as pd
import requests
from bs4 import BeautifulSoup
from pathlib import Path
from pdf2image import convert_from_path
from PIL import Image
import pytesseract
from urllib.parse import urlsplit
import json
# My custom python codes
# from link_extractor import LinkExtractor


pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files(x86)\Tesseract-OCR\tesseract.exe"

Url=pd.read_csv("data_pdf.csv")["Url"]

webbased_url=[]
pdfbased_url=[]


for y in Url:
    if ".pdf" in y:
        try:
            text_obj=Pdf2processor(y)
            pdfbased_url.append({"page-url":str(y),"pdf-url":str(y),"pdf-content":text_obj.generate_text()})
        except:
            continue
    else:
        try:
            obj=LinkExtractor(y)
            text_obj=Pdf2processor(obj.get_pdf_link())
            webbased_url.append({"page-url":str(y),"pdf-url":str(obj.get_pdf_link()),"pdf-content":text_obj.generate_text()})
        except:
            continue
        

json_object=webbased_url+pdfbased_url
json_object=json.dumps(json_object,indent=3)
print(json_object)

with open("pdf_data.json", "w") as outfile:
    outfile.write(json_object)