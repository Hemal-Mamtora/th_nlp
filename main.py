import fitz

path = "/home/hemal/th/nlp/training_invoices/training/Invoice 630559.pdf"

doc = fitz.open(path)

for page in doc:  # iterate the document pages
    textpage = page.get_textpage()
    text = textpage.extractBLOCKS()  # get plain text (is in UTF-8)
    print(text)  # write text of page