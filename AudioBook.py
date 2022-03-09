import pyttsx3
import PyPDF2
print("Enter the E-book Name with file extension")
book_name=input("enter the book name with extension")
book=open(book_name,'rb')
pdfReader=PyPDF2.PdfFileReader(book)
pages=pdfReader.numPages
speaker=pyttsx3.init()
for  num in range(23,50):
    page=pdfReader.getPage()
    text=page.extractText()
    speaker.say(text)
    speaker.runAndWait()
