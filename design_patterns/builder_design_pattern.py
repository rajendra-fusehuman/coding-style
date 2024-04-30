from abc import ABC, abstractmethod
from fpdf import FPDF


class DocumentBuilder(ABC):
    @abstractmethod
    def add_title(self, title):
        pass

    @abstractmethod
    def add_body(self, body):
        pass

    @abstractmethod
    def get_document(self):
        pass

    @abstractmethod
    def save_to_file(self, filename):
        pass


class PDFDocumentBuilder(DocumentBuilder):
    def __init__(self):
        self.pdf = FPDF()

    def add_title(self, title):
        self.pdf.add_page()
        self.pdf.set_font("Times", size=14)
        self.pdf.cell(200, 10, txt=title, ln=True, align="C")

    def add_body(self, body):
        self.pdf.set_font("Times", size=12)
        self.pdf.multi_cell(0, 10, txt=body)

    def get_document(self):
        return self.pdf

    def save_to_file(self, filename):
        self.pdf.output(filename)


class HTMLDocumentBuilder(DocumentBuilder):
    def __init__(self):
        self.document = ""

    def add_title(self, title):
        self.document += f"<h1>{title}</h1>\n"

    def add_body(self, body):
        self.document += f"<p>{body}</p>\n"

    def get_document(self):
        return f'''<!DOCTYPE html>\n<html>\n<head><title>Generated HTML
                Document</title></head>\n<body>\n{self.document}</body>\n
                </html>
                '''

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            f.write(self.get_document())


class PlainTextDocumentBuilder(DocumentBuilder):
    def __init__(self):
        self.document = {}

    def add_title(self, title):
        self.document['title'] = title

    def add_body(self, body):
        self.document['body'] = body

    def get_document(self):
        return f'''Plain Text Document:\nTitle: {self.document['title']}\n
                Body: {self.document['body']}
                '''

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            f.write(self.get_document())


class DocumentDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct_document(self, title, body):
        self.builder.add_title(title)
        self.builder.add_body(body)
        return self.builder.get_document()


if __name__ == "__main__":
    pdf_builder = PDFDocumentBuilder()
    pdf_director = DocumentDirector(pdf_builder)
    pdf_document = pdf_director.construct_document("Title",
                                                   "PDF Body. Hello World!!!")
    print(pdf_document)
    pdf_builder.save_to_file("pdf_document.pdf")

    html_builder = HTMLDocumentBuilder()
    html_director = DocumentDirector(html_builder)
    html_document = html_director.construct_document("Title",
                                                     '''HTML Body.
                                                      Hello World!!!''')
    print(html_document)
    html_builder.save_to_file("html_document.html")

    plain_text_builder = PlainTextDocumentBuilder()
    plain_text_director = DocumentDirector(plain_text_builder)
    plain_text_document = plain_text_director.construct_document("Title",
                                                                 '''Plain Text
                                                                 Body. Hello
                                                                 World!!!''')
    print(plain_text_document)
    plain_text_builder.save_to_file("text_document.txt")
