import PyPDF2
import img2pdf
import os
from tkinter import filedialog

readMe = """THE PYTHON PDF HANDLER v0.1

---Features---

1 -> Merge two or more PDF documents
2 -> Make an array of pictures into a PDF
3 -> Delete a page or range of pages in a PDF
4 -> Slice a PDF with a range
EXT -> Exit the programm
"""

print(readMe)

ans = ""
while True:
    ans = input(">>>")
    if ans=="1":
        print("Select the pdfs you want to merge in order...")
        tupOfPdfs = filedialog.askopenfilenames()
        name = input("Name of new merged PDF:")
        print("Select where you want to save the new PDF file...")
        newPdfDir = filedialog.askdirectory()
        newPdfDir.replace("/","\\")
        merger = PyPDF2.PdfWriter()
        for pdf in tupOfPdfs:
            merger.append(PyPDF2.PdfReader(pdf.replace("/","\\")))
        out = open(newPdfDir+"\\"+name+".pdf","wb")
        merger.write(out)
        merger.close()
        out.close()
        print("DONE!!!")
        os.popen("start "+newPdfDir+"\\"+name+".pdf")
    elif ans=="2":
        print("Select the images you want to turn into a PDF in reverse order...")
        imagesTup = filedialog.askopenfilenames()
        imagesList = []
        for img in imagesTup:
            imagesList.append(img.replace("/","\\"))
        print("Insert the name of the new pdf file")
        name = input(">>>")
        print("Select where you want to save the new pdf file")
        newPdfDir = filedialog.askdirectory()
        newPdfDir.replace("/","\\")
        #merger = PyPDF2.PdfWriter() - can't do it with PyPDF2
        with open(newPdfDir+"\\"+name+".pdf","wb") as newPdfFile:
            newPdfFile.write(img2pdf.convert([i for i in imagesList]))
        newPdfFile.close()
        print("DONE!!!")
        os.popen("start "+newPdfDir+"\\"+name+".pdf")
    elif ans=="3":
        print("Select the pdf's location...")
        pdfLocation = filedialog.askopenfile()
        pdfLocation = (pdfLocation.name).replace("/","\\")
        print(pdfLocation)
        newPdfName = ""
        print("Insert new pdf file name:")
        ans = input(">>>")
        newPdfName = ans
        print("Select where to save the new PDF file...")
        pdfDir = filedialog.askdirectory()
        pdfDir.replace("/","\\")
        print("Insert pages or ranges of pages to be deleted (e.g. 4,6-9,10)")
        ans = input(">>>")
        ans = ans.split(",")
        pdfFile = PyPDF2.PdfReader(pdfLocation)
        merger = PyPDF2.PdfWriter()
        nonIncludedPages=[]
        for request in ans:
            if "-" in  request:
                request = request.split("-")
                for j in range(int(request[0]),int(request[1])+1):
                    nonIncludedPages.append(j) #doesn't cut the right pages, maybe the problem is somewhere here
            else:
                nonIncludedPages.append(request)
        for i in range(len(pdfFile.pages)):
            if i+1 not in nonIncludedPages:
                merger.add_page(pdfFile.pages[i])
        out = open(pdfDir+"\\"+newPdfName+".pdf","wb")
        merger.write(out)
        merger.close()
        out.close()
        print("DONE!!!")
        os.popen("start "+pdfDir+"\\"+newPdfName+".pdf")

    elif ans=="4":
        print("Select the pdf file location...")
        pdfLocation = filedialog.askopenfile()
        pdfLocation = (pdfLocation.name).replace("/","\\")
        newPdfName = ""
        print("Insert new pdf file name:")
        ans = input(">>>")
        newPdfName = ans
        print("Select where you want to save the new pdf file...")
        pdfDir = filedialog.askdirectory()
        pdfDir.replace("/","\\")
        print("Insert range of slice (e.g. 4-10)")
        ans = input(">>>")
        ans = ans.split("-")
        pdfFile = PyPDF2.PdfReader(pdfLocation)
        merger = PyPDF2.PdfWriter()
        merger.append(fileobj=pdfFile,pages=(int(ans[0])-1,int(ans[1])))
        out = open(pdfDir+"\\"+newPdfName+".pdf","wb")
        merger.write(out)
        merger.close()
        out.close()
        print("DONE!!!")
        os.popen("start "+pdfDir+"\\"+newPdfName+".pdf")
    elif ans=="EXT":
        break
    else:
        print("Invalid command, try again...")