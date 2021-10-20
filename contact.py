
import csv
import os
import subprocess
import PyPDF2


# calling bat file to give all pdf name in text file
subprocess.call(['allfilenames.bat'])

with open('filenames.txt') as f:
    content = f.readlines()
    li = [x.strip() for x in content]
    



def getDetails(fileName):
    newdata = []
    pdfFileObj = open(fileName, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pageObj = pdfReader.getPage(0)
    mainContent = pageObj.extractText().upper()

    # Find Name & Contact
    name = mainContent.find("NAME",mainContent.find("NAME")+1)+5
    add = mainContent.find("ADD")
    contact = mainContent.find("CONTACT")+9
    auth = mainContent.find("AUTH")

    # Extract Name & Contact
    print("#######################")
    print(mainContent[name:add].strip())
    print("****************")
    print(mainContent[contact:auth].strip())

    print("#######################")

    newdata.append(mainContent[name:add].strip())
    newdata.append(mainContent[contact:auth].strip())

    with open('newcsv.csv', 'a', newline='\n') as newcsv:
        
        csvwriter = csv.writer(newcsv)
        csvwriter.writerow(newdata)

for i in range(len(li)):
    getDetails(li[i])

    
