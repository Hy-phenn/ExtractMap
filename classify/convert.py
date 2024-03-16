import fitz

class Pdf:
    
    def __init__(self, pdf_path, image_format = 'png'):
        self.pdf_document = fitz.open(pdf_path)
        self.page_number = 0
        self.length = len(self.pdf_document)
        self.image_format = image_format

    def next_page(self):
        if self.page_number == self.length:
            return False
        
        print(f"Page {self.page_number+1} of pdf")

        page = self.pdf_document.load_page(self.page_number)
        pixmap = page.get_pixmap()
        image_path = f"classify/temp/image_from_pdf.{self.image_format}"
        pixmap.save(image_path)

        self.page_number += 1
        return image_path


