from yargy import Parser, rule, and_, or_
from yargy.predicates import gram, is_capitalized, dictionary, is_upper, length_eq, is_title
from docx import Document
from docx.shared import Inches
import os

def GetDocuments():
    documents = []
    for filename in os.listdir(baseDir):
        if filename.endswith('.docx'):
            documents.append(filename)
    return documents

from yargy.tokenizer import TokenRule
from yargy.tokenizer import Tokenizer

CODE_RULE = TokenRule('Code', '\d{2}.\d{2}.\d{2}(?!\d)')
tokenizer = Tokenizer()
tokenizer.remove_types('EOL','LATIN','RU','INT','PUNCT','OTHER')
tokenizer.add_rules(CODE_RULE)




baseDir = r'C:\Users\Катя\Desktop\рпд'
documents = GetDocuments()
path = baseDir + '\\'+documents[13]
print(path)
document = Document(path)
def FindName():
    for table in document.tables:
        for row in table.rows:
            for cell in row.cells:
                if len(list(tokenizer(cell.text))) > 0:
                    span = list(tokenizer(cell.text))[0].span
                    return cell.text[span[0]:cell.text.find('\n', span[0])]
    for i in document.paragraphs:
        if len(list(tokenizer(i.text))) == 1:
            print(list(tokenizer(i.text)))
            return i.text



print(FindName())
