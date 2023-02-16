#!python

import argparse
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import io



def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = io.StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos = set()

    for page in PDFPage.get_pages(args.infile, pagenos, maxpages=maxpages,
                                  password=password,
                                  caching=caching,
                                  check_extractable=True):
        interpreter.process_page(page)
        if args.separate_pages:
            pass

    fp.close()
    device.close()
    text = retstr.getvalue()
    retstr.close()
    fixed = []
    for line in text.split('\n'):
        if len(line) < 10:
            continue
        if '©' in line:
            continue
        fixed.append(line)
    return "\n".join(fixed)

def paper2txt_main():
    parser = argparse.ArgumentParser(description="Converts scientific papers to txt")
    parser.add_argument('infile',  nargs=1, help="Input file")
    parser.add_argument('outfile', nargs=1, help="Output file")
    parser.add_argument('-p', '--separate-pages')
    args = parser.parse_args()

    with open(args.outfile, 'w') as out:
        out.write(convert_pdf_to_txt(args.infile))
    
