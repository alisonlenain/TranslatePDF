from cStringIO import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import re

documentName = 'myDocument.pdf'

def convert(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = file(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    return text 

#if you want all pages to be translated, remove the optional 'pages' argument
contents = convert(documentName, pages=[x for x in range(16,41)]) 

#removes footnotes references ("in some paper [5], there is" -> "in some paper, there is")
contents = re.sub(' ?\[\d+]', '', contents).split('\n\n')

contents2 = []
for line in contents:
	#if the whole line is only digits, it is probably the page number, and we don't need that.
    if line and not line.isdigit():
        line = line.replace('\n',' ').replace('  ',' ')
		
		#joins sentences that had been split by page break
        if not '' in line:
            contents2.append(line)
        else:
            contents2[-1] += line.replace('', ' ')

f = open("pdfcontents.txt", "w")
f.write("\n\n".join(contents2))
f.close()

