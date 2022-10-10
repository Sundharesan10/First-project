import PyPDF2
import pyttsx3


path = open('your_pdf_name.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(path)

from_page = pdfReader.getPage(0)

text = from_page.extractText()

speak = pyttsx3.init()
speak.say(text)
speak.runAndWait()