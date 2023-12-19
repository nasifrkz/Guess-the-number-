import pyttsx3
import PyPDF2

file = open("book.pdf", "rb")
pdfReader = PyPDF2.PdfReader(file)
page = len(pdfReader.pages)
print(page)
speaker = pyttsx3.init()

page = pdfReader.pages[40]
text = page.extract_text()
speaker.say(text)
speaker.runAndWait()


