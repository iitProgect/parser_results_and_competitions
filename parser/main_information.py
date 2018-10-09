from yargy import Parser, rule, and_, or_
from yargy.predicates import gram, is_capitalized, dictionary, is_upper, length_eq, is_title
from docx import Document, section
from docx.shared import Inches
import os, subprocess

baseDir = r'C:\Users\Катя\Desktop\рпд'

def GetDocuments():
    documents = []
    for filename in os.listdir(baseDir):
        if filename.endswith('.docx'):
            documents.append(filename)
    return documents

documents = GetDocuments()
path = baseDir + '\\'+documents[6]
print(path)
document = Document(path)
header  = section.header
print(document.header)