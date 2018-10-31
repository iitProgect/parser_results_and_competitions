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


CODE_RULE = TokenRule('Code', '\d+\d+.\d+\d+.\d+\d+')
tokenizer = Tokenizer()
tokenizer.remove_types('EOL','LATIN','RU','INT','PUNCT','OTHER')
tokenizer.add_rules(CODE_RULE)




baseDir = r'C:\Users\Катя\Desktop\рпд'
documents = GetDocuments()
path = baseDir + '\\'+documents[3]
print(path)
document = Document(path)
def FindName():
    for i in document.paragraphs:
        print(i.text)
        if len(list(tokenizer(i.text))) > 0:
            return i.text
        for table in document.tables:
            for row in table.rows:
                for cell in row.cells:
                    if len(list(tokenizer(cell.text))) > 0:
                        span = list(tokenizer(cell.text))[0].span
                        return cell.text[span[0]:cell.text.find('\n', span[0])]


for row in document.tables[1].rows:
    print(row.cells[0])
# print(FindName())

