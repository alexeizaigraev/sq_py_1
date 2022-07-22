import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *
from papa_pg import *

class Otbor():
    def __init__(self, choise):
        self.choise = choise

    def otbor_main(self):
        info = ''
        arr = []
        choise = self.choise
        if ' ' in choise:
            start, finish = choise.split(' ')
            if len(start) == len(finish):
                start, finish = int(start), int(finish) + 1
            else:
                finish = int( start[: (len(start) - len(finish))] + finish ) + 1
                start = int(start)

        else:
            start = int(choise)
            finish = start + 1

        for x in range(start, finish):
            dep, term = str(x), str(x*10+1)
            arr.append([term, dep])
            info += f'{term} {dep}\n'
        insert_all_otbor(arr)
        self.info = info
        
