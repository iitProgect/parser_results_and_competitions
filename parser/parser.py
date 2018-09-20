from yargy import Parser, rule, and_, or_
from yargy.predicates import gram, is_capitalized, dictionary, is_upper, length_eq
import pathlib


GEO = rule(
     and_(
         is_upper(),
         or_(
            length_eq(2),
            length_eq(3)
         )
        )

)


parser = Parser(GEO)
text = '''
В Чеченской республике  ОК-12 на день рождения ...
Донецкая народная республика провозгласила ...
Башня Федерация — одна из самых высоких ...
'''
def FindFGOS(text):
    for match in parser.findall(text):
        code_FGOS = match.tokens[0].value+text[match.tokens[0].span[1]]+text[match.tokens[0].span[1]+1]
        if text[match.tokens[0].span[1]+2].isdigit():
            code_FGOS = code_FGOS + text[match.tokens[0].span[1]+2]
        print(code_FGOS)
        return [_.value for _ in match.tokens]

FindFGOS(text)




