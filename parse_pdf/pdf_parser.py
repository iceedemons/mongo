# import PyPDF2
# import pprint
from pathlib import Path

dir = Path(r'L:\Projects - Proposals\P14500 - P14599\P14531 FTS SP Oil and Gas - Kakinada FPSO\10 Miscellaneous Data')

from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import os


# converts pdf, returns its text content as a string
def convert(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = open(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close()
    return text


def convertMultiple(pdfDir, txtDir):
    if pdfDir == "": pdfDir = os.getcwd() + "\\"  # if no pdfDir passed in
    for pdf in os.listdir(pdfDir):  # iterate through pdfs in pdf directory
        fileExtension = pdf.split(".")[-1]
        if fileExtension == "pdf":
            pdfFilename = str(pdfDir) + "\\" + pdf
            text = convert(pdfFilename)  # get string of text content of pdf
            textFilename = str(txtDir) + "\\" + pdf + ".txt"
            textFile = open(textFilename, "w")  # make text file
            textFile.write(str(text.encode("utf-8")))  # write text to text file
        # textFile.close


pdfDir = dir
txtDir = dir
convertMultiple(pdfDir, txtDir)