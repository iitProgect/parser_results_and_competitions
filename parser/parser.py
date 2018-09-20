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
В Чеченской республике  ОК-1 на день рождения ...
Донецкая народная республика провозгласила ...
Башня Федерация — одна из самых высоких ...
'''
for match in parser.findall(text):
    print([_.value for _ in match.tokens])








