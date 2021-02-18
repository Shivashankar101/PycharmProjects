import PyPDF2

f = open('/Users/shiv/Desktop/CV/CV_Shivashankar.pdf', 'rb')

pdf_reader = PyPDF2.PdfFileReader(f)
page_one = pdf_reader.getPage(1)
# page_one_text = page_one.extractText()
# print(page_one_text)

pdf_text = []

pdf_writer = PyPDF2.PdfFileWriter()
pdf_writer.addPage(page_one)
page_output = open('/Users/shiv/Downloads/old downloaded docs/Resume pdf.pdf', 'wb')
pdf_writer.write(page_output)
print(pdf_writer)
f.close()

# f2 = open('/Users/shiv/Downloads/old downloaded docs/Resume pdf.pdf', 'rb')
#
# written_page_read = PyPDF2.PdfFileReader(f2)
#
# new_pdf = written_page_read.extractText()
#
# print(new_pdf)

# for p in range(written_pdf.numPages):
#     page = written_pdf.getPage(p)
#
#     pdf_text.append(page.extractText())
#
# print(pdf_text)
#
