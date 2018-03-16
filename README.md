# TranslatePDF
Extracts text from PDF while keeping some layout, and translates it using the DeepL API.

## How to use this code
Open PDFextracter.py, change the name of the documentName to the name of your PDF. The code is now ready to be executed!
PDFextracter.py will create a pdfcontents.txt file, containing the contents of the PDF file. You can have a look at it to make sure the PDF has been extracted properly and make some manual edits if needed.

Once PDFextracter.py has been executed, run deepl.py, it will read the the pdfcontents.txt file, translate it, and put the results in a new file called traduction.txt.
