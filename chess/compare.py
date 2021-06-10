import hashlib
import time

randText1 = str(open("src/board.csv","r",encoding='utf-8'))
randText2 = str(open("src/board.csv","r",encoding='utf-8'))

print(randText1 == randText2)