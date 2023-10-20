from PyPDF2 import PdfReader, PdfWriter,PdfMerger
import img2pdf
class project():
    
    # Merging all the Pdf's in Single Pdf
    def merger(self,pdfs):
        merger=PdfMerger()
        for pdf in pdfs:
            merger.append(pdf)
        merger.write("result.pdf")
        return merger.close()
    
    #Split single Pdf into Mutliple Pdfs
    def split(self,pdfs):
        reader=PdfReader(pdfs)
        for pdf in range(len(reader.pages)):
            writer=PdfWriter()
            writer.add_page(reader.pages[pdf])
            with open(f"splitpages{pdf+1}.pdf",'wb') as output:
                writer.write(output)

    #Encrypt thr PDf File
    def encrypt(self,file):
        filename=PdfReader(file)
        output=PdfWriter()
        for i in range(len(filename.pages)):
            pagedetail=filename.pages[i]
            output.add_page(pagedetail)
        password='1234'
        output.encrypt(password)
        with open("encryptedresult.pdf",'wb') as files:
            output.write(files)

    #COnvert the pdf into text format
    def extract(self,pdfs):
        reader=PdfReader(pdfs)
        textformats=''
        for pdf in range(len(reader.pages)):
            page=reader.pages[pdf]
            textformats+=page.extract_text()
        with open("textformat.txt",'w' , encoding='utf-8') as output:
            output.write(textformats) 
    
    #Convert the jpg's,png,tiff into pdf

    def conversion(self,images):
        with open("images2.pdf",'wb') as pdf:
            pdf.write(img2pdf.convert(images))

obj=project()

obj.merger(['sample.pdf','sample1.pdf'])


obj.split('result.pdf')

obj.encrypt('result.pdf')

obj.extract("result.pdf")

obj.conversion(['jpeg.jpg','png.png','tiff.tiff'])

