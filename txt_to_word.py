from docx import Document
import os

path = "./text/"

file_list = os.listdir(path)

if not os.path.exists("./output"):
    os.makedirs("./output")

for file in file_list:
    filename = os.path.splitext(file)[0]
    document = Document()
    document.add_heading(filename, 0)

    file_contents = open(path + file, encoding='utf-8').read()

    p = document.add_paragraph(file_contents)
    
    document.save('./output/' + filename + '.docx')
